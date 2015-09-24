# -*- coding:utf-8 -*-
##########################################################################
# Copyright (C) 2005-2013 UC Mobile Limited. All Rights Reserved
# File          : common
# 
# Creation      : 2013年10月31日
# Author        : zengchen@ucweb.com
###########################################################################
import os
import sys
import paramiko
import subprocess
import pwd
import tcprelay
import select

class Common(object):
    def __init__(self):
        pass
    def killProcess(self,process_name):
        '''结束进程.
        Args:
            process_name：需结束的进程名称
        Returns:无
        '''
        cmd="ps ux|grep "+process_name+"|grep -v grep"
        popen = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
        out = popen.communicate()
        if len(out)>0:
            if len(out[0].split())>1:
                pid=out[0].split()[1]
                os.kill(int(pid),9)
                
    def getDevID(self):
        '''获取设备udid.
        Args:无
        Returns:无
        '''
        all_devid = os.popen('system_profiler SPUSBDataType | grep "Serial Number:.*" | sed s#".*Serial Number: "##').readlines()
        devid = ''
        i = 0;
        while (i < len(all_devid)):
            if len(all_devid[i]) >= 40:
                devid = all_devid[i].replace("\n", '')
                break;
            i += 1;
        return devid
     
    def localExcCMD(self,cmd):
        '''执行本地命令.
        Args:
            cmd：命令行
        Returns:
            handle：执行结果
        '''
        handle = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
        return handle
    
    def getIpAddress(self):
        '''获取本机ip.
        Args:无
        Returns:
            addr：本机ip地址
        '''
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(('8.8.8.8', 80))
        (addr, port) = csock.getsockname
        csock.close()
        return addr
        
if __name__=="__main__":
    comm = Common()
    print(comm.getDevID())