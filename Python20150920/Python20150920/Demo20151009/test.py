# -*- coding:utf-8 -*-

'''
yangfs
2015-09-22
'''
#!/usr/bin/python
from svnCheckout.svnCheckout import *


# sys.path.insert(0, "/Library/Python/2.7/site-packages");

print("check out 工程代码：")

svnPath = "https://github.com/iphoneReadingme/SpriteKitCode20150830.git/trunk/03-Particles/step01"
svnUserName= "iosdev20150920@126.com"
svnPassword = "yang346854"
codeDir = "/Users/yangfs/Desktop/E/Src20150915/Src20151009/SvnDemo20151009/";
svnObject = SourceSvnCheckout(svnPath, svnUserName, svnPassword, codeDir)
v = svnObject.checkoutCode()

print(v);

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