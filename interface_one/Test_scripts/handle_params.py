# encoding:utf-8
# author:wangzhicheng
# time:2019/11/29 19:22
# file:handle_params.py

import re

from Test_scripts.handle_yaml import do_yaml
from Test_scripts.handle_path import do_path
from Test_scripts.handle_phone import do_phone


class HandleParams:

    @classmethod
    def register_params(cls, data):
        """注册接口测试数据替换"""

        if "{no_register_phone}" in data:
            data = re.sub(r"{no_register_phone}", str(do_phone.get_no_register_phone()), data)

        if "{exist_phone}" in data:
            data = re.sub(r"{exist_phone}", str(do_yaml.read_yaml("借款人", "手机号", do_path.write_yaml_path)), data)

        if "{exist_pwd}" in data:
            data = re.sub(r"{exist_pwd}", str(do_yaml.read_yaml("借款人", "密码", do_path.write_yaml_path)), data)

        return data

    @classmethod
    def invest_params(cls, data):
        """投资接口测试数据替换"""

        if "{borrower_phone}" in data:
            data = re.sub(r"{borrower_phone}", str(do_yaml.read_yaml("借款人", "手机号", path=do_path.write_yaml_path)),
                          data)
        if "{borrower_pwd}" in data:
            data = re.sub(r"{borrower_pwd}", str(do_yaml.read_yaml("借款人", "密码", path=do_path.write_yaml_path)),
                          data)
        if "{borrower_id}" in data:
            data = re.sub(r"{borrower_id}", str(do_yaml.read_yaml("借款人", "用户ID", path=do_path.write_yaml_path)),
                          data)

        if "{admin_phone}" in data:
            data = re.sub(r"{admin_phone}", str(do_yaml.read_yaml("管理人", "手机号", path=do_path.write_yaml_path)),
                          data)
        if "{admin_pwd}" in data:
            data = re.sub(r"{admin_pwd}", str(do_yaml.read_yaml("管理人", "密码", path=do_path.write_yaml_path)),
                          data)

        if "{invest_phone}" in data:
            data=re.sub(r"{invest_phone}",str(do_yaml.read_yaml("投资人", "手机号", path=do_path.write_yaml_path)),data)

        if "{invest_pwd}" in data:
            data=re.sub(r"{invest_pwd}",str(do_yaml.read_yaml("投资人", "密码", path=do_path.write_yaml_path)),data)
        if "{invest_id}" in data:
            data=re.sub(r"{invest_id}",str(do_yaml.read_yaml("投资人", "用户ID", path=do_path.write_yaml_path)),data)

        if "{loan_id}" in data:
            data=re.sub(r"{loan_id}",str(getattr(cls,"loan_id")),data)

        return data



    def read_params(self, data):

        data = self.register_params(data)
        data = self.invest_params(data)

        return data


do_params = HandleParams()


if __name__ == '__main__':
    pass
