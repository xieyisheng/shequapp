from common.myunit import StartEnd
from businessView.loginView import loginView
import unittest
import logging

class test_login(StartEnd):

    # @unittest.skip(reason) װ����������������װ�εĲ��ԣ���˵���������Ե�ԭ��
    # @unittest.skipIf(a > 5, "condition is not satisfied!") ����Ϊ��ʱ������װ�εĲ��ԣ���˵���������Ե�ԭ��
    # @unittest.skipUnless(sys.platform.startswith("linux"), "requires Linux")����Ϊ��ʱ������װ�εĲ��ԣ���˵���������Ե�ԭ��
    def test_login_success(self):
        logging.info('===========test_login_success==========')
        l=loginView(self.driver)
        l.login_action('15500001010','111111')
        self.assertTrue(l.check_login_success())

    def test_login_fail(self):
        logging.info('===========est_login_fail==========')
        l = loginView(self.driver)
        l.login_action('15500001010','222222')
        self.assertTrue(l.check_login_fail)

if __name__=='__main__':
    unittest.main()