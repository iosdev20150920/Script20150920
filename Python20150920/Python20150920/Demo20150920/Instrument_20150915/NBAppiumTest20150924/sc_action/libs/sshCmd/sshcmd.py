# -*- coding:utf-8 -*-

import os
import sys
import paramiko
import subprocess
import time

class SSHCmd(object):
    def __init__(self,host,port=2222,user_name='uc',pass_word='uctest'):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(host,port,username=user_name,password=pass_word,timeout=5)
        self.sftp = self.client.open_sftp()

    def sshGetAppPath(self,app_name):
        '''获取应用程序文件路径.
        Args:
            app_name：应用程序名称
        Returns:
            app_path：应用程序路径
        '''
        app_path = ''
        stdin, stdout, stderr = self.client.exec_command('ls /User/Applications')
        for std in stdout.readlines():
            stdin1, stdout1, stderr1 = self.client.exec_command('ls /User/Applications/'+std.replace('\n',''))
            for std1 in stdout1.readlines():
                if std1.find(app_name) == -1:
                    pass
                else:
                    app_path = '/User/Applications/'+std.replace('\n','')
        return app_path
        
    def sshChmod(self,file_path):
        '''文件夹授权
        Args:
            file_path：需授权文件夹路径
        Returns:
            无
        '''
        stdin,stdout,stderr = self.client.exec_command('chmod -R 777 '+file_path)
       
    def sshRemove(self,file_path):
        '''删除文件
        Args:
            file_path：文件路径
        Returns:
            无
        '''
        stdin,stdout,stderr = self.client.exec_command('rm -rf '+file_path)
    
    def sshPut(self,local_path,remote_path):
        '''从本地上传文件到手机端
        Args:
            local_path：本地文件路径
            remote_path：手机文件路径
        Returns:
            无
        '''
        self.sftp.put(local_path,remote_path)
        
    def sshGet(self,local_path,remote_path):
        '''从手机端获取文件到本地
        Args:
            local_path：本地文件路径
            remote_path：手机文件路径
        Returns:
            无
        '''
        self.sftp.get(remote_path,local_path)
        
    def __del__(self):
        self.client.close()

if __name__ == "__main__":
    comm = SSHCmd('127.0.0.1',2222,'root','uctest')
    print comm.sshGetAppPath("sl_uc_param")