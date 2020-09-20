# encoding:utf-8
# author:wangzhicheng
# time:2019/11/29 15:12
# file:handle_new_account.py

from Test_scripts.handle_path import do_path
from Test_scripts.handle_yaml import do_yaml
from Test_scripts.handle_phone import do_phone
from Test_scripts.handle_requests import ReadRequests


class CreatNewAccount:
    new_url = "http://api.lemonban.com/futureloan/member/register"

    @staticmethod
    def creat_new_account(reg_name, url=new_url, pwd="11111111", type="1",
                          headers=do_yaml.read_yaml("requests", "headers")):
        # 创建实例对象
        do_requests = ReadRequests()
        # 添加请求头
        do_requests.addd_headers(headers)
        # 手机号码
        mobile_phone = do_phone.get_no_register_phone()
        # 参数，data
        data = {"mobile_phone": mobile_phone,
                "pwd": pwd,
                "reg_name": reg_name,
                "type": type}

        # 发起resister请求
        res = do_requests.read_requests(url, method="post", data=data)
        # 主要目的返回此格式数据
        value = {reg_name: {"用户ID": res.json()["data"]["id"], "手机号": mobile_phone, "密码": pwd}}
        # 关闭requests请求
        do_requests.close()
        return value

    def handle_new_user(self):
        # 一个空字典，update  self.creat_new_account（）返回的数据
        datas = {}
        datas.update(self.creat_new_account(reg_name="管理人", type="0"))
        datas.update(self.creat_new_account(reg_name="借款人"))
        datas.update(self.creat_new_account(reg_name="投资人"))

        # 最终格式datas>>>{{admin},{invest_user},{loan_user}}写入yaml文件中
        do_yaml.write_yaml(datas, do_path.write_yaml_path)


do_new_user = CreatNewAccount()

if __name__ == '__main__':
    # do_new_user.creat_new_account(reg_name="admin_user",type="0")
    do_new_user.handle_new_user()
