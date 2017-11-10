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
        '''
        更新iPhone手机型号表，iPhone手机型号表iphone_model，参考网页：https://www.theiphonewiki.com/wiki/Models
        实现逻辑：查找iphone_model中的phone_name字段，然后模糊匹配爬虫数据表中的title字段，匹配成功，则修改爬虫数据的model字段为iphone_model中Internal_Name与Identifier字段拼接之和
        :param table_name:爬虫数据表
        :return:
        '''

        # 将iPhone的手机型号置空
        conn = Util().get_db_conn()
        cur = conn.cursor()
        models_sql = "select * from iphone_model"
        cur.execute(models_sql)
        models = cur.fetchall()
        for line in models:
            # iPhone手机名称
            phone_name = line[0]
            # iPhone手机型号1
            Internal_Name = line[2]
            # iPhone手机型号2
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