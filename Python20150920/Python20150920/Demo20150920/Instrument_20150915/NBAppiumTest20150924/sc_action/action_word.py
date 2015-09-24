# -*- coding:utf-8 -*-
from time import sleep
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.touch_action import TouchAction
from sc_action import picture
from sc_action import device_info
from sc_action.libs.result import case_res
from sc_action.libs import result
import copy
import string
import logging
import logging.config
logger = logging.getLogger("log_NB")
class ActionWord():

    def __init__(self, driver):
        """
        @type driver:WebDriver
        """
        self.driver = driver
        self.action = TouchAction(self.driver)

    def click(self, topic):
        el1 = self.driver.find_element_by_name(self.get_par_list(topic)[1])
        if self.get_par_list(topic).__len__() == 2:
            count = 1
        else:
            count = int(self.get_par_list(topic)[2])
        for i in range(0, count):
            if el1.is_displayed() == False:
                self.action.long_press(el1, 100).perform()
            else:
                self.driver.find_element_by_name(self.get_par_list(topic)[1]).click()

    def long_press(self, topic):
        """
        长按 eg: topic = long_press:ele_name:2   长按ele_name控件 2秒
        """
        el1 = self.driver.find_element_by_name(self.get_par_list(topic)[1])
        time = int(self.get_par_list(topic)[2])*1000     #秒
        self.action.long_press(el1, time).wait(time).perform()

    def move_to(self, topic):
        """
        长按一个控件拖至另一个控件位置(包括TableCell控件)
        eg: topic = move_to:ele_1:ele_2    长按ele_1然后移动至ele_2
        """
        el0 = self.driver.find_elements_by_name(self.get_par_list(topic)[1])[0]
        if el0.tag_name != "UIATableCell":
            el1 = self.driver.find_elements_by_name(self.get_par_list(topic)[2])[0]
            self.action.long_press(el0).wait(2000).move_to(el1).release().perform()
        else:
            self.cell_move(topic)

    def cell_move(self, topic):
        el0 = self.driver.find_elements_by_name(self.get_par_list(topic)[1])[0]
        el1 = self.driver.find_elements_by_name(self.get_par_list(topic)[2])[0]
        move_x = el0.size["width"]*0.9
        move_y = el0.location["y"] + el0.size["height"]*0.5
        to_x = el1.size["width"]*0.9
        to_y = el1.location["y"] + el1.size["height"]*0.5

        self.action.long_press(x=move_x, y=move_y).wait(2000).move_to(x=0, y=(to_y - move_y)).release().perform()

    def cell_swipe(self, topic):
        el0 = self.driver.find_elements_by_name(self.get_par_list(topic)[1])[0]

        start_x = el0.size["width"]*0.7
        start_y = el0.location["y"] + el0.size["height"]*0.5
        end_x = el0.size["width"]*0.2
        end_y = start_y
        self.driver.swipe(start_x, start_y, end_x, end_y)


    def cell_del(self, topic):
        cell_name = self.get_par_list(topic)[1]
        del_lable = '''确认“''' + cell_name.encode('utf-8') + '''”上的删除'''
        try:
            self.driver.find_element_by_name("删除").click()
        except Exception,ex:
            #兼容6.x
            self.driver.find_element_by_name(del_lable).click()


    def swipe(self, topic):
        local = self.get_par_list(topic)[1].split(",", 5)
        start_x = string.atof(local[0])*device_info.device_screen[2]
        start_y = string.atof(local[1])*device_info.device_screen[3]
        end_x = string.atof(local[2])*device_info.device_screen[2]
        end_y = string.atof(local[3])*device_info.device_screen[3]
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def swipe2(self, topic):
        local = self.get_par_list(topic)[1].split(",", 5)
        start_x = local[0]
        start_y = local[1]
        end_x = local[2]
        end_y = local[3]
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def delete_windows(self, topic=None):
        local = device_info.device_screen
        self.driver.find_elements_by_name("Windows")[-1].click()
        sleep(2)
        self.action.press(x=local[2]*0.5, y=int(local[3]*0.5)).wait(2000).perform()
        self.driver.swipe(local[2]*0.5, int(local[3]*0.5), local[2]*1, int(local[3]*0.5), 1000)

    def reset(self, topic):
        self.driver.reset()

    def double_click(self, topic):
        el1 = self.driver.find_element_by_name(self.get_par_list(topic)[1])
        count = int(self.get_par_list(topic)[2])     #点击次数
        self.action.tap(el1,el1.size["width"]*0.5,el1.size["height"]*0.5, count).perform()

    def input(self, topic):
        self.driver.find_element_by_name(self.get_par_list(topic)[1]).set_value(self.get_par_list(topic)[2])

    def module(self, topic):
        print "module"

    def S(self, topic):
        if result.failed_path.has_key(self.get_par_list(topic)[1]):
            logger.info("scene failed:" + self.get_par_list(topic)[1])
        else:

            logger.info("scene pass:" + self.get_par_list(topic)[1])

    def click_web(self, topic):
        self.driver.find_element_by_xpath('//*[@name="' + self.get_par_list(topic)[1] + '"]').click()

    def click_m(self, topic):
        local = device_info.device_screen
        if self.get_par_list(topic).__len__() == 1:
            count = 1
        else:
            count = int(self.get_par_list(topic)[1])
        for i in range(0, count):
            self.driver.tap([(local[2]*0.5, local[3]*0.5)])

    def slider(self, topic):
        """
        操作滑块
        eg: topic = slider:element_name:1 将name为element_name的滑块拖至100%比例的位置
        """
        value = self.get_par_list(topic)[2]
        self.driver.find_element_by_name(self.get_par_list(topic)[1]).send_keys(value)

    def click_u(self, topic):
        local = device_info.device_screen
        if self.get_par_list(topic).__len__() == 1:
            count = 1
        else:
            count = int(self.get_par_list(topic)[1])
        for i in range(0, count):
            self.action.press(x=local[2]*0.5, y=int(local[3]*0.2)).wait(2000).perform()

    def click_d(self, topic):
        local = device_info.device_screen
        if self.get_par_list(topic).__len__() == 1:
            count = 1
        else:
            count = int(self.get_par_list(topic)[1])
        for i in range(0, count):
            self.driver.tap([(local[2]*0.5, local[3]*0.8)])

    def click_l(self, topic):
        local = device_info.device_screen
        if self.get_par_list(topic).__len__() == 1:
            count = 1
        else:
            count = int(self.get_par_list(topic)[1])
        for i in range(0, count):
            self.driver.tap([(local[2]*0.1, local[3]*0.5)])

    def click_r(self, topic):
        local = device_info.device_screen
        if self.get_par_list(topic).__len__() == 1:
            count = 1
        else:
            count = int(self.get_par_list(topic)[1])
        for i in range(0, count):
            self.driver.tap([(local[2]*0.9, local[3]*0.5)])


    def click_v(self,topic):
        """
        视频：视频播放器唤起上下操作栏，点击控件
        """
        for i in range(0,5):
            try:
                video_ele = self.driver.find_element_by_name(self.get_par_list(topic)[1])
                video_ele.click()
                break
            except Exception,vx:
                local = device_info.device_screen
                self.driver.execute_script('''target.touch([{"touch":[{"x":'''+str(local[2]*0.5*0.5)+''',"y":'''+str(local[3]*0.5*0.25)+'''}],"time":0.2}])''')

    def wait(self, topic):
        time = int(self.get_par_list(topic)[1])
        sleep(time)

    def search(self, topic):
        urlInputField = self.driver.find_elements_by_name("urlInputField")
        urlInputField[0].click()

        urlInputField = self.driver.find_elements_by_name("urlInputField")
        strings = self.get_urlpar_list(topic)[1]
        urlInputField[1].send_keys(strings)

        if len(self.driver.find_elements_by_name("确认")) > 0:
            self.driver.find_element_by_name("确认").click()
        self.driver.find_element_by_name("前往").click()

    def search_word(self, topic):
        urlInputField = self.driver.find_elements_by_name("urlInputField")
        urlInputField[0].click()

        urlInputField = self.driver.find_elements_by_name("urlInputField")
        strings = self.get_par_list(topic)[1]
        urlInputField[1].send_keys(strings)

        if len(self.driver.find_elements_by_name("确认")) > 0:
            self.driver.find_element_by_name("确认").click()
        self.driver.find_element_by_name("前往").click()

    def check(self, topic):
        """
        图片校验
        eg1: topic = check:TC_001 按默认比例截图对比
        eg2: topic = check:0,0,0.5,1:TC_002 按起点坐标比例 0,0 终点坐标比例 0.5,1截图对比
        eg3: eg2: topic = check:element_name:TC_002 截取name为element_name的控件截图
        """
        size = []
        case_title = ""
        if self.get_par_list(topic).__len__() == 2:
            #默认截图
            size = copy.deepcopy(device_info.device_screen_real)
            size[1] = size[3]*40/1136
            size[3] = size[3] - (size[1]*2)
            case_title = self.get_par_list(topic)[1]
        elif self.get_par_list(topic).__len__() == 3:
            #ele截图 或 比例截图
            case_title = self.get_par_list(topic)[2]
            if self.get_par_list(topic)[1].split(",", 5).__len__() == 4:
                scale = copy.deepcopy(self.get_par_list(topic)[1].split(",", 5))
                size = copy.deepcopy(device_info.device_screen_real)
                size[0] = int(size[2]*string.atof(scale[0]))
                size[1] = int(size[3]*string.atof(scale[1]))
                size[2] = int(size[2]*string.atof(scale[2])) - size[0]
                size[3] = int(size[3]*string.atof(scale[3])) - size[1]
            else:
                el1 = self.driver.find_element_by_name(self.get_par_list(topic)[1])
                size.append(el1.location["x"]*device_info.device_scaling)
                size.append(el1.location["y"]*device_info.device_scaling)
                size.append(el1.size["width"]*device_info.device_scaling)
                size.append(el1.size["height"]*device_info.device_scaling)
        rate = picture.pic_operate(case_title, self.is_update_pic(self.get_marker(topic)), size, self.driver)
        #重试一次
        #上报重试
        picture.is_reCompare = 1
        if rate < 99:
            sleep(3)
            rate = picture.pic_operate(case_title, self.is_update_pic(self.get_marker(topic)), size, self.driver)
        print rate
        logger.info("相似度: " + str(rate))
        picture.is_reCompare = 0
        if rate > 99:
            logger.info(case_title + " check pass")
        else:
            result.set_check_result(case_title)


    def check_ele(self, topic):
        """
        校验控件是否存在
        eg: topic = check_ele:element_name:TC_003  检查是否存在name为element_name的控件
        """
        self.driver.implicitly_wait(5)
        check_title = self.get_par_list(topic)[2]
        try:
            self.driver.find_element_by_name(self.get_par_list(topic)[1])
        except Exception,ex:
            result.set_check_result(check_title)

    @staticmethod
    def get_par_list(topic):

        par_list = topic.getTitle().split(":", 5)
        return par_list

    @staticmethod
    def get_urlpar_list(topic):

        par_list = topic.getTitle().split("@")
        return par_list

    @staticmethod
    def get_marker(topic):

        try:
            marker = topic.getMarkers()[0].getMarkerId().name
        except Exception,ex:
            marker = "None"
            print "no Marker"

        return marker

    @staticmethod
    def is_update_pic(marker):

        if marker == "flag-yellow":
            pic = "Y"
        else:
            pic = "N"

        return pic

    @staticmethod
    def click_mid(driver):
        local = device_info.device_screen
        driver.tap([(local[2]*0.5, local[3]*0.5)])

if __name__ == '__main__':
    print "test"
