import unittest
from lxml.doctestcompare import strip
from base.get_driver import GetDriver
from page.page_login import PageLogin
from parameterized import parameterized
from tool.read_txt import read_txt
from base.get_logger import GetLogger


#  获取log日志器
log = GetLogger().get_logger()


def get_data():
    arrange = []
    for data in read_txt("login.txt"):
        arrange.append(tuple(data.strip().split(",")))
    return arrange[1:]


#  新建测试类并继承unittest.TestCase
class TestLogin(unittest.TestCase):
    #  新建setUp
    def setUp(self):
        try:
            #  实例化并获取driver
            self.driver = GetDriver().get_driver()
            #  实例化获取PageLogin()
            self.login = PageLogin(self.driver)
        except Exception as e:
            log.error("出错：{}".format(e))
            #  截图
            self.login.base_get_image()

    #  新建tearDown
    def tearDown(self):
        try:
            #  关闭浏览器驱动
            GetDriver.quit_driver()
        except Exception as e:
            log.error("出错：{}".format(e))
            #  截图
            self.login.base_get_image()

    #  新建登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, password, expect_result, positive):
        try:
            #  调用组合登录业务方法
            self.login.page_login(username, password)
            #  判断是否为正向：
            if positive == "ture":
                #  断言是否登录成功因为返回的结果是True所以用assertTrue()
                try:
                    self.assertTrue(self.login.page_if_login_success())
                except:
                    #  截图
                    self.login.base_get_image()
                    #  点击头像退出
                    self.login.page_click_person_logout()
            #  逆向用例
            else:
                #  获取错误提示信息
                msg = self.login.page_get_error_text()
                # print("msg: ", strip(msg))
                self.assertEqual(strip(msg), expect_result)
        except Exception as e:
            log.error("出错：{}".format(e))
            #  截图
            self.login.base_get_image()

