# authon:  Administrator
# __date__:  2019/11/22
# __time__:  23:15
# __file__:  handle_user.py

from Test_scripts.handle_path import do_path
from Test_scripts.handle_phone import do_phone
from Test_scripts.handle_requests import HttpRequests
from Test_scripts.handle_read_config import do_read_yaml
from Test_scripts.handle_write_config import do_write_yaml


class CreatNewUser:

    def creat_new_user(self, regname, pwd="11111111", type=1):
        # 给定 data，参数化
        new_data = {"mobile_phone": do_phone.get_no_register_phone(), "pwd": pwd, "reg_name": regname, "type": type}

        do_requests = HttpRequests()
        do_requests.add_headers(do_read_yaml.read_config("requests", "headers"))  # 添加请求头

        # 发起请求
        res = do_requests.http_requests(method="post",
                                        url=do_read_yaml.read_config("requests", "url") + "/member/register",
                                        data=new_data)

        # 构造用户数据，目的就是获取此数据
        value = {regname: {"用户ID": res.json()["data"]["id"], "手机号": new_data["mobile_phone"], "密码": new_data["pwd"]}}

        # 关闭请求
        do_requests.close()

        return value

    def generage_user_info(self):
        # 把构造的三个用户数据存放在一个字典中，写入配置文件
        user_info_dict = {}

        user_info_dict.update(self.creat_new_user(regname="管理人", type=0))
        user_info_dict.update(self.creat_new_user(regname="借款人"))
        user_info_dict.update(self.creat_new_user(regname="投资人"))

        do_write_yaml.write_config(datas=user_info_dict, path=do_path.new_user_path)


do_creat_new_user = CreatNewUser()

if __name__ == '__main__':
    do_creat_new_user.generage_user_info()
