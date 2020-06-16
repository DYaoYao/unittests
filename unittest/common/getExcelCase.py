import os

import xlrd
from common import readConfig

localReadConfig = readConfig.ReadConfig()




def get_excelCase(sheetname,row):

    excel_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),localReadConfig.get_db("excel_path"))

    excel = xlrd.open_workbook(excel_path, encoding_override="utf-8")
    #通过角标获取sheet
    #sheet = excel.sheet_by_index(0)
    # 通过名字获取sheet
    sheetNames = excel.sheet_names()

    sheet = excel.sheet_by_name(sheetname)

    index = sheetNames.index(sheetname)

    # 获取sheet的行数
    name = sheet.cell_value(row, 1)
    host = sheet.cell_value(row, 2)
    url = sheet.cell_value(row, 3)
    method = sheet.cell_value(row, 4)
    header = sheet.cell_value(row, 5)
    param = sheet.cell_value(row, 6)
    check = sheet.cell_value(row, 7)


    return name, host, url, method,header, param, check,index





