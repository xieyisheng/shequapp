from common.myunit import StartEnd
from businessView.rubbishgameView import rubbishgameView
from businessView.loginView import loginView
import unittest
import logging

class test_rubbishgame(StartEnd):

    def test_rub_dist_char(self):
        logging.info('===============test_rub_dist_char================')
        l=loginView(self.driver)
        ru=rubbishgameView(self.driver)
        l.login_action('15500001010','111111')
        ru.rub_dist_char()
        self.assertTrue(ru.check_rub_dist_char_result())

    def test_rub_dist_photo(self):
        logging.info('===============test_rub_dist_photo================')
        l=loginView(self.driver)
        ru=rubbishgameView(self.driver)
        l.login_action('15500001010','111111')
        ru.rub_dist_photo()
        self.assertTrue(ru.check_rub_dist_photo_result())

if __name__=='__main__':
    unittest.main()