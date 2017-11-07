#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-11-3 15:35:17
# @File : updata_model_normal.py
# @Software : IntelliJ IDEA
# 更新爬虫数据表单shouji_all_spider_data中model字段
import logging

from util import Util
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class UpdateModel(object):

    def __update_data__(self,table_name):

        # 读取models手机型号表单
        conn = Util().get_db_conn()
        cur = conn.cursor()
        sql = "SELECT * FROM model_and_brand WHERE brand != 'NULL' AND brand_chinese IS NOT NULL ORDER BY cnt DESC LIMIT 1000"
        cur.execute(sql)
        res = cur.fetchall()
        for line in res:
            model = line[0]
            brand = line[1]
            cnt = line[2]
            brand_chinese = line[3]
            print model,brand,cnt,brand_chinese
            update.__update_model_recursion__(model,brand_chinese,table_name)

    def __update_model_recursion__(self,model,brand_chinese,table_name):
        conn = Util().get_db_conn()
        cur = conn.cursor()
        # 按照brand查找数据
        sql = "select url from %s WHERE title LIKE '%%%%%s%%%%' AND (title LIKE '%%%%%s%%%%' OR model LIKE '%%%%%s%%%%')"%(table_name,brand_chinese,model,model)
        cur.execute(sql)
        brand_res = cur.fetchall()
        # 如果找到该手机模型，则更新爬虫数据中的model
        if len(brand_res) > 0:
            for line in brand_res:
                url = line[0]
                update_sql = "update %s set model = '%s' WHERE url = '%s'"%(table_name,model,url)
                cur.execute(update_sql)
                conn.commit()
                print 'update ----- ',model,brand_chinese,url
        # 如果找不到，则区别对待
        else:
            # 去掉HUAWEI开头查找华为的手机型号
            data = open("conf/data_notfound.txt",'a')
            if model.startswith('HUAWEI '):
                new_model = model.replace('HUAWEI ','').strip()
                res = update.get_result(conn,brand_chinese,new_model)
                if len(res) > 0:
                    for line in res:
                        url = line[0]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                        print 'update ----- ',model,brand_chinese,url
                else:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('SM-'):
                # 去掉SM-开头查找三星的手机型号
                new_model = model.replace('SM-','').strip()
                res = update.get_result(conn,brand_chinese,new_model)
                if len(res) > 0:
                    for line in res:
                        url = line[0]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                        print 'update ----- ',model,brand_chinese,url
                else:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('GT-'):
                # 去掉GT-开头查找三星的手机型号
                new_model = model.replace('GT-','').strip()
                res = update.get_result(conn,brand_chinese,new_model)
                if len(res) > 0:
                    for line in res:
                        url = line[0]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                        print 'update ----- ',model,brand_chinese,url
                else:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('Coolpad '):
                # Coolpad 开头查找酷派的手机型号
                new_model = model.replace('Coolpad ','').strip()
                res = update.get_result(conn,brand_chinese,new_model)
                if len(res) > 0:
                    for line in res:
                        url = line[0]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                        print 'update ----- ',model,brand_chinese,url
                else:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('Lenovo '):
                # Lenovo 开头查找联想的手机型号
                new_model = model.replace('Lenovo ','').strip()
                res = update.get_result(conn,brand_chinese,new_model)
                if len(res) > 0:
                    for line in res:
                        url = line[0]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                        print 'update ----- ',model,brand_chinese,url
                else:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('HTC '):
                # HTC 开头查找HTC的手机型号
                new_model = model.replace('HTC ','').strip()
                res = update.get_result(conn,brand_chinese,new_model)
                if len(res) > 0:
                    for line in res:
                        url = line[0]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                        print 'update ----- ',model,brand_chinese,url
                else:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('ZTE '):
                # ZTE 开头查找中兴的手机型号
                new_model = model.replace('ZTE ','').strip()
                res = update.get_result(conn,brand_chinese,new_model)
                if len(res) > 0:
                    for line in res:
                        url = line[0]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                        print 'update ----- ',model,brand_chinese,url
                else:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('koobee '):
                # koobee 开头查找酷比的手机型号
                new_model = model.replace('koobee ','').strip()
                res = update.get_result(conn,brand_chinese,new_model)
                if len(res) > 0:
                    for line in res:
                        url = line[0]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                        print 'update ----- ',model,brand_chinese,url
                else:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('vivo '):
                # vivo 开头查找vivo的手机型号
                new_model = model.replace('vivo ','').strip()
                res = update.get_result(conn,brand_chinese,new_model)
                if len(res) > 0:
                    for line in res:
                        url = line[0]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                        print 'update ----- ',model,brand_chinese,url
                else:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('ZUK '):
                # ZUK 开头查找ZUK的手机型号
                new_model = model.replace('ZUK ','').strip()
                res = update.get_result(conn,brand_chinese,new_model)
                if len(res) > 0:
                    for line in res:
                        url = line[0]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                        print 'update ----- ',model,brand_chinese,url
                else:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            else:
                data.write(model + '---------- is not found')
                data.write('\n')

    def get_result(self,conn,brand_chinese,model):
        cur = conn.cursor()
        sql = "select url from shouji_all_spider_data WHERE title LIKE '%%%%%s%%%%' AND (title LIKE '%%%%%s%%%%' OR model LIKE '%%%%%s%%%%')"%(brand_chinese,model,model)
        # model本身是否存在该手机型号
        cur.execute(sql)
        res = cur.fetchall()
        return res


if __name__ == '__main__':
    update = UpdateModel()
    update.__update_data__(table_name='shouji_all_spider_data')
