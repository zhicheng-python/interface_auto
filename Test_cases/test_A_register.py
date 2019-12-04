# encoding:utf-8
# author:wangzhicheng
# time:2019/11/22 18:56
# file:test_A_register.py


import unittest
from my_Libs import ddt_obj
from Test_scripts.handle_excel import do_excel
from Test_scripts.handle_mylogger import logger
from Test_scripts.handle_requests import HttpRequests
from Test_scripts.handle_params import do_handle_params
from Test_scripts.handle_read_config import do_read_yaml
from Test_scripts.handle_write_config import do_write_yaml


@ddt_obj.ddt
class TestRegister(unittest.TestCase):
    """注册接口测试用例"""

    data = do_excel.get_data_obj()  # 测试数据

    @classmethod
    def setUpClass(cls):
        cls.do_requests = HttpRequests()
        # cls.do_requests.add_headers(do_read_yaml.read_config("requests", "headers"))

    @classmethod
    def tearDownClass(cls):
        cls.do_requests.close()

    @ddt_obj.data(*data)
    def test_register(self, item):
        logger.info(f"正在执行{item.api}接口的第{item.case_id}条测试用例--{item.title}")

        new_method = item.method

        new_url = do_read_yaml.read_config("requests", "url") + item.url

        new_data = eval(do_handle_params.handle_params(item.data))

        if item.title == "缺少必要的请求头":  # 为测试用例缺少必要的请求头准备
            headers = None
        else:
            headers = do_read_yaml.read_config("requests", "headers")

        result = self.do_requests.http_requests(method=new_method, url=new_url, data=new_data, headers=headers)

        row = item.case_id + 1
        column = do_excel.get_title().index(do_read_yaml.read_config("excel", "result_column")) + 1
        actul_column = do_excel.get_title().index(do_read_yaml.read_config("excel", "actul_column")) + 1

        pass_value = do_read_yaml.read_config("excel", "pass_value")
        fail_value = do_read_yaml.read_config("excel", "fail_value")

        try:
            self.assertEqual(eval(item.expected)["code"], result.json()["code"])
        except AssertionError as e:
            logger.error(f"正在执行{item.api}接口的第{item.case_id}条测试用例--{item.title}执行失败，异常为{e}")
            do_excel.write_data(row, column, fail_value)
            raise e
        else:
            logger.info(f"测试用例执行成功--{item.title}")
            do_excel.write_data(row, column, pass_value)
        finally:
            # 写入测试实际结果
            do_excel.write_data(row, actul_column, result.text)

            # 设置单元格背景颜色
            do_excel.write_color()
