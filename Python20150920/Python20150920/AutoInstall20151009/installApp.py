#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2013-11-26

@author: yangfs

'''
import os

# from common import Common


#from dbgp.client import brk


def getUUID():
    "获取设备UUID"

    udid = os.popen('''system_profiler SPUSBDataType | grep "Serial Number:.*" | sed s#".*Serial Number: "## ''').readlines()
    if len(udid)>1:
        for item in udid:
            if len(item) < 20:
                udid.remove(item)
            else:
                break

    if len(udid)>0:
        udid = udid[0].replace('\n','')
    
    return udid

def installApp():
    "安装应用程序"

    '''获取 home路径'''
    homePath = os.path.expanduser("~");
    print("homePath = %s"%(homePath))
    path = homePath + "/Desktop/B/Backup20150529/20150810_ios/trunk_Src20150920/Script20150920/Python20150920/Python20150920/AutoInstall20151009"
    os.system("cd %s"%(path))

    '''指定目录'''
    os.chdir(path)
    os.system("ls")
    
    devid = "c5aeecc8150b073d013635727f0bee87c09344f3"
    # 设备UUID
    devid = getUUID()
    print("devid = %s"%(devid))
    appPath = "./SpaceRun.app"
    cmdText = "./fruitstrap -d -b " + appPath + " -i " + devid
    print(cmdText)
    os.system(cmdText)
    
if  __name__ == '__main__':
    
    # test2()
    installApp()
