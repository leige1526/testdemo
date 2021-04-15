import unittest

from quote.bese.usebrower import Usebrowser
from quote.page.loginpage import LoginPage
from quote.util.excel_aperation import ExcelOperation


class LoginFailedCase(unittest.TestCase):
    def setUp(self) -> None:
        self.login_page = LoginPage()
        self.excop = ExcelOperation()

    def test_1_usn_psw_is_not_exit(self):
        self.login_page.login(self.excop.get_cell_value(4,2),self.excop.get_cell_value(4,3))
        self.assertEqual(self.login_page.get_failed_text(),self.excop.get_cell_value(4,4))

    def test_2_usn_psw_is_null(self):
        self.login_page.login(self.excop.get_cell_value(4,2),self.excop.get_cell_value(4,3))
        self.assertEqual(self.login_page.get_failed_text(),self.excop.get_cell_value(4,4))

    def test_3_psw_is_null(self):
        self.login_page.login(self.excop.get_cell_value(5,2),self.excop.get_cell_value(5,3))
        self.assertEqual(self.login_page.get_failed_text(),self.excop.get_cell_value(5,4))

    def test_4_usn_null(self):
        self.login_page.login(self.excop.get_cell_value(6,2),self.excop.get_cell_value(6,3))
        self.assertEqual(self.login_page.get_failed_text(),self.excop.get_cell_value(6,4))

    def tearDown(self) -> None:
        Usebrowser.quit()


if __name__ == '__main__':
    unittest.main()
