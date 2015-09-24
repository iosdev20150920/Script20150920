# -*- coding:utf-8 -*-
'''
Created on 2014年10月10日

@author: liupeng3
'''
import path
import copy
import logging
import logging.config
from sc_action.libs import result, exe_status
from PIL import Image

import histsimilar

logger = logging.getLogger("log_NB")
PATH_PIC = path.PATH
similar_rate = "null"
is_reCompare = 0

def pic_operate(case_name, is_update, size, drive):
    name = case_name
    pic_drive = drive
    pic_size = copy.deepcopy(size)
    pic_expect_path = path.get_multi_platform(PATH_PIC + "/pic/expect/%s.png"%name)
    pic_fact_path = path.get_multi_platform(PATH_PIC + "/pic/fact/%s.png"%name)
    result_path = path.get_multi_platform(PATH_PIC + "/result/%s.png"%name)
    pic_size[2] = pic_size[2] + pic_size[0]
    pic_size[3] = pic_size[3] + pic_size[1]
    logger.info("截图起点坐标: " + str(pic_size[0]) + "," + str(pic_size[1]) + " 截图终点坐标: " + str(pic_size[2]) + "," + str(pic_size[3]))
    global similar_rate


    if is_update == "Y":
        pic_drive.get_screenshot_as_file(pic_expect_path)
        Image.open(pic_expect_path).crop(pic_size).save(pic_expect_path)

        similar_rate = 100
    elif is_update == "N":
        pic_drive.get_screenshot_as_file(pic_fact_path)
        Image.open(pic_fact_path).crop(pic_size).save(pic_fact_path)
        pic0 = Image.open(pic_expect_path)
        pic1 = Image.open(pic_fact_path)
        pic_joint(pic0, pic1).save(result_path)

        if is_reCompare == 0:

            #上报图片所属用例
            if result.case_pic.has_key(exe_status.exe_case_title):
                result.case_pic[exe_status.exe_case_title] += name + ".png" + "|"
            else:
                result.case_pic[exe_status.exe_case_title] = name + ".png" + "|"

        similar_rate = histsimilar.calc_similar_by_path(pic_fact_path,pic_expect_path)*100

    return similar_rate

def pic_joint(img0 , img1):
    x1 = img1.size[0]
    y1 = img1.size[1]

    box1 = (0, 0, x1, y1)
    box2 = (x1 + 10, 0, x1*2 + 10, y1)
    img = Image.new('RGBA', (x1*2 + 10, y1))
    img.paste(img0, box1)
    img.paste(img1, box2)
    return img
