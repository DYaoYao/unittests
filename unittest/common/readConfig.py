import configparser

import os
import codecs
import configparser


#获取配置文件的路径
configPath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "testFile","config.ini")
#proDir = os.path.split(os.path.realpath(__file__))[0]  #项目根目录地址
#configPath = os.path.join(proDir, "config.ini")   #存放在根目录下，文件名是config.ini

class ReadConfig:
    def __init__(self):
        '''
        fd = open(configPath)
        data = fd.read()
        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()
        '''
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath,encoding='utf8')

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_userid(self, name):
        value = self.cf.get("USERID", name)
        return value
    def get_sql(self, name):
        value = self.cf.get("SQL", name)
        return value
