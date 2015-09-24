# -*- coding:utf-8 -*-
import action

device_type = "iphone5"
device_scaling = 2          #缩放比
device_screen = [0, 0, 320, 568]
device_screen_real = [0, 0, 640, 1136]

def set_device_type():
    global device_type
    device_type = "iphone5"

def set_device_scaling():
    global device_scaling
    device_scaling = 2

def set_device_screen(driver):
    size = driver.find_element_by_xpath('//UIAApplication[1]').size
    global device_screen
    device_screen = [0,0,size['width'], size['height'] + 20]
    print device_screen
    set_device_screen_real(device_screen)
    #device_screen = [0,0,size['width'],size['height']+10]

def set_device_screen_real(device_screen):
    global device_scaling, device_screen_real
    device_screen_real = [device_screen[0]*device_scaling, device_screen[1]*device_scaling, device_screen[2]*device_scaling, device_screen[3]*device_scaling]