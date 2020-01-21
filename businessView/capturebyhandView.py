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


class capturebyhandView(common):


    captureenter=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView')
    addcapture=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView')
    addcapture2=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView')
    camera=(By.XPATH,'//android.widget.TextView[@text="相机"]')
    Album=(By.XPATH,'//android.widget.TextView[@text="相册图片"]')
    albumpic=(By.CLASS_NAME,'android.widget.ImageView')
    allow_photo = (By.XPATH, '//android.widget.Button[@text="始终允许"]')
    takebtn = (By.ID,'com.huawei.camera:id/shutter_button')
    takebtn2= (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]')
    photo_done= (By.ID, 'com.huawei.camera:id/done_button')
    recordsound=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.ImageView')
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    word=now+'随手拍工单请及时处理'
    newcap=(By.XPATH,'//android.widget.TextView[@text="%s"]' %word)

    word_input = (By.XPATH, '//android.widget.EditText[@text="想说的话或详细位置描述"]')
    choice_resdence=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.TextView[2]')
    resdence = (By.XPATH, '//android.widget.TextView[@text="真善美小区"]')
    confirm = (By.XPATH, '//android.widget.TextView[@text="确定"]')
    resdence7 = (By.XPATH, '//android.widget.TextView[@text="第一城7期"]')
    swipeer=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup')
    upload=(By.XPATH,'//android.widget.TextView[@text="上传"]')
    my_capturebyhand=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ImageView')






    def send_capturebyhand_action(self):
        logging.info('==================send_capturebyhand_action==================')
        try:
            self.click(*self.captureenter)
            self.check_allow_btn()
            self.click(*self.addcapture)
            self.click(*self.camera)
            self.check_allow_btn()
            time.sleep(1)
            self.check_allow_btn()
            self.click(*self.takebtn)
            WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_id('com.huawei.camera:id/done_button'))
            self.click(*self.photo_done)
            logging.info('确认所拍照片')
            self.click(*self.addcapture2)
            self.click(*self.Album)
            self.find_elements(*self.albumpic)[3].click()
            self.long_press(10,*self.recordsound)
            self.input(self.word,*self.word_input)
            #滑动选择菜单，需要先click菜单组件确保后面的swipe是在组件内滑动。
            while True:
                try:
                    self.find_element(*self.resdence7)
                    break
                except NoSuchElementException:
                    self.click(*self.choice_resdence)
                    self.click(*self.swipeer)
                    self.resdence_swipup()
                    time.sleep(1)
                    self.click(*self.confirm)
            self.click(*self.upload)
        except Exception as e:
            #logging.info('添加随手拍过程出现错误：%s' %traceback.format_exc())
            self.getscreenshot('添加随手拍过程错误')
            raise e

    def resdence_swipup(self):
        logging.info('上滑。。。')
        l=self.get_size()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.9)
        y2=int(l[1]*0.87)
        try:
            self.swipe(x1,y1,x1,y2,800)
        except Exception as e:
            raise e

    def resdence_moveup(self):
        logging.info('按住向上拖动。。。')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.9)
        y2 = int(l[1] * 0.7)
        TouchAction(self.driver).long_press(x=x1,y=y1,duration=2000).wait(3000).move_to(x=x1,y=y2).release().perform()


    def check_allow_btn(self):
        logging.info('==================check_allowphoto_btn================')
        try:
            self.find_element(*self.allow_photo)
        except NoSuchElementException:
            logging.info('没有出现权限提示')
            pass
        else:
            self.click(*self.allow_photo)
            logging.info('点击始终允许')

    def check_capturebyhand_result(self):
        logging.info('==================check_capturebyhand_result================')
        self.click(*self.captureenter)
        self.click(*self.my_capturebyhand)
        try:
            self.find_element(*self.newcap)
        except NoSuchElementException:
            logging.info('未找到刚新增的随手拍工单')
            self.getscreenshot('随手拍结果未找到')
            return False
        else:
            return True



if __name__=='__main__':
    driver = appium_desired()
    l = loginView(driver)
    cap=capturebyhandView(driver)
    l.login_action('15500001010', '111111')
    l.check_login_success()
    cap.send_capturebyhand_action()
    cap.check_capturebyhand_result()


