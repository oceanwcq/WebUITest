from tool.HTMLTestRunner import HTMLTestRunner
import time
import unittest

suite = unittest.defaultTestLoader.discover('./case', pattern="test_*.py")
report_path = "./report/{}.html".format(time.strftime("%Y_%m_%d_%H_%M_%S"))
with open(report_path, "wb") as f:
    HTMLTestRunner(stream=f).run(suite)

