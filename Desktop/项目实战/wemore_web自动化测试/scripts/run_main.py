import unittest
import time
from tool.HTMLTestRunner import HTMLTestRunner


#  定义测试套件
suite = unittest.defaultTestLoader.discover("./")
#  报告生成目录及文件名称
dir_path = "../report/%s.html" % (time.strftime("%Y_%m_%d %H_%M_%S"))
#  获取文件流并调用run运行
with open(dir_path, "wb") as f:
    HTMLTestRunner(stream=f, title="Wemore的Web自动化测试报告", description="python语言编写").run(suite)