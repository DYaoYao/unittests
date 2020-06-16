import os
import time

import xlrd
import xlwt

from common import readConfig

localReadConfig = readConfig.ReadConfig()

def copyExcelCase():

    excel_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                              localReadConfig.get_db("excel_path"))
    excel1 = xlrd.open_workbook(excel_path, encoding_override="utf-8")

    curtime = time.strftime("%Y%m%d-%H%M%S")
    #储存路径
    save_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'excelReport',curtime+'.xls')

    #获取原来的sheets
    sheets = excel1.sheets()
    sheets_name = excel1.sheet_names()

    # 新建excel
    xls = xlwt.Workbook(encoding='utf-8')

    for sheet in sheets_name:
        sht1 = xls.add_sheet(sheet)
        for rows in range(excel1.sheet_by_name(sheet).nrows):
            for cols in range(excel1.sheet_by_name(sheet).ncols):
                sht1.write(rows, cols, excel1.sheet_by_name(sheet).cell_value(rows, cols))

    xls.save(save_path)


#copyExcelCase()



