# -*- coding:utf-8 -*-
import logging
from common.common_fun import common, NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from common.users import owner_dependents,owner_be_deleted,owner_not_pass,owner_have_dep,owner_del_dep,dependents_pass,dependents_notpass,tenant_pass
from businessView.registerView import registerView
from businessView.loginView import loginView
from businessView.bindhouseView import bindhouseView
import traceback
import time

class committee_verify_View(common):
    usercenter_tag = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView')
    logout_btn = (By.XPATH, '//android.widget.TextView[@text="退出登录"]')
    logout_confirm = (By.ID, 'android:id/button1')
    usercenter_my2 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[6]/android.widget.ImageView')
    usercenter_my3 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[6]')
    ownerlist=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ImageView')
    ownerlist2=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup')

    goback=(By.XPATH,'//android.view.ViewGroup[@content-desc=" "]/android.view.ViewGroup/android.widget.ImageView')
    ownerverify = (By.XPATH, '//android.widget.TextView[@text="业主审核"]')
    verify_pass = (By.XPATH, '//android.widget.TextView[@text="审核通过"]')
    verify_refuse= (By.XPATH, '//android.widget.TextView[@text="审核不通过"]')
    confirm_owner = (By.XPATH, '//android.widget.Button[@text="设为业主"]')
    confirm_retain_dep= (By.XPATH, '//android.widget.Button[@text="设为家属"]')
    confirm_del_dep= (By.XPATH, '//android.widget.Button[@text="删除业主"]')
    confirm_notowner= (By.XPATH, '//android.widget.Button[@text="确定"]')
    owner_dependents_elem = (By.XPATH, '//android.widget.TextView[@text="%s"]' %owner_dependents['name'])
    owner_not_pass_elem= (By.XPATH, '//android.widget.TextView[@text="%s"]' %owner_not_pass['name'])
    owner_be_deleted_elem= (By.XPATH, '//android.widget.TextView[@text="%s"]' %owner_be_deleted['name'])
    owner_have_dep_elem= (By.XPATH, '//android.widget.TextView[@text="%s"]' %owner_have_dep['name'])
    owner_del_dep_elem= (By.XPATH, '//android.widget.TextView[@text="%s"]' %owner_del_dep['name'])
    family_meb = (By.XPATH, '//android.widget.TextView[@text="家庭成员"]')



    def committee_verify_action(self):
        logging.info('================committee_verify_action==============')
        try:
            self.click(*self.usercenter_my3)
            self.click(*self.ownerverify)
        except Exception as e:
            raise e


    def verify_owner_dependents_action(self):
        logging.info('================verify_owner_dependents_action==============')
        try:
            self.click(*self.owner_dependents_elem)
            self.click(*self.verify_pass)
            self.click(*self.confirm_owner)
            self.find_toast_element('提交成功')
            logging.info('检测到 提交成功 提示')
        except Exception as e:
            self.getscreenshot('审核业主—家属出现错误')
            logging.info('审核业主转家属过程出现错误：%s' %traceback.format_exc())


    def check_owner_dependents_result(self):
        logging.info('================check_owner_dependents_result==============')
        try:
            self.click(*self.ownerlist2)
            self.find_element(*self.owner_dependents_elem)
        except NoSuchElementException:
            logging.info('业主列表中未找到：%s' %owner_dependents['name'])
            self.getscreenshot('查找业主—家属失败')
            return False
        else:
            logging.info('业主列表中成功找到 %s'%owner_dependents['name'])
            return True
        finally:
            self.click(*self.goback)

    def verify_owner_not_pass_action(self):
        logging.info('================verify_owner_not_pass_action==============')
        try:
            self.click(*self.owner_not_pass_elem)
            self.click(*self.verify_refuse)
            self.click(*self.confirm_notowner)
            self.find_toast_element('提交成功')
            logging.info('检测到 提交成功 提示')
        except Exception as e:
            self.getscreenshot('审核业主—不通过出现错误')
            logging.info('审核业主—不通过过程出现错误：%s' %traceback.format_exc())


    def check_owner_not_pass_result(self):
        logging.info('================check_owner_not_pass_result==============')
        try:
            self.click(*self.ownerlist2)
            self.find_element(*self.owner_not_pass_elem)
        except NoSuchElementException:
            logging.info('业主列表中符合预期的未找到：%s' %owner_not_pass['name'])
            return True
        else:
            logging.info('业主列表中错误的找到 %s'%owner_not_pass['name'])
            self.getscreenshot('错误的找到业主—不通过')
            return False
        finally:
            self.click(*self.goback)

    def verify_owner_be_deleted_action(self):
        logging.info('================verify_owner_be_deleted_action==============')
        try:
            self.click(*self.owner_be_deleted_elem)
            self.click(*self.verify_pass)
            self.click(*self.confirm_owner)
            self.find_toast_element('提交成功')
            logging.info('检测到 提交成功 提示')
        except Exception as e:
            self.getscreenshot('审核业主—被删除出现错误')
            logging.info('审核业主被删除过程出现错误：%s' %traceback.format_exc())

    def check_owner_be_deleted_result(self):
        logging.info('================check_owner_dependents_result==============')
        try:
            self.click(*self.ownerlist2)
            self.find_element(*self.owner_be_deleted_elem)
        except NoSuchElementException:
            logging.info('业主列表中未找到：%s' %owner_be_deleted['name'])
            self.getscreenshot('查找业主—被删除失败')
            return False
        else:
            logging.info('业主列表中成功找到 %s'%owner_be_deleted['name'])
            return True
        finally:
            self.click(*self.goback)

    def verify_owner_have_dep_action(self):
        logging.info('================verify_owner_have_dep_action==============')
        try:
            self.click(*self.owner_have_dep_elem)
            self.click(*self.verify_pass)
            self.click(*self.confirm_retain_dep)
            self.find_toast_element('提交成功')
            logging.info('检测到 提交成功 提示')
        except Exception as e:
            self.getscreenshot('审核业主—留家属出现错误')
            logging.info('审核业主留家属过程出现错误：%s' %traceback.format_exc())

    def check_owner_have_dep_result(self):
        logging.info('================check_owner_have_dep_result==============')
        try:
            self.click(*self.ownerlist2)
            self.find_element(*self.owner_have_dep_elem)
        except NoSuchElementException:
            logging.info('业主列表中未找到：%s' %owner_have_dep['name'])
            self.getscreenshot('查找业主—留家属失败')
            return False
        else:
            logging.info('业主列表中成功找到 %s'%owner_have_dep['name'])
            return True
        finally:
            self.click(*self.goback)


    def verify_owner_del_dep_action(self):
        logging.info('================verify_owner_del_dep_action==============')
        try:
            self.click(*self.owner_del_dep_elem)
            self.click(*self.verify_pass)
            self.click(*self.confirm_del_dep)
            self.find_toast_element('提交成功')
            logging.info('检测到 提交成功 提示')
        except Exception as e:
            self.getscreenshot('审核业主—删家属出现错误')
            logging.info('审核业主—删家属过程出现错误：%s' %traceback.format_exc())

    def check_owner_del_dep_result(self):
        logging.info('================check_owner_del_dep_result==============')
        try:
            self.click(*self.ownerlist2)
            self.find_element(*self.owner_del_dep_elem)
        except NoSuchElementException:
            logging.info('业主列表中未找到：%s' %owner_del_dep['name'])
            self.getscreenshot('查找业主—删家属失败')
            return False
        else:
            logging.info('业主列表中成功找到 %s'%owner_del_dep['name'])
            return True
        finally:
            self.click(*self.goback)

    def logout_after_check_owners(self):
        logging.info('==============logout_after_check_owners=============')
        self.driver.keyevent(4)
        try:
            self.driver.find_element(*self.usercenter_my3).click()
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

    def check_have_dep_result(self):
        #driver=appium_desired()
        l=loginView(self.driver)
        l.login_action(owner_have_dep['phone'],'111111')
        self.click(*self.usercenter_my3)
        self.click(*self.family_meb)
        try:
            self.find_element(*self.owner_dependents_elem)
        except NoSuchElementException:
            logging.info('家属列表中未找到：%s' % owner_dependents['name'])
            self.getscreenshot('家属中未发现业主—家属')
            return False
        else:
            logging.info('家属列表中成功找到：%s' % owner_dependents['name'])
            return True

    def check_no_dep_result(self):
        #driver=appium_desired()  这句有错，因为在执行测试时 会有一个driver已经起来，此处写上造成session冲突
        l=loginView(self.driver)
        l.login_action(owner_del_dep['phone'],'111111')
        self.click(*self.usercenter_my2)
        self.click(*self.family_meb)
        try:
            self.find_element(*self.owner_be_deleted_elem)
        except NoSuchElementException:
            logging.info('家属列表中按预期未找到：%s' % owner_be_deleted['name'])
            return True
        else:
            logging.info('家属列表中错误的找到：%s' % owner_be_deleted['name'])
            self.getscreenshot('家属中错误的找到业主—被删除')
            return False


