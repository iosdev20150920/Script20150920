# -*- coding:utf-8 -*-

import paramiko
import path
import commands
from time import sleep
import os
import subprocess
# lp 5c

hostname = '127.0.0.1'
username = 'root'
password = 'alpine'
port = 2222

class FileSet():
    def __init__(self):
        #设置代理
        os.system("kill -9 $(ps ux | grep tcprelay.py | grep -v grep | awk {'print $2'})")
        command_str = 'python ' + path.PATH + '/sc_action/libs/sshCmd/tcprelay.py 22:2222&'
        os.system(command_str)
        sleep(3)
        #初始化连接
        paramiko.util.log_to_file('paramiko.log')
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname, port, username=username,password=password,timeout=5)
        self.sftp = self.client.open_sftp()
        #初始化路径
        stdin, stdout, stderr = self.client.exec_command('find /private/var/mobile/ -name sl_uc_param')
        file_path = stdout.read()[:-1]
        self.cd_path = file_path
        self.root_path = file_path.split("Library/Caches/Library", 25)[0]
        print self.root_path
        self.local_cd_path = path.PATH + '/conf/cd/sl_uc_param'
        self.local_setting_path = path.PATH + '/conf/Settings'
        self.setting_path = self.root_path + '''/Library/Profile/Settings'''


    def restore(self):
        self.rm_dir()

        files_setting = os.listdir(self.local_setting_path)
        
        for f in files_setting:
            self.sftp.put(os.path.join(self.local_setting_path, f), os.path.join(self.setting_path, f))
        stdin, stdout, stderr = self.client.exec_command('chmod -R 777 ' + self.setting_path)
        print stdout.read()[:-1]

    def download(self):

        files_setting = self.sftp.listdir(self.setting_path)
        for f in files_setting:
            self.sftp.get(os.path.join(self.setting_path, f), os.path.join(self.local_setting_path, f))

    def rm_dir(self):
        stdin, stdout, stderr = self.client.exec_command('rm -rf ' + self.setting_path + '/*')
        print stdout.read()[:-1]

    def cd_replace(self):

        local_path = self.local_cd_path
        print local_path
        remote_path = self.cd_path
        print remote_path

        self.replace(local_path, remote_path) #cd参数初始化
        self.replace(path.PATH + '/conf/cd/Bookmarks', self.root_path + '/Documents/Profile/Bookmarks') #书签初始化
        # self.sftp.put(local_path, remote_path)
        # stdin, stdout, stderr = self.client.exec_command('chown -R mobile ' + self.cd_path)
        # print stdout.read()[:-1]

    def replace(self, local_path, remote_path):

        local_path = local_path
        remote_path = remote_path
        self.sftp.put(local_path, remote_path)
        stdin, stdout, stderr = self.client.exec_command('chown -R mobile ' + remote_path)
        print stdout.read()[:-1]

    def close(self):
        self.client.close()

# replace(f_path = "/Users/liupeng3/SVN/x_test/autotest/x_test/conf/cd/sl_uc_param")
# fs = FileSet()
# fs.restore()
# fs.close()