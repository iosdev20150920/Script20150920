# -*- coding:utf-8 -*-

'''
yangfs
2015-10-09
'''
#!/usr/bin/python
import os

class SourceSvnCheckout:
	"check out 工程代码 类"

	def __init__(self, svnPath="", svnUserName="", svnPassword="", codeDir=""):
		self.svnPath = svnPath
		self.svnUserName= svnUserName
		self.svnPassword = svnPassword
		self.codeDir = codeDir;

		self.buildSucced = False
		self.buildErrorDescription = []
		
	def checkoutCode(self):
		"下载代码的方法"

		print("svn Checkout source start:")

		codeDir = self.codeDir
		svnInfo = "%s --username %s -- password %s"%(self.svnPath, self.svnUserName, self.svnPassword)
		os.system('rm -frd %s '%codeDir);
		os.system('mkdir %s'%codeDir);

		svnCmd = 'svn checkout %s -- no-interactive %s'%(svnInfo, codeDir)
		os.system(svnCmd);
		print("svn语句：%s"%(svnCmd))

		retValue = False;
		msg = 'checkOut code failed'
		if os.path.exists('%sYourProjectName'%codeDir) == False:
			msg = 'checkOut code failed'
			print(msg)
			self.buildSucced = False
			self.buildErrorDescription.append(msg)
		else:
			msg = 'checkOut code success!'
			# os.chdir(LifeSearchBuild.codeDir)
			retValue = True

		return msg