if __name__ == '__main__':
    driver=appium_desired()
    v=committee_verify_View(driver)
    l = loginView(driver)
    b = bindhouseView(driver)
    reg = registerView(driver)
    reg.register_action(owner_dependents)
    reg.check_register_success()
    b.bindhouse_action(owner_dependents)
    b.check_bind_result(113)
    b.logout_after_bind()
    reg.register_action(owner_have_dep)
    reg.check_register_success()
    b.bindhouse_action(owner_have_dep)
    b.check_bind_result(113)
    b.logout_after_bind()
    l.login_action('15500001010', '111111')
    time.sleep(5)
    v.committee_verify_action()
    v.verify_owner_dependents_action()
    v.check_owner_dependents_result()
    v.verify_owner_have_dep_action()
    v.check_owner_have_dep_result()
    v.logout_after_check_owners()
    v.check_have_dep_result()



    """
    driver = appium_desired()
    reg = registerView(driver)
    b = bindhouseView(driver)
    v=committee_verify_View(driver)
    l=loginView(driver)
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

    l.login_action('15500001010','111111')
    v.committee_verify_action()
    v.verify_owner_dependents_action()
    v.check_owner_dependents_result()
    v.verify_owner_not_pass_action()
    v.check_owner_not_pass_result()
    v.verify_owner_be_deleted_action()
    v.check_owner_be_deleted_result()
    v.verify_owner_have_dep_action()
    v.check_owner_have_dep_result()
    v.verify_owner_del_dep_action()
    v.check_owner_del_dep_result()
    v.logout_after_check_owners()
    v.check_have_dep_result()
    v.check_no_dep_result()
    """


























