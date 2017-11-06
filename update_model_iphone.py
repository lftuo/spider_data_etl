#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-11-6 13:58:55
# @File : update_model_iphone.py
# @Software : IntelliJ IDEA
# 更新iPhone手机model类型
from util import Util


class UpdateIphoneModel(object):
    def __update__(self,table_name):
        # 将iPhone的手机型号置空
        conn = Util().get_db_conn()
        cur = conn.cursor()
        models_sql = "select * from iphone_model"
        cur.execute(models_sql)
        models = cur.fetchall()
        for line in models:
            phone_name = line[0]
            type = line[1]
            Internal_Name = line[2]
            Identifier = line[3]
            result_sql = "select url from %s where title LIKE '%%%%%s%%%%'"%(table_name,phone_name)
            cur.execute(result_sql)
            type_results = cur.fetchall()
            for line in type_results:
                url = line[0]
                update_sql = "update %s set model = '%s' WHERE url = '%s'"%(table_name,Internal_Name+";"+Identifier,url)
                cur.execute(update_sql)
            conn.commit()


if __name__ == '__main__':
    update = UpdateIphoneModel()
    update.__update__(table_name='shouji_all_spider_data')