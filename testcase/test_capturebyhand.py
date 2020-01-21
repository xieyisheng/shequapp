# -*- coding:utf-8 -*-
from common.myunit import StartEnd
from businessView.capturebyhandView import capturebyhandView
from businessView.loginView import loginView
from common.common_fun import common
import unittest
import logging

class test_capturebyhand(StartEnd):

    def test_send_capturebyhand(self):
        '''随手拍测试用例，验证添加图片和录音并提交'''
        logging.info('=============test_send_capturebyhand============')
        l=loginView(self.driver)
        ca=capturebyhandView(self.driver)
        c=common(self.driver)
        l.login_action('15500001010', '111111')
        ca.send_capturebyhand_action()
        self.assertTrue(ca.check_capturebyhand_result())
        c.add_screenshot_to_report('test_send_capturebyhand')


if __name__=='__main__':
    unittest.main()