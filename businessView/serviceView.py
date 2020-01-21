# -*- coding:utf-8 -*-
import logging
from common.common_fun import common, NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from businessView.registerView import registerView
from businessView.loginView import loginView
from businessView.bindhouseView import bindhouseView
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
import traceback
import time
import os



class serviceView(common):

    service_tag=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.widget.ImageView')
    cleantag=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[5]')
    stop_tag=(By.XPATH,'//android.widget.TextView[@text="宁波市三个阿姨信息科技有限公司 "]')
    select=(By.XPATH,'//android.widget.TextView[@text="筛选"]')
    textviewclass=(By.CLASS_NAME,'android.widget.TextView')
    last_tag = (By.XPATH, '//android.widget.TextView[@text="宁波海曙全能家电维修部 "]')
    homelectronics = (By.XPATH, '//android.widget.TextView[@text="家电清洗"]')
    Hightech= (By.XPATH, '//android.widget.TextView[@text="高新区"]')
    confirm = (By.XPATH, '//android.widget.TextView[@text="确定"]')
    searchinput = (By.XPATH, '//android.widget.EditText[@text="输入商家名称进行查询"]')
    searchinput2= (By.XPATH, '//android.widget.EditText[@text="新增商家"]')
    store1 = (By.XPATH, '//android.widget.TextView[@text="新增商家1111 "]')
    store2 = (By.XPATH, '//android.widget.TextView[@text="新增商家1010 "]')
    fistpage=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView')



    def search_store_action(self):
        logging.info('===============search_store_action================')
        self.click(*self.service_tag)
        s=self.get_size()
        x1=int(0.9*s[0])
        y1=int(0.2*s[1])
        x2=int(0.1*s[0])
        self.swipe(x1,y1,x2,y1,500)
        logging.info('左滑一次')
        time.sleep(3)
        self.click(*self.cleantag)
        logging.info('进入清理保养类别列表')
        time.sleep(2)
# 循环滑动方法一：每次话动画后查找一次所有的text并依次存入一个临时数组，在判断目标文本是不是在当前临时数组中
#如果不在则继续滑动—采集文本—判断。只到判断结果未true。 跳出循环 执行后面的语句
        # textslist = []
        # while True:
        #     try:
        #         textviewlist = self.find_elements(*self.textviewclass)
        #         for el in textviewlist:
        #             text = el.text
        #             textslist.append(text)
        #         print(textslist)
        #         name='宁波市三个阿姨信息科技有限公司 '
        #         assert name in textslist
        #         break
        #     except AssertionError:
        #         self.swipeup()
        #         textslist.clear()
        #         time.sleep(2)

# 循环滑动方法2：直接查找xpath定位给的目标元素，找到元素则停止滑动，找不到报NoSuchElementException 则继续滑动
        # while True:
        #     try:
        #         self.find_element(*self.stop_tag)
        #         break
        #     except NoSuchElementException:
        #         self.swipeup()
# 循环滑动方法3：如果查找目标的函数结果是False 就继续滑动；返回结果是 True 则停止滑动；
# 如果一直滑动到最后一页（发现了底部元素）还没找到目标元素，也停止滑动

        while self.stop_swipe_tag()==False:
            if self.find_last_elem():
                logging.info('已经到底部了不再滑动')
                break
            self.swipeup()

        self.click(*self.select)
        self.click(*self.homelectronics)
        self.click(*self.Hightech)
        self.click(*self.confirm)
        self.input('新增商家',*self.searchinput)
        time.sleep(2)
# 通过 adb shell ime list -s 查找安卓安装的输入法
        os.system('adb shell ime set com.baidu.input_huawei/.ImeService')
        self.click(*self.searchinput2)
# 键盘事件：enter
        self.driver.keyevent(66)


    def check_store1_exist(self):
        try:
            self.find_element(*self.store1)
        except NoSuchElementException:
            return False
        else:
            return True

    def check_store2_notexist(self):
        try:
            self.find_element(*self.store2)
        except NoSuchElementException:
            return True
        else:
            return False

    def check_search_result(self):
        if self.check_store1_exist() and self.check_store2_notexist():
            logging.info('查询结果符合预期，查询测试通过')
            return True
        else:
            logging.info('查询结果错误！')
            return False

    def return_first_page(self):
        driver.keyevent(4)
        self.click(*self.fistpage)

    def stop_swipe_tag(self):
        logging.info('================stop_swipe_tag================')
        try:
            self.find_element(*self.stop_tag)
        except NoSuchElementException:
            logging.info('未找到目标元素，继续上滑')
            return False
        else:
            logging.info('找到目标元素，停止滑动')
            return True

    def find_last_elem(self):
        try:
            self.find_element(*self.last_tag)
        except NoSuchElementException:
            return False
        else:
            logging.info('已发现底部标志')
            return True





if __name__=='__main__':
    driver = appium_desired()
    l = loginView(driver)
    s=serviceView(driver)
    l.login_action('15500001010', '111111')
    l.check_login_success()
    s.search_store_action()
    s.check_search_result()
    s.return_first_page()






