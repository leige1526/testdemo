import sys
sys.path.append('D:\\PyCharm Community Edition 2020.3.3\\pythonProject1')
from HwTestReport import HTMLTestReportEN
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from quote.bese.usebrower import Usebrowser
from quote.page.loginpage import LoginPage
from quote.util.excel_aperation import ExcelOperation
from quote.webtest.customertest.customertestsuccess import Customer_add_success_Case
from quote.webtest.logintext.loginfailedtest import LoginFailedCase

class LoginsuccessCase(unittest.TestCase):
    def setUp(self) -> None:
        self.login_page = LoginPage()
        self.excop = ExcelOperation()


    def test_1_success_case(self):
        self.login_page.login(self.excop.get_cell_value(1,2),self.excop.get_cell_value(1,3))
        self.assertEqual(self.login_page.get_success_text(),self.excop.get_cell_value(1,4))

    def test_2_success_case(self):
        self.login_page.login(self.excop.get_cell_value(2,2),self.excop.get_cell_value(2,3))
        self.assertEqual(self.login_page.get_success_text(),self.excop.get_cell_value(2,4))


    def tearDown(self) -> None:
        Usebrowser.quit()

if __name__ == '__main__':
    #测试套件
    suite = unittest.TestSuite()
    #加载测试用例
    login_failed_case = unittest.TestLoader().loadTestsFromTestCase(LoginFailedCase)
    login_success_case = unittest.TestLoader().loadTestsFromTestCase(LoginsuccessCase)
    customer_add_success = unittest.TestLoader().loadTestsFromTestCase(Customer_add_success_Case)
    #case加入到测试套件中
    case_contet = [login_failed_case,login_success_case,customer_add_success]
    suite.addTests(case_contet)
    file_date = time.strftime('%Y-%m-%d_%H_%M_%S')
    #报告文件写入
    # fp = open('../../report/report'+file_date+'.html','wb+')
    with open('../../report/report'+file_date+'.html','wb+') as fp:
        runner = HTMLTestReportEN(stream=fp, verbosity=2, title='Quote Project', description='UI Auto Test')
        #文本测试运行对象
        # runner = unittest.TextTestRunner(verbosity=2)
        #执行
        runner.run(suite)

