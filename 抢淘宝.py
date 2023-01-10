#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:20:24 2022

@author: gaobikai
"""
import platform
import os
from selenium import webdriver
import datetime
import time
from selenium.webdriver.chrome import service as fs
 




def buy(chrome, store, buy_time):
    # 淘宝
    if store == '1':
        # "立即购买"的css_selector
        btn_buy = '#J_juValid > div.tb-btn-buy > a'
        # "立即下单"的css_selector
        btn_order = '#submitOrderPC_1 > div.wrapper > a'
        print("淘宝")
    # 天猫
    elif store == '2':
        btn_buy = '#J_LinkBuy'
        btn_order = '#submitOrderPC_1 > div > a'
        print("天猫")
    # 天猫超市
    elif store == '3':
        btn_buy = '#J_Go'
        btn_order = '#submitOrderPC_1 > div > a.go-btn'
        print("天猫商城")

    while True:
        # 现在时间大于预设时间则开售抢购
        # print("开始抢购")
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > buy_time:
            print("开始抢购")
            try:
                # 找到"立即购买" 点击
                if chrome.find_element("css selector", btn_buy):
                    print("点击购买")
                    chrome.find_element("css selector", btn_buy).click()
                    break
                time.sleep(0.1)
            except:
                time.sleep(0.3)

    while True:
        try:
            # 找到"立即下单" 点击
            if chrome.find_element("css selector", btn_order):
            # chrome.find_element_by_css_selector(btn_order):
                chrome.find_element("css selector", btn_order).click()
                # 下单成功，跳转至支付页面
                print('购买成功')
                break
        except:
            time.sleep(0.5)


#address for the chromedriver
CHROMEDRIVER = "...../chromedriver"

chrome_service = fs.Service(executable_path=CHROMEDRIVER)



driver = webdriver.Chrome(service=chrome_service)
driver.get('.....address for the taobao/ tianmao url link')

driver.maximize_window()
store = '2'
buy_time = 'set the time in the form of (2022-11-20 11:00:00)'
print('请手动登录（务必在抢购时间前完成）')
buy(driver, store, buy_time)
    
  


    
    
    
    
    