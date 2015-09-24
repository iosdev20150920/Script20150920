# -*- coding: utf-8 -*-
import json
import path
# import logging
# import logging.config
# logging.config.fileConfig("log.conf")
# logger = logging.getLogger("log_NB")


#10.1.88.101
PATH = path.PATH
# file = PATH.replace('/',"\\") + r'\setting.txt'
file = path.get_multi_platform(PATH + r'/conf/setting.txt')
print file
f = open(file)
str = f.read()

file_map = json.loads(str)

if __name__ == '__main__':
    # logger.info("click log")

    print ""
    print ""