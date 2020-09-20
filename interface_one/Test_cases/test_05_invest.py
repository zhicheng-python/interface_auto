# encoding:utf-8
# author:wangzhicheng
# time:2019/12/5 10:43
# file:test_05_invest.py


import unittest
from MyLibs import ddt_obj
from Test_scripts.handle_yaml import do_yaml
from Test_scripts.handle_logger import logger
from Test_scripts.handle_excel import ReadExcel
from Test_scripts.handle_mysql import ReadMysql
from Test_scripts.handle_params import do_params
from Test_scripts.handle_params import HandleParams
from Test_scripts.handle_requests import ReadRequests

do_excel = ReadExcel(sheet_name=do_yaml.read_yaml("excel", "sheet_name_invest"))

token = {}


@ddt_obj.ddt
class TestInvest(unittest.TestCase):
    """投资接口测试用例"""

    @classmethod
    def setUpClass(cls):
        print("测试用例开始执行---")
        cls.do_requests = ReadRequests()
        cls.do_mysql = ReadMysql()

    @classmethod
    def tearDownClass(cls):
        print("测试用例执行结束---")
        cls.do_requests.close()
        cls.do_mysql.close()

    # 获取数据
    datas = do_excel.get_data_obj()

    @ddt_obj.data(*datas)
    def test_invest(self, item):
        logger.info(f"正在执行{item.api}接口的第{item.case_id}条测试用例，用例标题：{item.title}")
        global token

        # 拼接后的最终url
        new_url = do_yaml.read_yaml("requests", "url") + item.url
        # excel中读取的请求方式
        new_method = item.method
        # 处理转化后的最终数据
        new_data = do_params.read_params(item.datas)
        # eval转化后的期望值
        new_expected = eval(item.expected)

        new_headers = do_yaml.read_yaml("requests", "headers")
        new_headers.update(token)

        # if getattr(TestInvest,"token"):
        #     new_headers.update(getattr(TestInvest,"token"))

        # http请求
        res = self.do_requests.read_requests(url=new_url, method=new_method, data=new_data, headers=new_headers)

        # 写回测试结果的行数
        row = item.case_id + 1
        # 写回测试结果的列数
        column = do_excel.get_title().index("result") + 1
        # 写回测试实际结果的列数
        actul_column = do_excel.get_title().index("actul") + 1

        try:
            self.assertEqual(new_expected["code"], res.json()["code"])

        except AssertionError as e:
            logger.error(f"{item.api}接口的第{item.case_id}条测试用例执行失败，用例标题：{item.title}，异常为:{e}")
            # 写回测试结果
            do_excel.write_data(row, column, do_yaml.read_yaml("excel", "fail_result"))
            raise e

        else:
            logger.error(f"{item.api}接口的第{item.case_id}条测试用例执行成功，用例标题：{item.title}!")
            do_excel.write_data(row, column, do_yaml.read_yaml("excel", "pass_result"))

            # 如果加标成功，设置类属性值
            if "加标成功" in item.title:
                loan_id=res.json().get("data").get("id")
                # loan_id = str(self.do_mysql.read_mysql(sql=do_yaml.read_yaml("mysql","loan_id_sql")))
                setattr(HandleParams, "loan_id", loan_id)

            if "正常登录" in item.title:
                token_info = res.json().get("data").get("token_info").get("token")

                token["Authorization"] = "Bearer " + token_info
                # setattr(TestInvest,"token",new_token)



        finally:
            # 写回实际结果：
            do_excel.write_data(row, actul_column, res.text)
            # 设置单元格颜色：
            do_excel.write_color()
