# encoding:utf-8
# author:wangzhicheng
# time:2019/11/22 18:29
# file:handle_phone.py


import random

from Test_scripts.handle_mysql import do_mysql


class NoRegisterPhone:

    def __init__(self):
        pass

    def create_phone(self):  # 随机生成一个手机号

        phone_head = random.choice(["130", "131", "138", "139", "150", "187", "188", "189"])

        phone_body = "".join(random.sample("0123456789", 8))  # random.sample(序列，次数)

        phone = phone_head + phone_body

        return phone

    def get_no_register_phone(self):

        while True:

            phone = self.create_phone()

            if not do_mysql.read_mysql(args=phone):  # 生成的手机号传进数据库进行校验，有返回值说明已注册
                break

        do_mysql.close()  # 关闭数据库及游标

        return phone


do_phone = NoRegisterPhone()

if __name__ == '__main__':
    phone = do_phone.get_no_register_phone()
    print(phone)
