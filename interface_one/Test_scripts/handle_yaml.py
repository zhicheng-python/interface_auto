#encoding:utf-8
#author:wangzhicheng
#time:2019/11/27 11:04
#file:handle_yaml.py.py

import yaml
from Test_scripts.handle_path import do_path


class ReadWriteYaml:

    @staticmethod
    def read_yaml(section,option,path=do_path.read_yaml_path):

        with open(file=path,encoding="utf8") as f:
            value=yaml.load(f,Loader=yaml.FullLoader)
            value_1=yaml.full_load(f)
        # return value,value.get(section,option)
        return value[section][option]


    @staticmethod
    def write_yaml(data,path=do_path.write_yaml_path):
        with open (file=path,mode="w",encoding="utf8") as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)



do_yaml=ReadWriteYaml()

if __name__ == '__main__':

    # do_yaml.write_yaml(data={"Test":{"test":"123H我"}})

    fmt = do_yaml.read_yaml("logging", "fmt")
    datefmt = do_yaml.read_yaml("logging", "datefmt")
    log_name = do_yaml.read_yaml("logging", "log_name")
    output_level = do_yaml.read_yaml("logging", "output_level")
    collect_level = do_yaml.read_yaml("logging", "collect_level")

    print(fmt,datefmt)





