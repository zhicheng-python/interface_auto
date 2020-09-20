#encoding:utf-8
#author:wangzhicheng
#time:2019/11/28 10:35
#file:handle_mysql.py

import pymysql
from Test_scripts.handle_yaml import do_yaml
class ReadMysql:

    def __init__(self):

        config=do_yaml.read_yaml("mysql","config")
        #连接数据库
        self.cnn=pymysql.connect(**config)
        #创建游标
        self.cursor=self.cnn.cursor(cursor=pymysql.cursors.DictCursor)

    def read_mysql(self,sql,args=None,is_less=True):
        #执行sql语句
        self.cursor.execute(sql,args)
        #提交
        self.cnn.commit()

        #如果查询的单条数据用fetchone，多条用fetchall
        if is_less:
            value=self.cursor.fetchone()
        else:
            value=self.cursor.fetchall()
        return value

    def close(self):
        #先关闭游标
        self.cursor.close()
        #再关闭数据库
        self.cnn.close()


if __name__ == '__main__':

    do_mysql=ReadMysql()
    value=do_mysql.read_mysql(sql=do_yaml.read_yaml("mysql","sql"),args=[13888888888])
    do_mysql.close()
    print(value)




