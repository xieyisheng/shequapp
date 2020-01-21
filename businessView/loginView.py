import logging
from common.common_fun import common,NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
import time

class loginView(common):
    username_password_input=(By.CLASS_NAME,'android.widget.EditText')
    #password_input=(By.XPATH,'//android.widget.EditText[@text="请输入登录密码"]')
    login_btn=(By.XPATH,'//android.widget.TextView[@text="立即登录"]')
    usercenter_my=(By.XPATH,'//android.widget.TextView[@text="我的"]')
    usercenter_my2=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[6]/android.widget.ImageView')
    usercenter_tag=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView')
    logout_btn=(By.XPATH,'//android.widget.TextView[@text="退出登录"]')
    logout_confirm=(By.ID,'android:id/button1')

    failmessage = '用户名或密码不正确，请重新输入'

    def login_action(self,username,password):
        time.sleep(3)
        self.check_update_msg()
        logging.info('============login_action==============')
        oldnumber = self.driver.find_elements(*self.username_password_input)[0].text
        self.driver.keyevent(123)  # 123代表光标移动到末尾键
        for i in range(0, len(oldnumber)):
            self.driver.keyevent(67)
        logging.info('username is %s' %username)
        self.find_elements(*self.username_password_input)[0].send_keys(username)
        logging.info('password is %s' %password)
        self.find_elements(*self.username_password_input)[1].send_keys(password)
        self.find_element(*self.login_btn).click()
        self.check_update_msg()

    def check_login_success(self):
        logging.info('===============check_login_success===============')
        self.check_update_msg()
        try:
            self.driver.find_element(*self.usercenter_my)
        except NoSuchElementException:
            logging.info('login fail!')
            self.getscreenshot('login fail')
            return False
        else:
            logging.info('login success!')
            return True

    def logout_action(self):
        logging.info('===============logout_action=============')
        try:
            self.driver.find_element(*self.usercenter_my2).click()
            time.sleep(1)
            self.swipedown()
            self.driver.find_element(*self.usercenter_tag).click()
            time.sleep(1)
            self.driver.find_element(*self.logout_btn).click()
            self.driver.find_element(*self.logout_confirm).click()
        except Exception as e:
            raise e
        else:
            logging.info('logout success!')

    def check_login_fail(self):
        try:
            self.find_toast_element('用户名或密码不正确，请重新输入')
        except Exception as e:
            raise e
        else:
            logging.info('成功检测到登录错误提示')
            return True


if __name__=='__main__':
    driver= appium_desired()
    l=loginView(driver)
    l.login_action('15500001010','111111')
    #l.check_login_fail()












