#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-11-3 15:35:17
# @File : updata_model_normal.py
# @Software : IntelliJ IDEA
# 更新爬虫数据表单shouji_all_spider_data中model字段
import logging
import os

from util import Util
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class UpdateModel(object):

    def __update_data__(self,top_limit,brand_table,spider_table):
        '''
        查找手机型号与品牌前1000条数据
        :param top_limit：品牌条数限制，SQL中查询型号与品牌表中的top多少条
        :param brand_table: 手机型号表单
        :param spider_table: 需要更新的爬虫表单
        :return:
        '''

        # 存放检查手机模型不存在的文件conf/data_notfound.txt，每次检查手机模型，重新生成
        if os.path.exists("conf/data_notfound.txt"):
            os.remove("conf/data_notfound.txt")

        # 读取models手机型号表单
        conn = Util().get_db_conn()
        cur = conn.cursor()
        sql = "SELECT * FROM %s WHERE brand != 'NULL' AND brand_chinese IS NOT NULL ORDER BY cnt DESC LIMIT %s"%(brand_table,top_limit)
        cur.execute(sql)
        res = cur.fetchall()
        try:
            for line in res:
                model = line[0]
                brand = line[1]
                cnt = line[2]
                brand_chinese = line[3]
                print model,brand,cnt,brand_chinese
                # 更新爬虫表单
                update.__update_model__(model,brand_chinese,spider_table)
        except Exception,e:
            logging.exception(e)
        finally:
            conn.close()

    def __update_model__(self,model,brand_chinese,table_name):
        '''
        更新爬虫数据中的手机型号
        :param model: 要更新的手机型号
        :param brand_chinese: 要更新手机型号的所属中文名称
        :param table_name: 爬虫数据表单
        :return:
        '''

        conn = Util().get_db_conn()
        try:
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
                elif model.startswith('HONOR '):
                    # 去掉HONOR 开头查找荣耀的手机型号
                    new_model = model.replace('HONOR ','').strip()
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
                elif model.startswith('OPPO '):
                    # OPPO 开头查找OPPO的手机型号
                    new_model = model.replace('OPPO ','').strip()
                elif model.startswith('ZUK '):
                    # ZUK 开头查找ZUK的手机型号
                    new_model = model.replace('ZUK ','').strip()
                elif model.startswith('Letv '):
                    # Letv 开头查找乐视的手机型号
                    new_model = model.replace('Letv ','').strip()
                elif model.startswith('Le '):
                    # Le 开头查找乐视的手机型号
                    new_model = model.replace('Le ','').strip()
                elif model.startswith('Hisense '):
                    # Hisense 开头查找海信的手机型号
                    new_model = model.replace('Hisense ','').strip()
                else:
                    data.write(model + '---------- is not found')
                    data.write('\n')

                # 如果切割后的model存在，则按切割后的model加上品牌重新查找
                if new_model != "":
                    update.__update_recursion__(conn,model,brand_chinese,new_model,table_name)
        except Exception,e:
            logging.exception(e)
        finally:
            conn.close()

    def __update_recursion__(self, conn,model, brand_chinese, new_model,table_name):
        '''
        更新爬虫数据表
        :param conn: 数据库连接串
        :param model: 手机型号
        :param brand_chinese: 手机型号品牌的中文描述
        :param new_model: 去掉前缀的手机型号：如HUIWEI XXXXXXXX，去掉HUAWEI，XXXXXXXX作为新的手机型号
        :param table_name: 爬虫数据表名
        :return:
        '''

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

    def get_result(self,conn,brand_chinese,model,table_name):
        '''
        获取查询爬虫数据表的结果，根据手机型号的中文品牌like查询爬虫数据中的title，如果为该品牌数据，则再查找手机型号
        :param conn: 存储爬虫数据的数据库连接串
        :param brand_chinese: 手机型号的中文品牌
        :param model: 手机型号
        :param table_name: 爬虫数据表名
        :return:
        '''

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
    update.__update_data__(top_limit=10000,brand_table='model_and_brand',spider_table='shouji_all_spider_data')
