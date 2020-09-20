#encoding:utf-8
#author:wangzhicheng
#time:2019/11/27 9:15
#file:runAll.py

import unittest,os
from MyLibs import HTMLTestRunnerNew

from Test_scripts.handle_path import do_path

from Test_cases.test_01_register import TestrRegister
from Test_cases.test_05_invest import TestInvest
from Test_scripts.handle_new_account import do_new_user



if not os.path.exists(do_path.write_yaml_path):
    do_new_user.handle_new_user()



class RunAll:

    def run_all(self):

        suite=unittest.TestSuite()

        loader=unittest.TestLoader()

        suite.addTest(loader.loadTestsFromTestCase(TestrRegister))
        suite.addTest(loader.loadTestsFromTestCase(TestInvest))


        with open(file=do_path.report_path,mode="wb") as f:

            runner=HTMLTestRunnerNew.HTMLTestRunner(stream=f,tester="zhicheng",title="auto_api",description="详情如下：")

            runner.run(suite)


if __name__ == '__main__':

    RunAll().run_all()