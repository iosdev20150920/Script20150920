# -*- coding:utf-8 -*-
from Tkinter import *
import os
import tkMessageBox
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

if __name__ == '__main__':
    # app = Application()
    # # 设置窗口标题:
    # app.master.title('Hello World')
    # # 主消息循环:
    # app.mainloop()
    #os.system("kill -9 $(ps ux | grep node | grep -v grep | awk {'print $2'})")
    # appium_cmd = 'nohup /Applications/Appium.app/Contents/Resources/node/bin/node /Applications/Appium.app/Contents/Resources/node_modules/appium/lib/server/main.js --command-timeout "7200" --platform-version "8.1" --platform-name "iOS" --app "com.ucweb.iphone" --udid "8223f1cf73820d03d4dfc4ff647917bda3e34e80" --show-ios-log --default-device &'
    appium_cmd = 'nohup /Applications/Appium.app/Contents/Resources/node/bin/node /Applications/Appium.app/Contents/Resources/node_modules/appium/lib/server/main.js --command-timeout "7200" --platform-version "8.1" --platform-name "iOS" --app "com.ucbrowser.iphone.cn" --udid "8223f1cf73820d03d4dfc4ff647917bda3e34e80" --show-ios-log --default-device &'

    print('cmd:'+appium_cmd)
    v = os.system(appium_cmd)
    print v