#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-11-3 15:35:17
# @File : updata_model_normal.py
# @Software : IntelliJ IDEA
# 更新爬虫数据表单shouji_all_spider_data中model字段
import os

from util import Util
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class UpdateModel(object):

    """
    查找手机型号与品牌前1000条数据
    :param brand_table 手机型号表单
    :param spider_table 需要更新的爬虫表单
    """
    def __update_data__(self,brand_table,spider_table):

        # 存放检查手机模型不存在的文件conf/data_notfound.txt，每次检查手机模型，重新生成
        if os.path.exists("conf/data_notfound.txt"):
            os.remove("conf/data_notfound.txt")

        # 读取models手机型号表单
        conn = Util().get_db_conn()
        cur = conn.cursor()
        sql = "SELECT * FROM %s WHERE brand != 'NULL' AND brand_chinese IS NOT NULL ORDER BY cnt DESC LIMIT 1000"%brand_table
        cur.execute(sql)
        res = cur.fetchall()
        for line in res:
            model = line[0]
            brand = line[1]
            cnt = line[2]
            brand_chinese = line[3]
            print model,brand,cnt,brand_chinese
            # 更新爬虫表单
            update.__update_model__(model,brand_chinese,spider_table)

    """
    更新爬虫数据中的手机型号
    :param model:要更新的手机型号
    :param brand:要更新手机型号的所属品牌拼音
    :param brand_chinese:要更新手机型号的所属中文名称
    :param table_name:要更新的爬虫表单
    """
    def __update_model__(self,model,brand_chinese,table_name):
        conn = Util().get_db_conn()
        cur = conn.cursor()
        # 按照brand查找数据
        res_title = update.get_result(conn,brand_chinese,model,table_name)[0]
        res_model = update.get_result(conn,brand_chinese,model,table_name)[1]
        # 标题中存在，model字段不存在，则更新model字段为当前model
        if len(res_title) > 0 and len(res_model) == 0 :
            for line in res_title:
                url = line[0]
                update_sql = "update %s set model = '%s' WHERE url = '%s'"%(table_name,model,url)
                cur.execute(update_sql)
                conn.commit()
                print 'update ----- ',model,brand_chinese,url
        # 如果找不到，则区别对待
        elif len(res_title) == 0 and len(res_model) == 0:
            # 去掉HUAWEI开头查找华为的手机型号
            data = open("conf/data_notfound.txt",'a')
            new_model = ""
            if model.startswith('HUAWEI '):
                new_model = model.replace('HUAWEI ','').strip()
            elif model.startswith('SM-'):
                # 去掉SM-开头查找三星的手机型号
                new_model = model.replace('SM-','').strip()
            elif model.startswith('GT-'):
                # 去掉GT-开头查找三星的手机型号
                new_model = model.replace('GT-','').strip()
            elif model.startswith('Coolpad '):
                # Coolpad 开头查找酷派的手机型号
                new_model = model.replace('Coolpad ','').strip()
            elif model.startswith('Lenovo '):
                # Lenovo 开头查找联想的手机型号
                new_model = model.replace('Lenovo ','').strip()
            elif model.startswith('HTC '):
                # HTC 开头查找HTC的手机型号
                new_model = model.replace('HTC ','').strip()
            elif model.startswith('ZTE '):
                # ZTE 开头查找中兴的手机型号
                new_model = model.replace('ZTE ','').strip()
            elif model.startswith('koobee '):
                # koobee 开头查找酷比的手机型号
                new_model = model.replace('koobee ','').strip()
            elif model.startswith('vivo '):
                # vivo 开头查找vivo的手机型号
                new_model = model.replace('vivo ','').strip()
            elif model.startswith('ZUK '):
                # ZUK 开头查找ZUK的手机型号
                new_model = model.replace('ZUK ','').strip()
            else:
                data.write(model + '---------- is not found')
                data.write('\n')

            # 如果切割后的model存在，则按切割后的model加上品牌重新查找
            if new_model != "":
                update.__update_recursion__(conn,model,brand_chinese,new_model,table_name)

    def __update_recursion__(self, conn,model, brand_chinese, new_model,table_name):
        data = open("conf/data_notfound.txt",'a')
        cur = conn.cursor()
        res_title = update.get_result(conn,brand_chinese,new_model,table_name)[0]
        res_model = update.get_result(conn,brand_chinese,new_model,table_name)[1]
        if len(res_title) > 0 and len(res_model) == 0:
            for line in res_title:
                url = line[0]
                update_sql = "update %s set model = '%s' WHERE url = '%s'"%(table_name,model,url)
                cur.execute(update_sql)
                conn.commit()
                print 'update ----- ',model,brand_chinese,url
        else:
            data.write(model + '---------- is not found')
            data.write('\n')

    """
    获取查询爬虫数据表的结果，根据手机型号的中文品牌like查询爬虫数据中的title，如果为该品牌数据，则再查找手机型号
    :param conn：存储爬虫数据的数据库连接串
    :param brand_chinese：手机型号的中文品牌
    :param model：手机型号
    """
    def get_result(self,conn,brand_chinese,model,table_name):
        cur = conn.cursor()
        # model本身是否存在该手机型号
        sql_title = "select url from %s WHERE title LIKE '%%%%%s%%%%' AND title LIKE '%%%%%s%%%%'"%(table_name,brand_chinese,model)
        cur.execute(sql_title)
        res_title = cur.fetchall()
        sql_model = "select url from %s WHERE title LIKE '%%%%%s%%%%' AND model LIKE '%%%%%s%%%%'"%(table_name,brand_chinese,model)
        cur.execute(sql_model)
        res_model = cur.fetchall()
        return res_title,res_model




if __name__ == '__main__':
    update = UpdateModel()
    # 更新爬虫表单中的手机型号，传入参数为爬虫数据表名
    update.__update_data__(brand_table='model_and_brand_top50_youxiao',spider_table='shouji_all_spider_data')
