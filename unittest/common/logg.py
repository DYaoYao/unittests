import logging
import os

# 报告存放目录
import time
path = "../log/"

class Log:
    def __init__(self):
        # 父级的父级目录
        #parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        #当前时间
        curtime = time.strftime('%Y-%m-%d')
        #日志存放目录
        if not os.path.exists(path):
            os.mkdir(path)

        self.logpath = os.path.join(path, curtime + ".log")

    def get_log(self,level,msg):
        #创建日志收集器
        logger = logging.getLogger()
        logger.setLevel('DEBUG')
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logpath,encoding='utf-8')
        fh.setLevel('INFO')
        # 创建一个handler，用于将日志输出到控制台
        #清理
        logger.handlers.clear()
        ch = logging.StreamHandler()
        ch.setLevel('INFO')
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-日志信息:%(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)

        if level == "DEBUG":
            logger.debug(msg)
        elif level == "INFO":
            logger.info(msg)
        elif level == "WARNING":
            logger.warning(msg)
        elif level == "ERROR":
            logger.error(msg)
        elif level == 'CRITICAL':
            logger.critical(msg)


    def log_debug(self,msg):
        self.get_log("DEBUG",msg)
    def log_info(self,msg):
        self.get_log("INFO",msg)

    def log_warning(self, msg):
        self.get_log('WARNING', msg)

    def log_error(self, msg):
        self.get_log('ERROR', msg)

    def log_critical(self, msg):
        self.get_log('CRITICAL', msg)









