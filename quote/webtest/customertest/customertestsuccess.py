import unittest

from quote.bese.usebrower import Usebrowser
from quote.db.dbcustomer.customeroperation import DbCustomerOp
from quote.page.customerpage import CustomerPage


class Customer_add_success_Case(unittest.TestCase):
    def setUp(self) -> None:
        self.ub = Usebrowser
        self.customerpage = CustomerPage()
        self.db = DbCustomerOp()

    def test_customer_1_case(self):
        self.db.delete_customer_account(['123302'])
        self.customerpage.add_customer("123302", 'mike', '1366666666', '1', '1', '1')
        self.assertEqual(self.customerpage.get_success_text(),'添加记录成功！')
        # if self.customerpage.get_success_text() == "添加记录成功！":
        #     print("pass")
        # else:
        #     print("failed")

    def test_customer_2_case(self):
        self.db.delete_customer_account(['1277312'])
        self.customerpage.add_customer("1277312", '', '1366666666', '', '', '')
        self.assertEqual(self.customerpage.get_success_text(),'添加记录成功！')


    def tearDown(self) -> None:
        Usebrowser.quit()

    # if __name__ == "__main__":
    #     customer_success = CustomerTestSuccess()
    #     customer_success.set_up()
    #     customer_success.customer_1_case()
    #     customer_success.tear_down()
    #



if __name__ == '__main__':
    unittest.main()
