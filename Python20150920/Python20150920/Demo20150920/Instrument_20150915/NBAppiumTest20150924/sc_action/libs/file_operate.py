# -*- coding:utf-8 -*-
import os
import os.path
import shutil
import time, datetime

def copyFiles(sourceDir,  targetDir):
    '''
    把某一目录下的所有文件复制到指定目录中
    '''
    if sourceDir.find(".svn") > 0:
        return
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(sourceFile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                    open(targetFile, "wb").write(open(sourceFile, "rb").read())
        if os.path.isdir(sourceFile):
            First_Directory = False
            copyFiles(sourceFile, targetFile)


def removeFileInFirstDir(targetDir):
    """
    删除一级目录下的所有文件
    """
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)

    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(targetFile):
            os.remove(targetFile)