import json

import requests

from common.logg import Log

getLog = Log()

def getHttp(host, url, method, header,param,num):

    if method == "get":
        res = requests.get(host + url,headers = json.loads(header), json=param)
        return res

    elif method == "post":
        res = requests.post(host + url,headers = json.loads(header), json=param)
        return res

    else:
        getLog.log_info("第" + str(num) + "条用例请求方式有误！！！请确认字段【Method】值是否正确，正确值为大写的GET或POST。")



