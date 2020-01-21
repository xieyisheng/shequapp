import logging
import time
from  common.common_fun import common,By,NoSuchElementException
from common.desired_caps import appium_desired
from common.idCardandphone import get_user_info
from businessView.loginView import loginView

#随机生成一组 姓名/手机号/身份证号 用于注册业主。 1为业主 2为家属 3为租户
owner_dependents=get_user_info('业主转家属')
owner_be_deleted=get_user_info('业主被删除')
owner_not_pass=get_user_info('业主未通过')
owner_have_dep=get_user_info('业主有家属')
owner_del_dep=get_user_info('业主无家属')
dependents_pass=get_user_info('通过的家属')
dependents_notpass=get_user_info('不通过的家属')
tenant_pass=get_user_info('通过的租户')

class registerView(common):
    mobile_login=(By.XPATH,'//android.widget.TextView[@text="手机快捷登录"]')
    mobile_input = (By.CLASS_NAME,'android.widget.EditText')
    sendcode=(By.XPATH,'//android.widget.TextView[@text="获取验证码"]')
    code_input = (By.XPATH, '//android.widget.EditText[@text="请输入验证码"]')
    login_btn = (By.XPATH, '//android.widget.TextView[@text="立即登录"]')
    usercenter_my = (By.XPATH, '//android.widget.TextView[@text="我的"]')

    def check_code_send(self):
        try:
            self.find_toast_element('验证码发送成功')
        except Exception as e:
            raise e
        else:
            logging.info('成功检测到验证码提示')
            return True


    def register_action(self,type):
        logging.info('===================register_action=================')
        time.sleep(3)
        self.check_update_msg()
        try:
            self.driver.find_element(*self.mobile_login).click()
            oldnumber=self.driver.find_elements(*self.mobile_input)[0].text
            self.driver.keyevent(123)  # 123代表光标移动到末尾键
            for i in range(0, len(oldnumber)):
                self.driver.keyevent(67)
            self.driver.find_elements(*self.mobile_input)[0].send_keys(type['phone'])
            self.driver.find_element(*self.sendcode).click()
            self.check_code_send()
            time.sleep(5)
            self.driver.find_element(*self.code_input).send_keys('111111')
            self.driver.find_element(*self.login_btn).click()
        except Exception as e:
            raise e
        else:
            logging.info('已执行注册 %s' %type['phone'])

    def check_register_success(self):
        logging.info('===============check_register_success===============')
        self.check_update_msg()
        try:
            self.driver.find_element(*self.usercenter_my)
        except NoSuchElementException:
            logging.info('注册失败')
            self.getscreenshot('register fail')
            return False
        else:
            logging.info('注册成功！')
            return True



if __name__=='__main__':
    driver=appium_desired()
    contexts = driver.contexts
    print(contexts)

    #reg=registerView(driver)
    #reg.register_action(owner_be_deleted)
    #reg.check_register_success()


