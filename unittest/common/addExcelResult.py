import os
import time

import xlrd
import xlwt
from xlutils.copy import copy

from common import readConfig
from common.copyExcelCase import copyExcelCase

localReadConfig = readConfig.ReadConfig()

def addExcelResult(index,num,flag,res):
    #获取excel结果文件的最后一张表的名字
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"excelReport")
    xls_name = os.listdir(path)[-1]
    #拼接路径

    xlsDir = os.path.join(path,xls_name)

    sheet = xlrd.open_workbook(xlsDir)
    ws = copy(sheet)  # 复制之前表里存在的数据,# 将xlrd对象拷贝转化为xlwt对象
    sht1 = ws.get_sheet(index)
    sht1.write(0, 8, "测试结果")
    sht1.write(0, 9, "服务器返回")
    sht1.write(num,8,flag)

    sht1.write(num, 9,res)

    ws.save(xlsDir)
