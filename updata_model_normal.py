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
        """
        try:
            file = open(path,'r')
            while 1:
                model = file.readline().strip('\n').strip()
                update.__update_model_recursion__(model)
                if not model:
                    break
                pass
        except Exception,e:
            logging.exception(e)
        """


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
        # 如果找不到，则区别对待
        else:
            print ''

        res_title = update.get_result(conn,model)[0]
        res_model = update.get_result(conn,model)[1]
        data = open("conf/data.txt",'a')
        print model,len(res_title),len(res_model)
        # title字段可以找到，model字段找不到，则更新model字段为model
        if len(res_title) > 0 and len(res_model) == 0:
            for line in res_title:
                url = line[2]
                update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                cur.execute(update_sql)
                conn.commit()
        elif len(res_title) == 0 and len(res_model) == 0:
            # 去掉HUAWEI开头查找华为的手机型号
            if model.startswith('HUAWEI '):
                new_model = model.replace('HUAWEI ','').strip()
                print new_model
                res_title = update.get_result(conn,new_model)[0]
                res_model = update.get_result(conn,new_model)[1]
                if len(res_title) > 0 and len(res_model) == 0:
                    data.write(model + ' ------ need update')
                    data.write('\n')
                    for line in res_title:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) > 0:
                    for line in res_model:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) == 0:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('SM-'):
                # 去掉SM-开头查找三星的手机型号
                new_model = model.replace('SM-','').strip()
                print new_model
                res_title = update.get_result(conn,new_model)[0]
                res_model = update.get_result(conn,new_model)[1]
                if len(res_title) > 0 and len(res_model) == 0:
                    for line in res_title:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) > 0:
                    for line in res_model:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) == 0:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('GT-'):
                # 去掉GT-开头查找三星的手机型号
                new_model = model.replace('GT-','').strip()
                print new_model
                res_title = update.get_result(conn,new_model)[0]
                res_model = update.get_result(conn,new_model)[1]
                if len(res_title) > 0 and len(res_model) == 0:
                    for line in res_title:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) > 0:
                    for line in res_model:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) == 0:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('Coolpad '):
                # Coolpad 开头查找酷派的手机型号
                new_model = model.replace('Coolpad ','').strip()
                print new_model
                res_title = update.get_result(conn,new_model)[0]
                res_model = update.get_result(conn,new_model)[1]
                if len(res_title) > 0 and len(res_model) == 0:
                    for line in res_title:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) > 0:
                    for line in res_model:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) == 0:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('Lenovo '):
                # Lenovo 开头查找联想的手机型号
                new_model = model.replace('Lenovo ','').strip()
                print new_model
                res_title = update.get_result(conn,new_model)[0]
                res_model = update.get_result(conn,new_model)[1]
                if len(res_title) > 0 and len(res_model) == 0:
                    for line in res_title:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) > 0:
                    for line in res_model:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) == 0:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('HTC '):
                # HTC 开头查找HTC的手机型号
                new_model = model.replace('HTC ','').strip()
                print new_model
                res_title = update.get_result(conn,new_model)[0]
                res_model = update.get_result(conn,new_model)[1]
                if len(res_title) > 0 and len(res_model) == 0:
                    for line in res_title:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) > 0:
                    for line in res_model:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) == 0:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('ZTE '):
                # ZTE 开头查找中兴的手机型号
                new_model = model.replace('ZTE ','').strip()
                print new_model
                res_title = update.get_result(conn,new_model)[0]
                res_model = update.get_result(conn,new_model)[1]
                if len(res_title) > 0 and len(res_model) == 0:
                    for line in res_title:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) > 0:
                    for line in res_model:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) == 0:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('koobee '):
                # koobee 开头查找酷比的手机型号
                new_model = model.replace('koobee ','').strip()
                print new_model
                res_title = update.get_result(conn,new_model)[0]
                res_model = update.get_result(conn,new_model)[1]
                if len(res_title) > 0 and len(res_model) == 0:
                    for line in res_title:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) > 0:
                    for line in res_model:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) == 0:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('vivo '):
                # vivo 开头查找vivo的手机型号
                new_model = model.replace('vivo ','').strip()
                print new_model
                res_title = update.get_result(conn,new_model)[0]
                res_model = update.get_result(conn,new_model)[1]
                if len(res_title) > 0 and len(res_model) == 0:
                    for line in res_title:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) > 0:
                    for line in res_model:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) == 0:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('ZUK '):
                # ZUK 开头查找ZUK的手机型号
                new_model = model.replace('ZUK ','').strip()
                print new_model
                res_title = update.get_result(conn,new_model)[0]
                res_model = update.get_result(conn,new_model)[1]
                if len(res_title) > 0 and len(res_model) == 0:
                    for line in res_title:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) > 0:
                    for line in res_model:
                        url = line[2]
                        update_sql = "update shouji_all_spider_data set model = '%s' WHERE url = '%s'"%(model,url)
                        cur.execute(update_sql)
                        conn.commit()
                elif len(res_title) == 0 and len(res_model) == 0:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            else:
                data.write(model + '---------- is not found')
                data.write('\n')

    def get_result(self,conn,model):
        cur = conn.cursor()
        sql_title = "select title,model,url from shouji_all_spider_data WHERE title LIKE '%%%%%s%%%%'"%model
        # model本身是否存在该手机型号
        sql_model = "select title,model,url from shouji_all_spider_data WHERE model LIKE '%%%%%s%%%%'"%model
        cur.execute(sql_title)
        res_title = cur.fetchall()
        cur.execute(sql_model)
        res_model = cur.fetchall()
        return res_title,res_model


if __name__ == '__main__':
    update = UpdateModel()
    update.__update_data__(table_name='shouji_all_spider_data')
