from common.myunit import StartEnd
from businessView.serviceView import serviceView
from businessView.loginView import loginView
import unittest
import logging

class test_services(StartEnd):

    def test_service(self):
        logging.info('===============test_service==============')
        l=loginView(self.driver)
        s=serviceView(self.driver)
        l.login_action('15500001010','111111')
        s.search_store_action()
        self.assertTrue(s.check_search_result())

if __name__=='__main__':
    unittest.main()

