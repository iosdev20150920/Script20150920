# -*- coding:utf-8 -*-

'''
yangfs
2015-09-22
'''
#!/usr/bin/python

import os
from svnCheckout.svnCheckout import *


# sys.path.insert(0, "/Library/Python/2.7/site-packages");

print("check out 工程代码：")

svnPath = "https://github.com/iosdev20150920/DemoCode20151010/trunk/step01"
svnUserName= "***@126.com"
svnPassword = "***"

'''获取 home路径'''
homePath = os.path.expanduser("~");
print("homePath = %s"%(homePath))

codeDir = homePath + "/Desktop/E/Src20150915/Src20151009/SvnDemo20151009/";
svnObject = SourceSvnCheckout(svnPath, svnUserName, svnPassword, codeDir)
v = svnObject.checkoutCode()

print(v);


