import os

# 获取要执行的用例 不执行的用例前面加上# 用例文件 caselist.txt
caseList = []
def get_caselist():
    #获取castlist.txt文件路径
    caseListFile = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "testFile",
                                "caselist.txt")
    print(caseListFile)
    with open(caseListFile, 'r') as fb:
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                caseList.append(data.replace("\n", ""))
    return  caseList