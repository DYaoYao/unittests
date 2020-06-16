import unittest

from common.addExcelResult import addExcelResult

from common.getHttp import getHttp, getLog

import json
from common import readConfig
from common.getExcelCase import get_excelCase
from common.getHttp import getHttp
from common.paramfun import paramfun, paramgloble

localReadConfig = readConfig.ReadConfig()

sheetName = 'recharge'

'''
class Recharge(unittest.TestCase):
    def check(self, num):
        # 获num条用例的用例的数据
        name, host, url, method, header, param, check, index = get_excelCase(sheetName, num)
        # 将excel读取出来的参数转换成字典
        # 将参数的时间、随机数等使用函数paramfun（）特殊处理
        param_new = paramfun(json.loads(param))
        getLog.log_info("开始验证第" + str(num) + "条用例：" + name)
        try:
            res = getHttp(host, url, method, header,param_new,num)
        except Exception as e:
            getLog.log_info(e)
        if res.status_code == 200:
            if check in res.text:
                getLog.log_info("第" + str(num) + "条用例验证成功！服务器响应：" + str(res.status_code) + res.text)
                flag = 'SUCCESS'
                addExcelResult(index, num, flag,res.text)
            else:
                getLog.log_info("第" + str(num) + "条用例验证失败！服务器响应：" + str(res.status_code) + res.text)
                flag = 'FAIL'
                addExcelResult(index, num, flag, res.text)
        else:
            getLog.log_info("第" + str(num) + "条用例执行失败！服务器响应：" + str(res.status_code) + res.text)
            flag = 'FAIL'
            addExcelResult(index, num, flag, res.text)
        getLog.log_info("第" + str(num) + "条用例验证完成")
        self.assertIn(check, res.text)
    def test_01(self):
        # 测试第一条用例
        num = 1
        self.check(num)

    def test_02(self):
        # 测试第二条用例
        num = 2
        self.check(num)

'''

class Recharge(unittest.TestCase):

    #def __init__(self, *args, **kwargs):
     #   unittest.TestCase.__init__(self, *args, **kwargs)
    '''
    def setUp(self):
        print('这是每条用例的开始前的准备工作')

    def tearDown(self):
        print("这是每条用例的结束后的清理工作")
    def setUpClass(self):
        print('这是全部用例的开始前的准备工作')
    def tearDownClass(self):
        print("这是全部用例的结束后的清理工作")
    '''

    def check(self, num,par = ''):
        # 调用函数get_excelCase（）获第num条用例的用例的数据，比如接口，参数等
        name, host, url, method, header, param, check, index = get_excelCase(sheetName, num)
        # 将参数内的时间戳、随机数等需要处理的数据使用函数paramfun（）特殊处理
        param_new = paramfun(json.loads(param))
        getLog.log_info("开始验证第" + str(num) + "条用例：" + name)
        try:
            #调用函数getHttp（）获取接口返回结果
            res = getHttp(host, url, method, header,param_new,num)
        except Exception as e:
            getLog.log_info(e)
        if res.status_code == 200:
            if check in res.text:
                getLog.log_info("第" + str(num) + "条用例验证成功！服务器响应：" + str(res.status_code) + res.text)
                #判断参数长度是否大于0，大于0表示有传入参数，则将结果和需要提取的参数传给paramgloble（）函数，提取值设置成全局变量，
                if len(par) > 0:
                    paramgloble(res.text, par)
                flag = 'SUCCESS'
                #将失败或者成功的结果和服务器返回结果写入测试用例excel中
                addExcelResult(index, num, flag,res.text)
            else:
                getLog.log_info("第" + str(num) + "条用例验证失败！服务器响应：" + str(res.status_code) + res.text)
                flag = 'FAIL'
                addExcelResult(index, num, flag, res.text)
        else:
            getLog.log_info("第" + str(num) + "条用例执行失败！服务器响应：" + str(res.status_code) + res.text)
            flag = 'FAIL'
            addExcelResult(index, num, flag, res.text)
        getLog.log_info("第" + str(num) + "条用例验证完成")
        #断言
        self.assertIn(check, res.text)
    def test_01(self):
        # 测试第一条用例,num表示excel第一条用例，par表示返回结果中需要提取出来的值
        num = 1
        par = 'acctNo'
        self.check(num,par)

    def test_02(self):
        # 测试第二条用例
        num = 2
        self.check(num)