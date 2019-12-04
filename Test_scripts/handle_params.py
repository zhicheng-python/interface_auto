# encoding:utf-8
# author:wangzhicheng
# time:2019/11/22 19:23
# file:handle_params.py


import re

from Test_scripts.handle_path import do_path
from Test_scripts.handle_phone import do_phone
from Test_scripts.handle_mysql import do_mysql
from Test_scripts.handle_excel import ReadExcel
from Test_scripts.handle_read_config import ReadConfig

do_yaml = ReadConfig(path=do_path.new_user_path)


class HandleParams:

    @classmethod
    def handle_params(cls,data):

        # 没有注册的手机号码替换
        if re.search(r"{no_register_phone}", data):
            data = re.sub(r"{no_register_phone}", str(do_phone.get_no_register_phone()), data)

        # 已存在手机号码替换
        if re.search(r"{exist_phone}", data):
            data = re.sub(r"{exist_phone}", do_yaml.read_config("管理人", "手机号"), data)

        # 已存在账号密码替换
        if re.search(r"{pwd}", data):
            data = re.sub(r"{pwd}", do_yaml.read_config("管理人", "密码"), data)

        # 投资人手机号码替换
        if re.search(r"{invest_user_tel}", data):
            data = re.sub(r"{invest_user_tel}", do_yaml.read_config("投资人", "手机号"), data)

        # 投资人密码替换
        if re.search(r"{invest_user_pwd}", data):
            data = re.sub(r"{invest_user_pwd}", do_yaml.read_config("投资人", "密码"), data)

        # 投资人ID替换
        if re.search(r"{invest_user_id}", data):
            data = re.sub(r"{invest_user_id}", str(do_yaml.read_config("投资人", "用户ID")), data)

        # 借款人手机号码替换
        if re.search(r"{borrow_user_tel}", data):
            data = re.sub(r"{borrow_user_tel}", (do_yaml.read_config("借款人", "手机号")), data)

        # 借款人ID替换
        if re.search(r"{borrow_user_id}", data):
            data = re.sub(r"{borrow_user_id}", str(do_yaml.read_config("借款人", "用户ID")), data)

        # 借款人密码替换
        if re.search(r"{borrow_user_pwd}", data):
            data = re.sub(r"{borrow_user_pwd}", (do_yaml.read_config("借款人", "密码")), data)

        # 不存在的借款人id
        if re.search(r"{no_exist_id}", data):
            id = do_mysql.read_mysql(ReadConfig().read_config("mysql", "sql_no_exist_id"))["id"] + 100

            data = re.sub(r"{no_exist_id}", str(id), data)

        # 管理员手机号码替换
        if re.search(r"{admin_user_tel}", data):
            data = re.sub(r"{admin_user_tel}", do_yaml.read_config("管理人", "手机号"), data)

        # 管理员账号密码替换
        if re.search(r"{admin_user_pwd}", data):
            data = re.sub(r"{admin_user_pwd}", do_yaml.read_config("管理人", "密码"), data)

        # load_id 替换
        if re.search(r"{loan_id}", data):
            data = re.sub(r"{loan_id}", str(getattr(cls,"loan_id")), data)



        # 不存在的标id
        if re.search(r"{not_existed_loan_id}", data):
            data = re.sub(r"{not_existed_loan_id}",
                          str(do_mysql.read_mysql(ReadConfig().read_config("mysql", "sql_no_exist_loan_id"))["id"]),
                          data)

        return data


do_handle_params = HandleParams()

if __name__ == '__main__':

    # data = '{"mobile_phone":"{no_register_phone}","pwd":"11111111"}'
    do_excel = ReadExcel(sheet_name="invest")

    datas = do_excel.get_data_obj()

    for data in datas:
        value = do_handle_params.handle_params(data.data)
        title = do_handle_params.handle_params(data.title)
        print(value)
        # print(title)
        pass
