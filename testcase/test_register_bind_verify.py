# -*- coding:utf-8 -*-
from common.myunit import StartEnd
from businessView.registerView import registerView
from businessView.bindhouseView import bindhouseView
from businessView.loginView import loginView
from businessView.committee_verify_View import committee_verify_View
from common.idCardandphone import get_user_info
from common.users import owner_dependents,owner_be_deleted,owner_not_pass,owner_have_dep,owner_del_dep
import unittest
import logging



class testregister(StartEnd):


    def test_0register_ownerdependents(self):
        logging.info('===========test_register_ownerdependents==========')
        re=registerView(self.driver)
        re.register_action(owner_dependents)
        self.assertTrue(re.check_register_success())

    def test_0register_ownerbedeleted(self):
        logging.info('===========test_register_ownerbedeleted==========')
        re=registerView(self.driver)
        re.register_action(owner_be_deleted)
        self.assertTrue(re.check_register_success())

    def test_0register_ownerhavedep(self):
        logging.info('===========test_register_ownerhavedep==========')
        re=registerView(self.driver)
        re.register_action(owner_have_dep)
        self.assertTrue(re.check_register_success())

    def test_0register_ownernotpass(self):
        logging.info('===========test_register_ownernotpass==========')
        re=registerView(self.driver)
        re.register_action(owner_not_pass)
        self.assertTrue(re.check_register_success())

    def test_0register_ownerdeldep(self):
        logging.info('===========test_register_ownerdeldep==========')
        re=registerView(self.driver)
        re.register_action(owner_del_dep)
        self.assertTrue(re.check_register_success())

    def test_1bindhouse_owner_have_dep(self):
        logging.info('===========test_bindhouse_owner_have_dep==========')
        b = bindhouseView(self.driver)
        l = loginView(self.driver)
        l.login_action(owner_have_dep['phone'],'111111')
        b.bindhouse_action(owner_have_dep)
        self.assertTrue(b.check_bind_result(113))

    def test_1bindhouse_owner_be_deleted(self):
        logging.info('===========test_bindhouse_owner_be_deleted==========')
        b=bindhouseView(self.driver)
        l = loginView(self.driver)
        l.login_action(owner_be_deleted['phone'], '111111')
        b.bindhouse_action(owner_be_deleted)
        self.assertTrue(b.check_bind_result(112))

    def test_1bindhouse_owner_not_pass(self):
        logging.info('===========test_bindhouse_owner_not_pass==========')
        b=bindhouseView(self.driver)
        l = loginView(self.driver)
        l.login_action(owner_not_pass['phone'], '111111')
        b.bindhouse_action(owner_not_pass)
        self.assertTrue(b.check_bind_result(113))

    def test_1bindhouse_owner_dependents(self):
        logging.info('===========test_bindhouse_owner_dependents==========')
        b=bindhouseView(self.driver)
        l = loginView(self.driver)
        l.login_action(owner_dependents['phone'], '111111')
        b.bindhouse_action(owner_dependents)
        self.assertTrue(b.check_bind_result(113))

    def test_1bindhouse_owner_del_dep(self):
        logging.info('===========test_bindhouse_owner_del_dep==========')
        b=bindhouseView(self.driver)
        l = loginView(self.driver)
        l.login_action(owner_del_dep['phone'], '111111')
        b.bindhouse_action(owner_del_dep)
        self.assertTrue(b.check_bind_result(112))

    def test_2verify_1owner_dependents(self):
        logging.info('===========test_2verify_1owner_dependents==========')
        v = committee_verify_View(self.driver)
        l = loginView(self.driver)
        l.login_action('15500001010', '111111')
        v.committee_verify_action()
        v.verify_owner_dependents_action()
        self.assertTrue(v.check_owner_dependents_result())

    def test_2verify_2owner_not_pass(self):
        logging.info('===========test_2verify_2owner_not_pass==========')
        v = committee_verify_View(self.driver)
        l = loginView(self.driver)
        l.login_action('15500001010', '111111')
        v.committee_verify_action()
        v.verify_owner_not_pass_action()
        self.assertTrue(v.check_owner_not_pass_result())

    def test_2verify_3owner_be_deleted(self):
        logging.info('===========test_2verify_3owner_be_deleted==========')
        v = committee_verify_View(self.driver)
        l = loginView(self.driver)
        l.login_action('15500001010', '111111')
        v.committee_verify_action()
        v.verify_owner_be_deleted_action()
        self.assertTrue(v.check_owner_be_deleted_result())

    def test_2verify_4owner_have_dep(self):
        logging.info('===========test_2verify_4owner_have_dep==========')
        v = committee_verify_View(self.driver)
        l = loginView(self.driver)
        l.login_action('15500001010', '111111')
        v.committee_verify_action()
        v.verify_owner_have_dep_action()
        self.assertTrue(v.check_owner_have_dep_result())

    def test_2verify_5owner_del_dep(self):
        logging.info('===========test_2verify_5owner_del_dep==========')
        v = committee_verify_View(self.driver)
        l = loginView(self.driver)
        l.login_action('15500001010', '111111')
        v.committee_verify_action()
        v.verify_owner_del_dep_action()
        self.assertTrue(v.check_owner_del_dep_result())

    def test_3check_1have_dep_result(self):
        logging.info('===========test_2check_6have_dep_result==========')
        v = committee_verify_View(self.driver)
        self.assertTrue(v.check_have_dep_result())

    def test_3check_2no_dep_result(self):
        logging.info('===========test_2check_7no_dep_result==========')
        v = committee_verify_View(self.driver)
        self.assertTrue(v.check_no_dep_result())



if __name__=='__main__':
    unittest.main()