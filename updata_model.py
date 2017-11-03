#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-11-3 15:35:17
# @File : updata_model.py
# @Software : IntelliJ IDEA
# 更新爬虫数据表单shouji_all_spider_data中model字段
import logging

from util import Util
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class UpdataModel(object):

    def __update_data__(self,path):
        # 获取数据库链接
        conn = Util().get_db_conn()
        cur = conn.cursor()
        data = open("conf/data.txt",'a')
        # 读取models手机型号表单
        try:
            file = open(path,'r')
            while 1:
                model = file.readline().strip('\n').strip()
                sql_title = "select * from shouji_all_spider_data WHERE title LIKE '%%%%%s%%%%'"%model
                sql_model = "select * from shouji_all_spider_data WHERE model LIKE '%%%%%s%%%%'"%model
                cur.execute(sql_title)
                res_title = cur.fetchall()
                cur.execute(sql_model)
                res_model = cur.fetchall()
                print model,len(res_title),len(res_model)
                # title字段可以找到，model字段找不到，则更新model字段为modelc
                if len(res_title) > 0 and len(res_model) == 0:
                    data.write(model + ' ------ need update')
                    data.write('\n')
                    for line in res_title:
                        content = line[0]+','+line[1]+','+line[2]+','+line[18]+','+line[20]+','+line[21]
                        data.write(content)
                        data.write('\n')
                elif len(res_title) == 0 and len(res_model) == 0:
                    data.write(model + '---------- is not found')
                    data.write('\n')

                if not model:
                    break
                pass
        except Exception,e:
            logging.exception(e)
        finally:
            conn.close()

    """
    链接数据库
    """
    def __conn_db__(self):
        print ''


if __name__ == '__main__':
    update = UpdataModel()
    update.__update_data__('conf/models.txt')
