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
            result_sql = "select * from %s where title LIKE '%%%%%s%%%%'"%(table_name,phone_name)
            cur.execute(result_sql)
            type_results = cur.fetchall()
            all_types = Internal_Name+";"+Identifier

            # 遍历某一型号的iPhone手机数据
            for line in type_results:
                id = line[0]
                title = line[1]
                price = line[2]
                screen_size = line[3]
                screen_material = line[4]
                resolution = line[5]
                opreating_system = line[6]
                cpu_name = line[7]
                core_nums = line[8]
                ram = line[9]
                rom = line[10]
                phone_color = line[11]
                phone_material = line[12]
                sim = line[13]
                sim_max_nums = line[14]
                battery = line[15]
                type1 = line[16]
                type2 = line[17]
                model = line[18]
                time = line[19]
                url = line[20]
                data_source = line[21]
                brand = line[22]
                # 删除原有数据
                sql_delete = "delete from %s WHERE url = '%s'"%(table_name,url)
                cur.execute(sql_delete)

                print id,title,price,screen_size,screen_material,resolution,opreating_system,cpu_name,core_nums,ram,rom,phone_color,phone_material,sim,sim_max_nums,battery,type1,type2,model,time,url,data_source,brand
                # 按照";"进行切分获取单个iPhone型号，每个型号对应一条数据，同一条数据复制型号总是条

                for type in all_types.split(";"):
                    content = "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'"\
                              %(id,title,price,screen_size,screen_material,resolution,opreating_system,cpu_name,core_nums,ram,rom,phone_color,phone_material,sim,sim_max_nums,battery,type1,type2,type,time,url,data_source,brand)
                    # 插入新的数据，每条数据对应应该iPhone型号
                    insert_sql = "insert into %s VALUES (%s)"%(table_name,content)
                    print insert_sql
                    cur.execute(insert_sql)
                conn.commit()

    def __update_brand__(self,table_name):
        '''
        更新爬虫数据中iPhone数据的brand字段
        :param table_name:爬虫数据表单
        :return:
        '''
        conn = Util().get_db_conn()
        cur = conn.cursor()
        update_sql = "update %s set brand = 'iPhone' WHERE title LIKE '%%%%苹果%%%%' OR title LIKE '%%%%Apple%%%%' OR title LIKE '%%%%iPhone%%%%'"%table_name
        cur.execute(update_sql)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    update = UpdateIphoneModel()
    # 更新手机型号
    update.__update__(table_name='shouji_all_spider_data')
    # 更新iPhone数据的brand字段
    update.__update_brand__(table_name='shouji_all_spider_data')