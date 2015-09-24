# -*- coding:utf-8 -*-

from time import sleep
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.touch_action import TouchAction
from sc_action import picture
from sc_action import device_info
from sc_action import action_word
from sc_action.libs.result import case_res, failed_path
from sc_action.libs import result, exe_status

import copy
import string
import logging
import logging.config

logger = logging.getLogger("log_NB")


class NB():
    def __init__(self, driver=None):
        """
        @type driver:WebDriver
        """
        self.driver = driver
        self.action = TouchAction(self.driver)
        self.aw = action_word.ActionWord(driver)

    def add_book(self, topic):

        self.driver.find_element_by_name("NB.BookShelf.SearchField").click()
        self.driver.find_element_by_name("NB.BookShelf.SearchField").set_value(self.aw.get_par_list(topic)[1])
        self.driver.find_element_by_name("搜索").click()
        # self.driver.find_element_by_name(self.aw.get_par_list(topic)[1]).click()
        self.driver.find_element_by_xpath('//*[@name="' + "加入书架" + '"]').click()
        self.aw.delete_windows()
        self.driver.find_element_by_name("Menu").click()
        self.driver.find_element_by_name("我的小说").click()

    def delete_book(self, topic):
        el1 = self.driver.find_element_by_name(self.aw.get_par_list(topic)[1])
        time = 2000  # 毫秒
        self.action.long_press(el1, time).wait(time).perform()
        self.driver.find_element_by_name("NB.BookShelf.Delete").click()
        self.driver.find_element_by_name("删除选中小说").click()


    def shelf_init(self, topic):
        self.deleteAll_books(0)
        #tst
        self.driver.find_element_by_name("孙子兵法").click()
        self.aw.click_mid(self.driver)

        try:
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_name("bookReader_setting")
        except Exception, ex:
            self.aw.click_mid(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("NB.Back.Boo.Shelf.Button").click()

    def check_bookshelf(self, topic):
        size_s = copy.deepcopy(device_info.device_screen_real)
        width_s = size_s[2]
        size_p1 = [0, 40, width_s, 210]  # 书架头部
        size_p2 = [0, 266, width_s, 660]
        check_title = self.aw.get_par_list(topic)[1]

        rate1 = picture.pic_operate(check_title + "_p1", self.aw.is_update_pic(self.aw.get_marker(topic)), size_p1,
                                    self.driver)
        rate2 = picture.pic_operate(check_title + "_p2", self.aw.is_update_pic(self.aw.get_marker(topic)), size_p2,
                                    self.driver)
        # 重试一次
        picture.is_reCompare = 1
        if rate1 < 99 or rate2 < 99:
            sleep(3)
            rate1 = picture.pic_operate(check_title + "_p1", self.aw.is_update_pic(self.aw.get_marker(topic)), size_p1,
                                        self.driver)
            rate2 = picture.pic_operate(check_title + "_p2", self.aw.is_update_pic(self.aw.get_marker(topic)), size_p2,
                                        self.driver)

        logger.info("相似度 p1: " + str(rate1) + " p2: " + str(rate2))
        picture.is_reCompare = 0
        if rate1 > 99 and rate2 > 99:
            logger.info(check_title + ": pass")
        else:
            #上报失败结果
            result.set_check_result(check_title)

    def reader_init(self, topic):
        self.deleteAll_books(0)
        self.driver.find_element_by_name("孙子兵法").click()
        self.aw.click_mid(self.driver)

        try:
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_name("NB.Chapter.Setting.ChapterSlider").send_keys("0.1")
        except Exception, ex:
            self.aw.click_mid(self.driver)
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_name("bookReader_setting").click()
        self.driver.find_element_by_name("bookReader_skin0").click()

        while self.driver.find_element_by_name("bookReaderFont_reduce").is_enabled() == True:
            self.driver.find_element_by_name("bookReaderFont_reduce").click()

        self.driver.find_element_by_name("NB.BottomBar.MoreSetting.Button").click()
        self.driver.find_element_by_name("NB.MoreSetting.Smooth").click()
        self.driver.find_element_by_name("NB.MoreSetting.PreReadOf10").click()
        el_back = self.driver.find_element_by_name("back")
        self.action.long_press(el_back, 100).perform()

        self.aw.click_mid(self.driver)

        self.driver.find_element_by_name("NB.Back.Boo.Shelf.Button").click()

        sleep(2)

    def deleteAll_books(self, n):
        el1 = self.driver.find_elements_by_xpath("//UIAButton[@name='服务声明']/../UIAElement")
        bookcount = el1.__len__()
        if bookcount > 2:
            self.driver.find_element_by_name("NB.BookShelf.Edit").click()

            for i in range(n, bookcount - 1):

                if "孙子兵法" != el1[i].get_attribute("name").encode('utf8'):
                    el1[i].click()
            self.driver.find_element_by_name("NB.BookShelf.Delete").click()
            self.driver.find_element_by_name("删除选中小说").click()
        else:
            print "书架中只有孙子兵法"
