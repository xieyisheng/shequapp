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

class rubbishgameView(common):

    rubbishimg=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[13]/android.widget.ImageView')
    rubname_input=(By.XPATH,'/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]/uni-input/div/form/input')
    search=(By.XPATH,'/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]/uni-button')
    result_guide=(By.XPATH,'//span[text()= "平板电脑"]')
    result_img=(By.XPATH,'/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-image/img')
    camera=(By.XPATH,'/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]/uni-view/uni-image/img')
    takephoto=(By.ID,'com.ygwy:id/tv_user_set_avatar_picker_camera')
    takebtn=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]')
    allow_photo = (By.XPATH, '//android.widget.Button[@text="始终允许"]')
    photo_done=(By.ID,'com.huawei.camera:id/done_button')
    recognition = (By.XPATH, '//uni-view[text()="识别结果"]')
    cancelbtn= (By.XPATH,'//uni-view[text()="取消"]')
    gameenter=(By.XPATH,'/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[4]/uni-image/img')
    #gamestart=(By.XPATH,'//*[@id="start"]')
    gamestart = (By.XPATH, '/html/body/div/div[2]/img[2]')
    rubdrag=(By.ID,'drag')
    Trash=(By.XPATH,'//*[@id="box"]/img[1]')



    def rub_dist_char(self):
        logging.info('==================rub_dist_char================')
        try:
            self.click(*self.rubbishimg)
            WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_class_name('android.webkit.WebView'))
            self.switch_to_context('WEBVIEW_com.ygwy')
            logging.info('切换context：WEBVIEW_com.ygwy')
            self.input('平板电脑',*self.rubname_input)
            logging.info('输入垃圾类型：平板电脑')
            time.sleep(2)
            self.click(*self.result_guide)
        except Exception as e:
            self.getscreenshot('搜索垃圾分类过程出现错误')
            logging.info('搜索垃圾分类过程出现错误：%s' % traceback.format_exc())
            raise e

    def check_rub_dist_char_result(self):
        logging.info('==================check_rub_dist_char_result================')
        try:
            time.sleep(3)
            self.find_element(*self.result_img)
        except NoSuchElementException:
            logging.info('返回分类结果失败')
            self.getscreenshot('垃圾文本识别失败')
            return False
        else:
            logging.info('返回分类结果成功！')
            return True


    def rub_dist_photo(self):
        logging.info('==================rub_dist_photo================')
        try:
            self.click(*self.rubbishimg)
            WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_class_name('android.webkit.WebView'))
            self.switch_to_context('WEBVIEW_com.ygwy')
            logging.info('切换context：WEBVIEW_com.ygwy')
            self.click(*self.camera)
            logging.info('点击拍照图标')
            self.switch_to_context('NATIVE_APP')
            logging.info('切换回NATIVE_APP')
            self.click(*self.takephoto)
            self.check_allowphoto_btn()
            time.sleep(2)
            self.click(*self.takebtn)
            logging.info('点击相机拍照')
            WebDriverWait(self.driver,8).until(lambda x: x.find_element_by_id('com.huawei.camera:id/done_button'))
            self.click(*self.photo_done)
            logging.info('提交所拍照片')
            self.switch_to_context('WEBVIEW_com.ygwy')
            logging.info('切换回WEBVIEW_com.ygwy')
        except Exception as e:
            self.getscreenshot('操作照片识别过程出现错误')
            logging.info('垃圾照片过程出现错误：%s' % traceback.format_exc())
            raise e

    def check_rub_dist_photo_result(self):
        logging.info('==================check_rub_dist_photo_result================')
        try:
            WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_xpath('//uni-view[text()= "识别结果"]'))
            #self.find_element(*self.recognition)
        except NoSuchElementException:
            logging.info('返回图片识别结果失败')
            self.getscreenshot('返回垃圾图片识别失败')
            return False
        else:
            logging.info('返回图片识别结果结果成功！')
            return True
        finally:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.cancelbtn)))
            self.click(*self.cancelbtn)


    def check_allowphoto_btn(self):
        logging.info('==================check_allowphoto_btn================')
        try:
            self.find_element(*self.allow_photo)
        except NoSuchElementException:
            logging.info('没有出现拍照权限提示')
            pass
        else:
            self.click(*self.allow_photo)
            logging.info('点击始终允许')

    def play_game_action(self):
        logging.info('==================play_game_action================')
        self.click(*self.gameenter)
        #WebDriverWait(self.driver,15).until(lambda x: x.find_element_by_id('start'))
        # 等待游戏开始按钮变为可见，此处self.gamestart外层多家一层括号，用来组成一个元组使之成位单个参数。否则会报多一个参数的错误
        WebDriverWait(driver,15).until(EC.visibility_of_element_located((self.gamestart)))
        time.sleep(2)
        #self.click(*self.gamestart)
        os.system('adb shell input tap 540 1110')
        time.sleep(1)
        rubdrag_elem=self.find_element(*self.rubdrag)
        Trash_elem=self.find_element(*self.Trash)
        #TouchAction(self.driver).press(x=530,y=1020).wait(1000) .move_to(x=140,y=2060).wait(1000).release().perform()
        #ActionChains(self.driver).drag_and_drop_by_offset(rubdrag_elem, 130, 2040).perform()
        TouchAction(self.driver).long_press(x=530,y=1010).wait(1000).move_to(x=140, y=2060).wait(1000).release().perform()


if __name__=='__main__':
    driver= appium_desired()
    ru=rubbishgameView(driver)
    l = loginView(driver)
    l.login_action('15500001010','111111')
    time.sleep(3)
    ru.rub_dist_char()
    time.sleep(3)
    ru.check_rub_dist_char_result()
    ru.rub_dist_photo()
    time.sleep(8)
    ru.check_rub_dist_photo_result()
    ru.play_game_action()





