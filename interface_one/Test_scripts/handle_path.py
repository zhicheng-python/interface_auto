#encoding:utf-8
#author:wangzhicheng
#time:2019/11/27 9:34
#file:handle_path.py


import os,datetime

new_time=datetime.datetime.strftime(datetime.datetime.now(),"%Y%m%d_%H%M%S_%a")

class ReadPath:
    """构造文件绝对路径"""

    #项目绝对路径：
    basic_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    #测试报告绝对路径：
    # report_path=os.path.join(basic_path,"Test_results","test_report",f"{new_time}_report.html")
    report_path=os.path.join(basic_path,"Test_results","test_report","report.html")
    #测试log绝对路径：
    # log_path=os.path.join(basic_path,"Test_results","log_path",f"{new_time}_log.log")
    log_path=os.path.join(basic_path,"Test_results","test_log","log.log")
    #写入config配置文件路径：
    write_config_path=os.path.join(basic_path,"Test_configs","write_config.config")
    #读取config配置文件路径：
    read_config_path=os.path.join(basic_path,"Test_configs","read_config.config")
    # 写入yaml配置文件路径：
    write_yaml_path = os.path.join(basic_path, "Test_configs", "write_yaml.yaml")
    # 读取yaml配置文件路径：
    read_yaml_path = os.path.join(basic_path, "Test_configs", "read_yaml.yaml")
    #测试数据绝对路径：
    data_path=os.path.join(basic_path,"Test_datas","test_data.xlsx")
    #测试用例的文件夹 discover 使用需要：
    cases_dir=os.path.join(basic_path,"Test_cases")



do_path=ReadPath()

if __name__ == '__main__':

    print(do_path.basic_path)
    print(do_path.cases_dir)
    print(do_path.data_path)
    print(do_path.write_config_path)
    print(do_path.log_path)
    print(do_path.report_path)

