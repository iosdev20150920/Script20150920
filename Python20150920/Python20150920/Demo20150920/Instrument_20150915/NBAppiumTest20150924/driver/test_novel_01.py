# -*- coding:utf-8 -*-
'''
Created on 2014年7月30日

@author: jiangyg
'''
import os
import unittest
import random
import string

from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from  sc_action import const

# def str_generator(size = 6, chars = string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))

class DemoTest(unittest.TestCase):
    '''
    发布性测试用例集 中文，
    '''
    def setUp(self):

        self.driver = webdriver.Remote(
            command_executor = const.file_map["command_executor"],
            desired_capabilities = const.file_map["desired_capabilities"])

      
    def tearDown(self):
        pass
    

        
    def test_novel_01(self):
        try:

            self.driver.implicitly_wait(5)
            act = TouchAction(self.driver)




            self.driver.find_elements_by_name("Windows")[-1].click()
            self.driver.find_elements_by_name("urlInputField")[1].send_keys(u"孙子兵法")
            el001 = self.driver.find_elements_by_name("urlInputField")
            act.long_press(el001[0], 100).perform()
            act.long_press(el001[0], 100).perform()
            self.driver.find_element_by_name("前往").click()
            self.driver.hide_keyboard(u"前往")
            self.driver.find_elements_by_name("urlInputField")[1].click()
            self.driver.find_elements_by_name("urlInputField")[0].click()
            self.driver.find_elements_by_name("urlInputField")[1].click()
            self.driver.hide_keyboard()



            self.driver.find_element_by_name("Menu1")
            self.driver.find_elements_by_name("我的小说")[0].click()
            test1 = self.driver.find_elements_by_name("NB.BookShelf.SearchField")

            act.long_press(test1[0], 100).perform()
            sleep(3)
            self.driver.find_elements_by_name("NB.BookShelf.SearchField")[1].set_value("孙子兵法")

            print self.driver.find_elements_by_name("百度搜索").__len__()
            print self.driver.find_elements_by_name("淘宝热卖").__len__()
            self.driver.find_element_by_name("RightEditButton").click()

            e1 = self.driver.find_elements_by_name("百度搜索")
            e2 = self.driver.find_elements_by_name("淘宝热卖")
            print self.driver.find_elements_by_name("百度搜索")[0].tag_name
            move_x = e1.size["width"]*0.9
            move_y = e1.location["y"] + e1.size["height"]*0.5
            print move_x
            print move_y
            to_x = e2.size["width"]*0.9
            to_y = e2.location["y"] + e1.size["height"]*0.5
            print to_x
            print to_y

            act.long_press(x=move_x, y=move_y).wait(2000).move_to(x=0, y=(to_y - move_y)).release().perform()


            print "test pass"





            self.driver.find_element_by_name("我的小说").click()
            el0 = self.driver.find_element_by_name("斗罗大陆II绝世唐门")
            el0.click()
            act.press(x=160, y=284).perform()
            self.driver.find_element_by_name("bookReader_setting").click()
            act.press(x=80, y=57).wait(2000).perform()






            # act.long_press(el=el0, duration=3000).wait(3000).perform()


            print "222"
            el1 = self.driver.find_element_by_name("男生热搜")
            el0 = self.driver.find_element_by_name("男生热搜1")
            act = TouchAction(self.driver)
            act.long_press(el0).move_to(el1).release()

            sleep(3)
            self.driver.find_element_by_name("NB.BookShelf.SearchField").click()
            self.driver.find_element_by_name("NB.BookShelf.SearchField").set_value("绝世唐门")
            self.driver.find_element_by_name("绝世唐门")
            self.driver.hide_keyboard()


        except Exception,ex:
            print("test001 failed :%s"%ex)


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(DemoTest)
    unittest.TextTestRunner(verbosity = 2).run(suite)