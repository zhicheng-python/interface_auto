# encoding:utf-8
# author:wangzhicheng
# time:2019/11/22 13:48
# file:handle_mysql.py


import pymysql
from Test_scripts.handle_read_config import ReadConfig
from Test_scripts.handle_read_config import do_read_yaml


class ReadMysql:
    """读取数据库"""

    def read_mysql(self, sql=do_read_yaml.read_config("mysql", "sql"), args=None, is_less=True):

        config = do_read_yaml.read_config("mysql", "config")

        self.cnn = pymysql.connect(**config)  # 连接数据库

        self.cursor = self.cnn.cursor(pymysql.cursors.DictCursor)  # 设置游标，输出内容是字典形式

        self.cursor.execute(sql, args)

        self.cnn.commit()  # 执行后提交

        if is_less:  # 如果sql语句查询单条记录，则用fetchone，查询多条用fetchall
            value = self.cursor.fetchone()
        else:
            value = self.cursor.fetchall()

        return value

    def close(self):  # 关闭游标，关闭数据库连接，单独用实例函数，数据库使用结束后记得调用关闭

        self.cursor.close()  # 关闭游标
        self.cnn.close()  # 关闭数据库


do_mysql = ReadMysql()

if __name__ == '__main__':

    # value = do_mysql.read_mysql(args="13888888888")
    # print(value)
    # print(do_read_yaml.read_config("mysql","sql_no_exist_id"))
    #
    # value=do_mysql.read_mysql(do_read_yaml.read_config("mysql","sql_no_exist_id"))
    # # value=do_mysql.read_mysql(sql="SELECT id FROM member ORDER BY id DESC LIMIT 0,1;")
    # print(value,type(value))
    #
    # print(str(do_mysql.read_mysql(ReadConfig().read_config("mysql", "sql_no_exist_loan_id")["id"]))
    value=do_mysql.read_mysql(ReadConfig().read_config("mysql", "sql_no_exist_loan_id"))["id"]
    print(value)

    # do_mysql.close()
