from selenium import webdriver
import time

class Usebrowser:

    driver = None


    def __init__(self,browser_name="Chrome"):
        if browser_name == "Chrome":
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            Usebrowser.driver = self.driver
        else:
            self.driver = webdriver.firefox('../firefoxdriver.exe')


    @classmethod
    def quit(cls):
        cls.driver.quit()


# if __name__ == '__main__':
#     ub = Usebrowser("Chrome")
#     time.sleep(3)
#     Usebrowser.quit()



