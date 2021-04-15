import time

from quote.bese.usebrower import Usebrowser


class WebOperation:

    def __init__(self,driver):
        self.driver = driver

    #打开网址
    def open_url(self,url):
        self.driver.get(url)

    #输入文本（通过name）
    def input_text_name(self,name_locator,text):
        self.driver.find_element_by_name(name_locator).send_keys(text)

    #输入文本（通过xpath）
    def input_text_xpath(self,xpath_locator,text):
        self.driver.find_element_by_name(xpath_locator).send_keys(text)

    #点击（通过Xpath）
    def click_xpath(self,xpath_locator):
        time.sleep(1)
        self.driver.find_element_by_xpath(xpath_locator).click()

    #获取文本信息
    def get_text_xpath(self,xpath_locator):
        return self.driver.find_element_by_xpath(xpath_locator).text

    #切换窗体
    def change_frame_element(self,xpath):
        self.driver.switch_to.default_content()
        element = self.driver.find_element_by_xpath(xpath)
        self.driver.switch_to.frame(element)

    def change_window_element(self,title):
        for window in self.driver.window_handles:
            self.driver.switch_to.window(window)
            if window == title:
                break
#
# if __name__ == '__main__':
#     ub = Usebrowser("Chrome")
#     op = WebOperation(Usebrowser.driver)
#     op.open_url('http://localhost:8080/JavaPrj_6/')
#     op.input_text_name('username','admin')
#     op.input_text_name('password','123456')
#     Usebrowser.quit()
#     time.sleep(3)

