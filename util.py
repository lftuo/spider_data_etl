#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-11-3 16:29:40
# @File : util.py
# @Software : IntelliJ IDEA
import ConfigParser

import MySQLdb


class Util(object):
    def read_config(self):
        config = ConfigParser.ConfigParser()
        config.read("conf/config.ini")
        return config
    '''
    获取MySQL数据库连接
    '''
    def get_db_conn(self):
        config = self.read_config()
        host_name = config.get("MySQL","MYSQL_HOST")
        db_name = config.get("MySQL","MYSQL_DBNAME")
        user_name = config.get("MySQL","MYSQL_USER")
        password = config.get("MySQL","MYSQL_PASSWD")
        port = int(config.get("MySQL","PORT"))
        charset = config.get("MySQL","CHARSET")
        conn = MySQLdb.connect(host=host_name, user=user_name, passwd=password, db=db_name, port=port, charset=charset)
        return conn
