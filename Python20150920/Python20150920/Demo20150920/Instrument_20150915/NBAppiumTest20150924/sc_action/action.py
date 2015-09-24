#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

根据函数名称动态调用
"""
import os
import sys
from sc_action import action_word
from xmind.core.topic import TopicElement
import xmind


class Action():

    def action_do(self, driver, topic):
        exe_name = topic.getTitle().split(":", 5)[0]
        if exe_name.split(".", 3).__len__() == 2:
            class_name = exe_name.split(".", 3)[0]
            func_name = exe_name.split(".", 3)[1]
            module = __import__(name='sc_action.cous_aw.' + class_name, fromlist=[class_name])
            parser = getattr(module, class_name)(driver)
            getattr(parser, func_name)(topic)
        else:
            aw = action_word.ActionWord(driver)
            getattr(aw, topic.getTitle().split(":", 5)[0])(topic)


if __name__ == '__main__':
    print "--"
    # main()