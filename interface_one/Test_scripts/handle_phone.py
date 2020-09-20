# encoding:utf-8
# author:wangzhicheng
# time:2019/11/29 9:18
# file:handle_phone.py

import random

from Test_scripts.handle_yaml import do_yaml
from Test_scripts.handle_mysql import ReadMysql

class GetNoRegisterPhone:

    @staticmethod
    def creat_phone():

        #random.choice(args) args 是一个非空序列，在此序列随机抽取一个元素
        phone_head = random.choice(["130", "131", "138", "139", "150", "187", "189"])
        #random.sample(非空序列或集合，随机次数K) 在一个非空序列或者集合中，选择K个随机唯一元素
        #返回一个包含填充元素的新列表，（0 <=随机次数小于等于序列长度）；"".join()转换为字符串
        phone_body = "".join(random.sample("0123456789", 8))

        phone = phone_head + phone_body

        return phone

    def get_no_register_phone(self):

        #创建数据库类实例对象
        do_mysql=ReadMysql()

        #生成的手机号，在数据库中进行查询，如果有返回值说明已注册，没有返回值则跳出循环
        while True:
            # 获取随机生成的手机号
            phone = self.creat_phone()
            if not do_mysql.read_mysql(sql=do_yaml.read_yaml("mysql","sql"),args=[phone]):
                break

        do_mysql.close()
        return phone


do_phone=GetNoRegisterPhone()

if __name__ == '__main__':

    value=do_phone.creat_phone()
    new_phone=do_phone.get_no_register_phone()

    print(value)
    print(new_phone)