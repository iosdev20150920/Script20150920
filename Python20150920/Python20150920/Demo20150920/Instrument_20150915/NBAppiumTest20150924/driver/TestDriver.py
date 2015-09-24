#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-


import sys
import os
# sys.path.append("/Users/liupeng3/Desktop/autotest/x_test")
sys.path.append("/Users/uc/buildbot/scripts/qmsinterceptor/uc_iosnovelui/novel_ui")
import path
from appium import webdriver
from sc_action import const
from sc_action import test_case
from sc_action.libs.result import case_res
from sc_action import action
from sc_action.action_word import ActionWord
from time import sleep
from sc_action.libs import mail
from sc_action import device_info
import logging
import logging.config
from sc_action.libs import result, exe_status, file_operate, file_init

class Driver():

    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor = const.file_map["command_executor"],
            desired_capabilities = const.file_map["desired_capabilities"])
        self.fs = file_init.FileSet()

    def set_up(self):
        self.driver.implicitly_wait(10)
        device_info.set_device_screen(self.driver)

        file_operate.removeFileInFirstDir(path.PATH + '/result')
        file_operate.removeFileInFirstDir(path.PATH + '/pic/fact')
        # file_operate.removeFileInFirstDir(path.PATH + '/conf/NovelBox')
        # file_operate.removeFileInFirstDir(path.PATH + '/conf/Settings')

        #初始化cd参数
        self.fs.cd_replace()
        #获取初始化设置文件(小说，浏览器)
        # fs.download()

        self.driver.reset()

    def tear_down(self):
        self.driver.quit()

    def log_init(self):
        log_file = path.get_multi_platform(path.PATH + r'/conf/log.conf')
        logging.config.fileConfig(log_file)
        logger = logging.getLogger("log_NB")
        return logger

    def test_act(self, file_path = None, ui_case = None):
        #ui_case=0 时用例为release.xmind，为1时用例为test.xmind
        logger = self.log_init()

        case = test_case.Tcase(ui_case=int(ui_case))
        ac = action.Action()

        for i in range(1, case.caseCount + 1):
            try:
                marker = case.getCaseList(i)[0].getMarkers()[0].getMarkerId().name
            except Exception,ex:
                marker = "None"
                logger.info("no Marker")
            #上报当前执行用例名
            exe_status.exe_case_title = ActionWord.get_par_list(case.getCaseList(i)[0])[1]

            if marker != "flag-red":
                #初始化setting
                self.fs.restore()
                self.driver.reset()
                #上报用例目的
                if case.getCaseList(i)[0].getNotes() == None:
                    print "无测试备注"
                else:
                    result.case_purpose[exe_status.exe_case_title] = case.getCaseList(i)[0].getNotes().getContent()

                for p in case.getCaseList(i)[::-1]:
                    try:
                        exe_status.exe_path += p.getTitle() + " -> "
                        logger.info(p.getTitle())
                        ac.action_do(self.driver, p)
                        #上报结果
                        result.set_pass_result(exe_status.exe_case_title)
                    except Exception,ex:
                        info=sys.exc_info()
                        err_str = p.getTitle() + ": " + str(info[1])
                        logger.error(msg=err_str)
                        #上报错误
                        result.set_check_result(exe_status.exe_path)
                        break
                exe_status.exe_path = ""
                sleep(2)
                # if i < case.caseCount:
                #     self.driver.reset()
            elif marker == "flag-red":
                logger.info(case.getCaseList(i)[0].getTitle() + " pass")
            else:
                print "test"
        self.fs.close()
        result.res_save(case_res)
        if sys.argv.__len__() > 1:
            file_operate.copyFiles(path.PATH + '/result', sys.argv[1])
        if file_path is not None:
            file_operate.copyFiles(path.PATH + '/result', file_path)
        # mail.send_result(case_res)


if __name__ == '__main__':
    td = Driver()
    td.set_up()
    td.test_act(ui_case = '0')
    td.tear_down()