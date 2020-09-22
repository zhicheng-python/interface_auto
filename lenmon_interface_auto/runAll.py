# encoding:utf-8
# author:wangzhicheng
# time:2019/11/22 9:59
# file:runAll.py


import os
import unittest
from my_Libs import HTMLTestRunnerNew
from Test_scripts.handle_path import do_path

from Test_scripts.handle_user import do_creat_new_user


# 如果 没有 new_user.yaml 配置文件就先创建一个，需要在 导入 handle_read_config 之前创建
if not os.path.exists(do_path.new_user_path):
    do_creat_new_user.generage_user_info()


from Test_scripts.handle_read_config import do_read_yaml



class RunAll:

    def run_all(self):
        suite = unittest.TestSuite()

        loader = unittest.TestLoader()

        suite.addTest(loader.discover(do_path.cases_dir))
        # suite.addTest(loader.loadTestsFromTestCase(TestRegister))

        with open(do_path.report_path, "wb") as f:
            runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, tester=do_read_yaml.read_config("report", "tester"),
                                                      title=do_read_yaml.read_config("report", "title"))
            runner.run(suite)


if __name__ == '__main__':

    if not os.path.exists(do_path.new_user_path):
        do_creat_new_user.generage_user_info()

    RunAll().run_all()
