import time
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
import page
from base.get_logger import GetLogger


#  获取log日志器
log = GetLogger().get_logger()


class Base:
    def __init__(self, driver):
        log.info("[base]:正在获取初始化driver对象:{}".format(driver))
        self.driver = driver

    # 查找元素方法封装
    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        log.info("[base]:正在定位元素:{}，默认时间:{}".format(loc, timeout))
        #  显示等待查找元素
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency).until(lambda x: x.find_element(*loc))

    # 点击元素方法封装
    def base_click(self, loc):
        log.info("[base]:正在对:{}元素实行点击操作".format(loc))
        self.base_find_element(loc).click()

    # 输入元素方法封装
    def base_input(self, loc, value):
        #  获取元素
        element = self.base_find_element(loc)
        #  清空
        log.info("[base]:正在对:{}元素实行清空操作".format(loc))
        element.clear()
        #  输入
        log.info("[base]:正在对:{}元素实行输入操作".format(loc))
        element.send_keys(value)

    # 获取文本信息方法封装
    def base_get_text(self, loc):
        log.info("[base]:正在对:{}元素实行获取文本操作".format(loc))
        return self.base_find_element(loc).get_attribute('textContent')

    # 截图方法封装
    def base_get_image(self):
        log.info("[base]:断言出错，调用截图")
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 判断元素是否存在方法封装
    def base_element_is_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            log.info("[base]:{}元素查找成功，存在当前页面".format(loc))
            return True  # 代表元素存在
        except:
            log.info("[base]:{}元素查找不成功，不存在当前页面".format(loc))
            return False  # 代表元素不存在

    #  打开All Catalogs页面
    def base_open_all_catalogs(self, loc):
        self.base_find_element(loc).click()

    #  按Enter键进行搜索
    def base_keyboard_enter(self, loc):
        self.base_find_element(loc).send_keys("\ue007")

    #  下拉框选择的方法封装
    def base_drop_list_select(self, loc):
        self.base_find_element(loc).click()


