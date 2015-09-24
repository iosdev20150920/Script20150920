# -*- coding:utf-8 -*-

import os
import sys

isWindows = 0

def cur_file_dir():
    #获取脚本路径或打包后的执行路径
    if getattr(sys, 'frozen', False):
        path = os.path.dirname(sys.executable)
    elif __file__:
        path = os.path.dirname(__file__)
    return path


def get_multi_platform(path):
    """
    @type path:str
    """
    multi_path = path
    if isWindows == 1:
        multi_path = multi_path.replace('/', '\\')
    return multi_path
PATH = cur_file_dir()
arg_path = None