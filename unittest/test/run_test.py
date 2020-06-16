import os
import unittest
import time

from common.copyExcelCase import copyExcelCase
from common.getCaseList import get_caselist
from HTMLTestRunner import HTMLTestRunner
from common import readConfig
from common.sendEmail import sendEmail

localReadConfig = readConfig.ReadConfig()

class TestRun():

    # 在当前目录获取需要执行的用例加载到suite中

    def get_cases(self):
        test_dir = './'
        suite_module = []
        suite = unittest.TestSuite()
        caseList = get_caselist()

        for case in caseList:
            discover = unittest.defaultTestLoader.discover(test_dir, pattern=case, top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:
            for suit in suite_module:
                for test_name in suit:
                    suite.addTest(test_name)
            return suite

if __name__ == '__main__':


    #复制测试用例
    copyExcelCase()
    #获取用例集
    suite = TestRun().get_cases()
    #生成报告
    time = time.strftime("%Y%m%d-%H%M%S")
    report_title = u"接口测试报告"
    desc = u"自动化接口测试报告详情："
    # 报告存放目录
    path = "../report/"
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        pass
    filename = path + time + ".html"
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title=report_title, description=desc, verbosity=2)
        runner.run(suite)
        fp.close()
    #发送邮件，传入报告目录
    sendEmail(path)

