from common.myunit import StartEnd
from businessView.loginView import loginView
import unittest
import logging

class test_login(StartEnd):

    # @unittest.skip(reason) 装饰器：无条件跳过装饰的测试，并说明跳过测试的原因。
    # @unittest.skipIf(a > 5, "condition is not satisfied!") 条件为真时，跳过装饰的测试，并说明跳过测试的原因。
    # @unittest.skipUnless(sys.platform.startswith("linux"), "requires Linux")条件为假时，跳过装饰的测试，并说明跳过测试的原因。
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