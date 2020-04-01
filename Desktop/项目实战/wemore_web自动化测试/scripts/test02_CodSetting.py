import unittest
from time import sleep
from lxml.doctestcompare import strip
from base.get_driver import GetDriver
from page.page_cod_setting import PageCodSetting
from page.page_login import PageLogin
from tool.read_txt import read_txt
from parameterized import parameterized


def get_data():
    arrange = []
    for data in read_txt("CodSetting.txt"):
        arrange.append(tuple(data.strip().split(",")))
    return arrange[1:]


#  定义测试类
class TestCodSetting(unittest.TestCase):
    #  定义setUp
    def setUp(self):
        #  获取driver
        self.driver = GetDriver().get_driver()
        #  实例化PageSummary页面
        self.CodSetting = PageCodSetting(self.driver)
        #  调用成功登录依赖
        PageLogin(self.driver).page_login_success()
        #  调用打开打开All Catalogs页面方法
        self.CodSetting.page_CodSetting_all_catalogs()

    #  定义tearDown
    def tearDown(self):  
        #  关闭浏览器驱动
        GetDriver.quit_driver()

    #  定义测试summary日期查询方法
    @parameterized.expand(get_data())
    def test_CodSetting(self, catalog_name, money, expect_result):
        #  调用组合业务方法
        self.CodSetting.page_CodSetting(catalog_name, money)
        #  获取错成功提示信息
        msg = self.CodSetting.page_CodSetting_view_cod_charge()
        print("msg:", msg)
        # self.assertEqual(strip(msg), expect_result)
