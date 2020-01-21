import logging
from common.common_fun import common, NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from common.users import owner_dependents,owner_be_deleted,owner_not_pass,owner_have_dep,owner_del_dep,dependents_pass,dependents_notpass,tenant_pass
from businessView.registerView import registerView
from businessView.loginView import loginView
import traceback
import time


class bindhouseView(common):
    usercenter_my2 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[6]/android.widget.ImageView')
    myhouse = (By.XPATH, '//android.widget.TextView[@text="我的房屋"]')
    guide = (By.XPATH,
             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView')
    addhouse = (By.XPATH,
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ImageView')
    realnamenow = (By.XPATH, '//android.widget.TextView[@text="立即实名"]')
    name_input = (By.XPATH, '//android.widget.EditText[@text="请输入真实姓名"]')
    idcard_input = (By.XPATH, '//android.widget.EditText[@text="请输入身份证号码"]')
    saveinfo = (By.XPATH, '//android.widget.TextView[@text="提交"]')
    addhousebtn = (By.XPATH,
                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ImageView')
    area = (By.XPATH, '//android.widget.TextView[@text="北仑区"]')
    street = (By.XPATH, '//android.widget.TextView[@text="小港街道"]')
    community = (By.XPATH, '//android.widget.TextView[@text="高河塘社区"]')
    residence = (By.XPATH, '//android.widget.TextView[@text="第一城7期"]')
    build = (By.XPATH, '//android.widget.TextView[@text="七期2号"]')
    houseNo113 = (By.XPATH, '//android.widget.TextView[@text="2单元113号"]')
    houseNo112 = (By.XPATH, '//android.widget.TextView[@text="2单元112号"]')
    identity_owner = (By.XPATH, '//android.widget.TextView[@text="业主"]')
    identity_dependents = (By.XPATH, '//android.widget.TextView[@text="家属"]')
    identity_tenant = (By.XPATH, '//android.widget.TextView[@text="租户"]')
    confirm = (By.XPATH, '//android.widget.Button[@text="确定"]')
    backbtn = (By.XPATH,'//android.widget.TextView[@text="返回首页"]')
    lefttop = (By.XPATH, '//android.widget.TextView[@text="智慧示范小区1幢"]')
    myhouselist113 = (By.XPATH, '//android.widget.TextView[@text="第一城7期七期2号2单元113"]')
    myhouselist112 = (By.XPATH, '//android.widget.TextView[@text="第一城7期七期2号2单元112"]')
    usercenter_tag = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView')
    logout_btn = (By.XPATH, '//android.widget.TextView[@text="退出登录"]')
    logout_confirm = (By.ID, 'android:id/button1')

    def bindhouse_action(self,type):
        logging.info('=====================bindhouse_action=================')
        try:
            self.click(*self.usercenter_my2)
            self.click(*self.myhouse)
            self.check_bind_guide()
            logging.info('点击立即实名')
            self.click(*self.realnamenow)
            logging.info('输入用户名%s' %type['name'])
            self.input(type['name'], *self.name_input)
            logging.info('输入身份证%s' %type['idcode'])
            self.input(type['idcode'], *self.idcard_input)
            self.click(*self.saveinfo)
            self.find_toast_element('修改用户信息成功')
            logging.info('检测到用户信息提交成功提示')
            logging.info('开始选择区县/街道/社区/小区/房屋/身份')
            self.click(*self.addhousebtn)
            self.click(*self.area)
            self.click(*self.street)
            self.click(*self.community)
            self.click(*self.residence)
            self.click(*self.build)
            time.sleep(2)
            str=type['type']
            if str=='业主转家属' or str=='业主未通过' or str=='业主有家属' or str=='通过的家属' or str=='不通过的家属' or str=='通过的租户':
                self.click(*self.houseNo113)
                if str=='通过的家属' or str=='不通过的家属':
                    self.click(*self.identity_dependents)
                elif str=='通过的租户':
                    self.click(*self.identity_tenant)
                else:
                    self.click(*self.identity_owner)
                logging.info('用户：%s选择绑定113' %type['name'])
            elif str=='业主被删除' or str=='业主无家属':
                self.click(*self.houseNo112)
                self.click(*self.identity_owner)
                logging.info('用户：%s选择绑定112' % type['name'])
            time.sleep(2)
            self.click(*self.confirm)
            logging.info('确认绑定所选房屋')
            time.sleep(3)
            self.check_submit_prompt()
        except Exception as e:
            self.getscreenshot('绑定房屋过程出现错误')
            logging.info('绑定房屋过程出现错误：%s' %traceback.format_exc())

    def check_submit_prompt(self):
        logging.info('==================check_submit_prompt==============')
        try:
            self.find_element(self.backbtn)
        except NoSuchElementException:
            logging.info('未找到 返回首页 提示信息，通过物理返回进入=我的=页面')
            self.driver.keyevent(4)
            self.driver.keyevent(4)
            self.click(*self.myhouse)
        else:
            logging.info('找到 返回首页 提示信息，点击返回首页，然后点击左上角进入房屋列表')
            self.click(*self.backbtn)
            self.click(*self.lefttop)







    def check_bind_guide(self):
        logging.info('=====================check_bing_guide=================')
        try:
            self.find_element(*self.guide)
        except NoSuchElementException:
            logging.info('未出现添加小区引导')
            self.click(*self.addhouse)
        else:
            logging.info('点击添加小区引导图片')
            self.click(*self.guide)

    def check_bind_result(self,houselist):
        logging.info('================check_bind_result==============')
        try:
            if houselist==113:
                self.find_element(*self.myhouselist113)
            elif houselist==112:
                self.find_element(*self.myhouselist112)
        except NoSuchElementException:
            logging.info('绑定小区房屋失败')
            self.getscreenshot('检查绑定房屋失败')
            return False
        else:
            logging.info('绑定小区房屋 %s成功' %houselist)
            return True



    def logout_after_bind(self):
        logging.info('==============logout_after_register=============')
        self.driver.keyevent(4)
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






if __name__ == '__main__':

    driver = appium_desired()
    reg = registerView(driver)
    b = bindhouseView(driver)
    reg.register_action(owner_have_dep)
    reg.check_register_success()
    b.bindhouse_action(owner_have_dep)
    b.check_bind_result(113)
    b.logout_after_bind()
    reg.register_action(owner_be_deleted)
    reg.check_register_success()
    b.bindhouse_action(owner_be_deleted)
    b.check_bind_result(112)
    b.logout_after_bind()
    reg.register_action(owner_not_pass)
    reg.check_register_success()
    b.bindhouse_action(owner_not_pass)
    b.check_bind_result(113)
    b.logout_after_bind()
    reg.register_action(owner_dependents)
    reg.check_register_success()
    b.bindhouse_action(owner_dependents)
    b.check_bind_result(113)
    b.logout_after_bind()
    reg.register_action(owner_del_dep)
    reg.check_register_success()
    b.bindhouse_action(owner_del_dep)
    b.check_bind_result(112)
    b.logout_after_bind()
