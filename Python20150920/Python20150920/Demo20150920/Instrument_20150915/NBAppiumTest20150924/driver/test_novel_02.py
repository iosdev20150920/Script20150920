# -*- coding:utf-8 -*-
'''
Created on 2014年7月30日

@author: jiangyg
'''
import os
import unittest
import random
import string
import inspect
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from  sc_action import const


from sc_action import test_case,action_word
from sc_action import action


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
def str_generator(size = 6, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class DemoTest(unittest.TestCase):
    '''
    发布性测试用例集
    '''

    def setUp(self):
        pass

        self.driver = webdriver.Remote(
            command_executor = const.file_map["command_executor"],
            desired_capabilities = const.file_map["desired_capabilities_samilor"])

      
    def tearDown(self):
        pass
        # self.driver.quit()

        
    def test_novel_01(self):
        # try:


        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_name("t")._execute()
        # sleep(10)
        # print picture.pic_operate(inspect.stack()[1][3],self.driver)
        case = test_case.Tcase()
        ac = action.Action(self.driver)


        for i in (1,case.caseCount):

            for p in case.getCaseList(i)[::-1]:
                print p.getTitle()
                ac.action_do(p)

            self.driver.reset()




        # self.driver.find_element_by_name("testlable").click();



        # except Exception,ex:
        #     print("test001 failed :%s"%ex)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DemoTest)
    unittest.TextTestRunner(verbosity = 2).run(suite)