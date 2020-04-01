from selenium import webdriver
import page


class GetDriver:
    driver = None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            #  获取driver
            cls.driver = webdriver.Firefox()
            #  最大化浏览器
            cls.driver.maximize_window()
            #  设置隐式等待
            cls.driver.implicitly_wait(30)
            #  打开url
            cls.driver.get(page.URL)
        #  返回driver
        return cls.driver

    #  关闭driver
    @classmethod
    def quit_driver(cls):
        #  如果driver为空不关闭浏览器驱动，这样不会报错
        if cls.driver:
            cls.driver.quit()
            #  必须置空操作
            cls.driver = None
