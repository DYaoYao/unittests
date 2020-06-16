import json
import random
import re
import time

from common import readConfig

localReadConfig = readConfig.ReadConfig()


#将请求中的时间、随机数参数更换成自定义的参数
def paramfun(param_dict):

    param_key = param_dict.keys()
    param_date = {
        "bussNo": str(int(round(time.time() * 1000))) + ''.join(str(random.choice(range(10))) for _ in range(16)),
        "bussNo2":time.strftime("%Y%m%d%H%M%S")+''.join(str(random.choice(range(10))) for _ in range(6)),
        "date": time.strftime("%Y%m%d"),
        "time": time.strftime("%H%M%S"),
        "userId1":localReadConfig.get_userid('userId1')
    }

    for key in param_key:
        if param_dict[key] == "$bussNo":
            param_dict[key] = param_date["bussNo"]
        elif param_dict[key] == "$bussNo2":
            param_dict[key] = param_date["bussNo2"]
        elif param_dict[key] == "$acctNo22":
            param_dict[key] = list['acctNo']
        elif param_dict[key] == "$date":
            param_dict[key] = param_date["date"]
        elif param_dict[key] == "$time":
            param_dict[key] = param_date["time"]
        elif param_dict[key] == "$userId1":
            param_dict[key] = param_date["userId1"]

        else:
            continue
    return param_dict

#将需要传给下个用例的参数设置成全局参数
def paramgloble(res,para):
    global list
    list = {}
    res1 = json.loads(res)
    if re.search(para, res):
        list[para] = res1[para]
    else:
        pass





