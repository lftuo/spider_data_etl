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

    def __update_data__(self,path):
        # 读取models手机型号表单
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


    def __update_model_recursion__(self,model):
        conn = Util().get_db_conn()
        cur = conn.cursor()
        res_title = update.get_result(conn,model)[0]
        res_model = update.get_result(conn,model)[1]
        data = open("conf/data.txt",'a')
        print model,len(res_title),len(res_model)
        # title字段可以找到，model字段找不到，则更新model字段为model
        if len(res_title) > 0 and len(res_model) == 0:
            data.write(model + ' ------ need update')
            data.write('\n')
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
                elif len(res_title) == 0 and len(res_model) == 0:
                    data.write(model + '---------- is not found')
                    data.write('\n')
            elif model.startswith('SM-'):
                # 去掉SM-开头查找华为的手机型号
                new_model = model.replace('SM-','').strip()
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
    update.__update_data__('conf/models.txt')
