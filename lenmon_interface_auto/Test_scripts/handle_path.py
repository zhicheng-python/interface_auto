# encoding:utf-8
# author:wangzhicheng
# time:2019/11/22 10:30
# file:handle_path.py


import os, datetime

# 设置时间格式
format_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%a")


class ReadPath:
    # 项目路径
    basic_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试数据路径：
    data_path = os.path.join(basic_path, "Test_datas", "test_data.xlsx")

    # 配置文件路径：
    config_path = os.path.join(basic_path, "Test_config", "read_config.yaml")

    # 写入配置文件路径：
    write_config_path = os.path.join(basic_path, "Test_config", "write_config.yaml")

    # 测试log路径：
    log_path = os.path.join(basic_path, "Test_result", "test_log", f"{format_time}_log.log")
    # log_path = os.path.join(basic_path, "Test_result", "test_log", "log.log")

    # 测试报告路径：
    report_path = os.path.join(basic_path, "Test_result", "test_report", f"{format_time}_report.html")
    # report_path = os.path.join(basic_path, "Test_result", "test_report", "report.html")

    # 测试用例文件夹
    cases_dir = os.path.join(basic_path, "Test_cases")

    # 新增用户（管理人，借款人，投资人）配置文件路径
    new_user_path = os.path.join(basic_path, "Test_config", "new_user.yaml")


do_path = ReadPath()

if __name__ == '__main__':
    print(do_path.report_path)
    print(do_path.basic_path)
