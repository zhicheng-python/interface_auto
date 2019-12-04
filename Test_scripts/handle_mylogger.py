#encoding:utf-8
#author:wangzhicheng
#time:2019/11/22 14:26
#file:handle_mylogger.py

import logging
from Test_scripts.handle_path import do_path
from Test_scripts.handle_read_config import do_read_yaml

class MyLogger:
    """获取log"""

    def __init__(self,log_path=do_path.log_path): # 构造函数中参数化数据
        self.path=log_path
        self.fmt=do_read_yaml.read_config("mylogger","fmt")
        self.logname=do_read_yaml.read_config("mylogger","logname")
        self.datefmt=do_read_yaml.read_config("mylogger","datefmt")
        self.output_level=do_read_yaml.read_config("mylogger","output_level")
        self.collect_level=do_read_yaml.read_config("mylogger","collect_level")


    def mylogger(self):

        logger=logging.getLogger(self.logname) #创建日志收集器
        logger.setLevel(self.collect_level) # 设置日志收集器的log收集级别

        sh=logging.StreamHandler() #创建日志管理器---输出日志到控制台
        sh.setLevel(self.output_level) #设置日志管理器的log输出级别

        fh=logging.FileHandler(filename=self.path,encoding="utf8") #创建日志管理器---输出日志到指定路径
        fh.setLevel(self.output_level) #设置日志管理器的log输出级别

        formatter=logging.Formatter(fmt=self.fmt,datefmt=self.datefmt) #设置日志输出的格式

        sh.setFormatter(formatter) #设置sh管理器日志输出格式
        fh.setFormatter(formatter) #设置fh管理器日志输出格式

        logger.addHandler(sh) #日志收集器添加指定日志管理器
        logger.addHandler(fh)

        return logger


logger=MyLogger().mylogger()


if __name__ == '__main__':
    logger.info("这是一条 info 信息")

