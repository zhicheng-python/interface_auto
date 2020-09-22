# authon:  Administrator
# __date__:  2019/11/24
# __time__:  16:42
# __file__:  test_D_add.py

import unittest
from my_Libs import ddt_obj
from Test_scripts.handle_mysql import do_mysql
from Test_scripts.handle_excel import ReadExcel
from Test_scripts.handle_mylogger import logger
from Test_scripts.handle_requests import HttpRequests
from Test_scripts.handle_params import do_handle_params
from Test_scripts.handle_read_config import do_read_yaml

do_excel = ReadExcel(sheet_name=do_read_yaml.read_config("excel", "sheet4_name"))

token = {}


@ddt_obj.ddt
class TestAdd(unittest.TestCase):
    """加标接口测试用例"""

    data = do_excel.get_data_obj()  # 测试数据

    @classmethod
    def setUpClass(cls):
        cls.do_requests = HttpRequests()
        # cls.do_requests.add_headers(do_read_yaml.read_config("requests", "headers"))

    @classmethod
    def tearDownClass(cls):
        cls.do_requests.close()

    @ddt_obj.data(*data)
    def test_add(self, item):

        global token  # 声明全局变量

        logger.info(f"正在执行{item.api}接口的第{item.case_id}条测试用例--{item.title}")

        # 最终的url地址
        new_url = do_read_yaml.read_config("requests", "url") + item.url

        # 经过转化的最终数据
        new_data = do_handle_params.handle_params(item.data)

        # 添加请求头
        if item.title == "缺少必要的请求头":  # 为测试用例缺少必要的请求头准备
            headers = None
        else:
            headers = do_read_yaml.read_config("requests", "headers")

        # 请求头中添加token
        headers.update(token)

        if " 充值成功" in item.title:
            # 获取充值前金额：
            self.before_value = float(
                do_mysql.read_mysql(do_read_yaml.read_config("mysql", "recharge_sql"), phone=item.data["mobile_phone"])[
                    "leave_amount"])
            do_mysql.close()

        # 发起请求
        result = self.do_requests.http_requests(method=item.method, url=new_url, data=new_data, headers=headers)

        if " 充值成功" in item.title:
            # 获取充值后金额：
            after_value = float(
                do_mysql.read_mysql(do_read_yaml.read_config("mysql", "recharge_sql"), phone=item.data["mobile_phone"])[
                    "leave_amount"])
            try:
                self.assertEqual(eval(item.data)["amount"], float(after_value) - float(self.before_value))
            except AssertionError as e:
                logger.error(f"充值后，数据库中数据异常!{e}")
                raise e
            do_mysql.close()

        row = item.case_id + 1
        column = do_excel.get_title().index(do_read_yaml.read_config("excel", "result_column")) + 1
        actul_column = do_excel.get_title().index(do_read_yaml.read_config("excel", "actul_column")) + 1

        pass_value = do_read_yaml.read_config("excel", "pass_value")
        fail_value = do_read_yaml.read_config("excel", "fail_value")

        try:
            self.assertEqual(eval(item.expected)["code"], result.json()["code"])
            self.assertEqual(eval(item.expected)["msg"], result.json()["msg"])
        except AssertionError as e:
            logger.error(f"正在执行{item.api}接口的第{item.case_id}条测试用例--{item.title}执行失败，异常为{e}")
            do_excel.write_data(row, column, fail_value)
            raise e
        else:
            logger.info(f"测试用例执行成功--{item.title}")
            do_excel.write_data(row, column, pass_value)

        finally:
            do_excel.write_data(row, actul_column, result.text)
            do_excel.write_color()

        # 如果是正常登录用例,则更新到全局变量token中
        if "正常登录" in item.title:
            token["Authorization"] = "Bearer " + result.json()["data"]["token_info"]["token"]
            # cls.do_requests.add_headers({"Authorization":"Bearer " + result.json()["data"]["token_info"]["token"]})
