#encoding:utf-8
#author:wangzhicheng
#time:2019/11/22 11:41
#file:handle_write_config.py


import yaml
from Test_scripts.handle_path import do_path


class WriteConfig:
    """写入配置文件"""

    @staticmethod
    def write_config(datas,path=do_path.write_config_path):

        with open(file=path,mode="w",encoding="utf8") as f:
            # yaml.dump写入配置文件，allow_unicode=True，中文写入是显示中文
            yaml.dump(data=datas,stream=f,allow_unicode=True)



do_write_yaml=WriteConfig()

if __name__ == '__main__':

    datas={"Test":{"test":"test_11_22"}}

    do_write_yaml.write_config(datas)


