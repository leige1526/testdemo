from quote.bese.usebrower import Usebrowser
from quote.bese.weboperation import WebOperation
from quote.page.loginpage import LoginPage


class CustomerPage:
    def __init__(self):
        self.loginpage = LoginPage()
        self.op =WebOperation(Usebrowser.driver)

    def add_customer(self,cusno,cusname,cusphone,cusaddress,cusralat,other):
        self.loginpage.login("admin","123456")
        self.op.change_frame_element('/html/frameset/frame[1]')
        self.op.click_xpath('//*[@id="Bar_panel0_b0"]/img')
        self.op.change_frame_element('/html/frameset/frame[2]')
        self.op.click_xpath('/html/body/center/table[2]/tbody/tr[2]/td[2]/a')
        self.op.change_window_element('新增客户信息')
        self.op.input_text_name('customerNO',cusno)
        self.op.input_text_name('customerName',cusname)
        self.op.input_text_name('phone',cusphone)
        self.op.input_text_name('address',cusaddress)
        self.op.input_text_name('relationman',cusralat)
        self.op.input_text_name('otherInfo',other)
        self.op.click_xpath('/html/body/center/form/table[2]/tbody/tr/td/input[1]')

    def get_success_text(self):
        return self.op.get_text_xpath('/html/body/center')[0:7]



    def modify_customer(self):
        pass


# if __name__ == "__main__":
# ub = Usebrowser()
# customerpage = CustomerPage()
# customerpage.add_customer("123312",'mike','1366666666','','','')
# Usebrowser.quit
