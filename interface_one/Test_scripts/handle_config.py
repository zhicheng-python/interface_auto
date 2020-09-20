# encoding:utf-8
# author:wangzhicheng
# time:2019/11/27 11:04
# file:handle_config.py

from configparser import ConfigParser
from Test_scripts.handle_path import do_path


class ReadWriteConfig:
    # 读配置文件
    def read_config(self, section, option, path=do_path.read_config_path):
        # 创建 config对象
        config = ConfigParser()  # 不放在 init 构造函数中，是因为读配置文件和写配置文件最好不用同一个config 对象
        # 读取配置文件（打开配置文件）
        config.read(path, encoding="utf8")
        # 返回数据
        return config.get(section,option)
        # return config[section][option]

    # 写入配置文件
    def write_config(self, data, path=do_path.write_config_path):
        # 创建 config对象
        config = ConfigParser()
        # 将内容写入文件中
        with open(file=path, mode="w", encoding="utf8") as f:
            # data是一个字典嵌套字典 类型数据，遍历data,循环给config 赋值：config[key]=data[key]
            for k in data:
                config[k] = data[k]
            # 将赋完值的config对象写入文件中
            config.write(f)


do_config = ReadWriteConfig()

if __name__ == '__main__':

    print(do_config.read_config("Test", "test"))

    data = {"Test": {"test": "我是帅gege!"}}

    do_config.write_config(data)
