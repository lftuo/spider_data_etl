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
                sql = "select * from shouji_all_spider_data WHERE title LIKE '%%%%%s%%%%' OR model LIKE '%%%%%s%%%%'"%(model,model)
                cur.execute(sql)
                res = cur.fetchall()
                data.write(str(len(res)))
                data.write('\n')
                if len(res) > 0:
                    for line in res:
                        content = line[0]+','+line[1]+','+line[2]+','+line[18]+','+line[20]+','+line[21]
                        print content
                        data.write(content)
                        data.write('\n')
                else:
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
