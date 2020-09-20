# encoding:utf-8
# author:wangzhicheng
# time:2019/11/29 19:12
# file:test_01_register.py


import unittest
from MyLibs import ddt_obj
from Test_scripts.handle_yaml import do_yaml
from Test_scripts.handle_logger import logger
from Test_scripts.handle_excel import do_excel
from Test_scripts.handle_params import do_params
from Test_scripts.handle_requests import ReadRequests


# ddt 数据驱动
@ddt_obj.ddt
class TestrRegister(unittest.TestCase):
    """注册接口"""

    # 获取测试数据对象
    datas = do_excel.get_data_obj()

    # 类函数，执行所有用例之前执行一次
    @classmethod
    def setUpClass(cls):
        cls.do_requests = ReadRequests()

    # 类函数，执行所有用例之后执行一次
    @classmethod
    def tearDownClass(cls):
        cls.do_requests.close()

    # ddt 数据驱动
    @ddt_obj.data(*datas)
    # 测试用例 以test 开头
    def test_register(self, item):
        # log 日志
        logger.info(f"正在执行{item.api}接口的第{item.case_id}条测试用例！--{item.title}")
        # 拼接后的url 地址
        new_url = do_yaml.read_yaml("requests", "url") + item.url
        # 转换后的最终数据
        new_data = do_params.read_params(item.datas)

        # 测试用例准备，请求头不存在,如果执行的是这条用例，则删除X-Lemonban-Media-Type
        if item.title == "请求头不存在":
            new_headers = do_yaml.read_yaml("requests", "headers")
            new_headers.pop("X-Lemonban-Media-Type")
        else:
            new_headers = do_yaml.read_yaml("requests", "headers")


        #期望值
        new_expected = eval(item.expected)

        # http请求
        res = self.do_requests.read_requests(url=new_url, method=item.method, data=new_data, headers=new_headers)

        #写入excel中需要的参数：
        row = item.case_id + 1
        column = do_excel.get_title().index("result") + 1
        pass_value = do_yaml.read_yaml("excel", "pass_result")
        fail_value = do_yaml.read_yaml("excel", "fail_result")
        actul_column = do_excel.get_title().index("actul") + 1

        #断言
        try:
            # self.assertEqual(new_expected["msg"],res.json()["msg"])
            self.assertEqual(new_expected["code"], res.json()["code"])
        except Exception as e:
            logger.info(f"执行{item.api}接口的第{item.case_id}条测试用例！--{item.title}--执行失败！")
            #执行失败则写入测试结果到excel
            do_excel.write_data(row, column, fail_value)
            logger.error(f"执行{item.api}接口的第{item.case_id}条测试用例！执行异常>>>>{e}")
            raise e
        else:
            logger.info(f"执行{item.api}接口的第{item.case_id}条测试用例！--{item.title}--执行成功！")
            #执行成功则写入测试结果到excel
            do_excel.write_data(row, column, pass_value)
        finally:
            #不论是执行成功还是失败都写入实际结果
            do_excel.write_data(row, actul_column, res.text)
            #设置背景颜色
            do_excel.write_color()
