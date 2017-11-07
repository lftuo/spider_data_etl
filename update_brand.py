#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-11-6 15:06:26
# @File : update_brand.py
# @Software : IntelliJ IDEA
# 更新品牌信息
from util import Util


def __update__(table_name):
    conn = Util().get_db_conn()
    cur = conn.cursor()
    # 查询所有中文品牌
    cur.execute("SELECT DISTINCT brand_chinese FROM model_and_brand WHERE brand_chinese IS NOT NULL")
    res = cur.fetchall()
    for line in res:
        chinese_brand = line[0]
        # 查询所有中文品牌对应的英文品牌
        brand_sql = "SELECT DISTINCT brand FROM model_and_brand WHERE brand_chinese = '%s'"%chinese_brand
        cur.execute(brand_sql)
        brand_res = cur.fetchall()
        for line in brand_res:
            brand = line[0]
            print chinese_brand,brand
            # 根据中文品牌名匹配爬虫结果表数据，添加爬虫品牌字段
            result_sql = "select title,url from %s WHERE title LIKE '%%%%%s%%%%'"%(table_name,chinese_brand)
            print result_sql
            cur.execute(result_sql)
            result = cur.fetchall()
            for line in result:
                url = line[1]
                # 更新table_name中的brand字段
                update_sql = "update %s set brand = '%s' WHERE url = '%s'"%(table_name,brand,url)
                cur.execute(update_sql)
                print line[0],line[1]
            conn.commit()

if __name__ == '__main__':
    __update__(table_name='shouji_all_spider_data')