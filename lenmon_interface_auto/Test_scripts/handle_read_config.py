# encoding:utf-8
# author:wangzhicheng
# time:2019/11/22 11:27
# file:handle_read_config.py

import yaml
from Test_scripts.handle_path import do_path


class ReadConfig:
    """读取配置文件"""
    def __init__(self,path=do_path.config_path): #构造函数中打开配置文件，yaml.load 读取内容

        with open(file=path,encoding="utf8") as f:

            self.data=yaml.full_load(f)
            # self.data=yaml.load(f,Loader=yaml.FullLoader)


    def read_config(self,section,option):
        #调用此函数时，返回配置文件中数据
        return self.data[section][option]


do_read_yaml=ReadConfig()

if __name__ == '__main__':

    print(do_read_yaml.read_config("Test","test"))


