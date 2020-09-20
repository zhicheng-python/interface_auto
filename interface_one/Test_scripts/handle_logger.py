#encoding:utf-8
#author:wangzhicheng
#time:2019/11/28 9:56
#file:handle_logger.py

import logging
from Test_scripts.handle_path import do_path
from Test_scripts.handle_yaml import do_yaml

class MyLogger:
    """处理日志"""
    def __init__(self,path=do_path.log_path):

        self.path=path
        self.fmt=do_yaml.read_yaml("logging","fmt")
        self.datefmt=do_yaml.read_yaml("logging","datefmt")
        self.log_name=do_yaml.read_yaml("logging","log_name")
        self.output_level=do_yaml.read_yaml("logging","output_level")
        self.collect_level=do_yaml.read_yaml("logging","collect_level")

    def my_logger(self):

        #创建日志收集器
        logger=logging.getLogger(self.log_name)
        #设置日志收集器收集的日志级别
        logger.setLevel(self.collect_level)

        #创建日志管理器--输出日志到控制台
        sh=logging.StreamHandler()
        #设置日志输出级别
        sh.setLevel(self.output_level)

        #创建日志管理器--输出日志到指定文件
        fh=logging.FileHandler(filename=self.path,encoding="utf-8")
        #设置日志输出级别
        fh.setLevel(self.output_level)

        #设置输出日志格式
        formatter=logging.Formatter(fmt=self.fmt,datefmt=self.datefmt)

        #给管理器输出日志设定输出格式
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        #收集器添加指定管理器
        logger.addHandler(sh)
        logger.addHandler(fh)

        return logger


logger=MyLogger().my_logger()

if __name__ == '__main__':
    logger.info("----info----")

