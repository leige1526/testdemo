from quote.bese.usebrower import Usebrowser
from quote.bese.weboperation import WebOperation
from quote.util.excel_aperation import ExcelOperation
from quote.util.log_info import LogInfo
from quote.util.yalm_operation import YamlOperation


class LoginPage:


    def __init__(self):
        self.ub=Usebrowser('Chrome')
        self.op = WebOperation(Usebrowser.driver)
        self.yalm = YamlOperation()
        self.excel = ExcelOperation()
        self.log = LogInfo

    def login(self,username,password):
        # self.log.set_message('info','打开网址')
        self.op.open_url(self.excel.get_cell_value(1,1))
        # self.log.set_message('info', '输入用户名'+username)
        self.op.input_text_name(self.yalm.get_locator('LoginPage','username'),username)
        # self.log.set_message('info', '输入密码'+password)
        self.op.input_text_name(self.yalm.get_locator('LoginPage','password'),password)
        # self.log.set_message('info', '点击提交')
        self.op.click_xpath(self.yalm.get_locator('LoginPage','submit'))

    def get_success_text(self):
        self.op.change_frame_element(self.yalm.get_locator('LoginPage','framemian'))
        return self.op.get_text_xpath(self.yalm.get_locator('LoginPage','successinfo'))

    def get_failed_text(self):
        return self.op.get_text_xpath('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td')

# if __name__ == "__main__":
#     loginpage = LoginPage()
#     loginpage.login("admin",'123456')
#     Usebrowser.quit()