# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import urllib.request
import os

import pymysql


class LianjiaspiderPipeline(object):
    def open_spider(self, spider):
        # 打开文件
        self.fp = open('lianjia.json', 'w', encoding='utf8')
        # 打开数据库
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='asd123!@#', db='lianjia',
                                    charset='utf8')

    def create_dir(self, path):
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        # 判断路径是否存在
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False

    def process_item(self, item, spider):
        d = dict(item)
        string = json.dumps(d, ensure_ascii=False)
        self.fp.write(string + '\n')

        # 保存数据
        sql = "insert into lianjia (community_housing_name,community_housing_type,community_housing_picture," \
              "community_housing_price,community_sales_status,community_opening_time,community_making_time," \
              "community_housing_area,community_housing_address,community_main_model,community_sales_address," \
              "community_developers,community_contact_phone,community_property_type,community_decorate_situation," \
              "community_covers_area,community_building_area,community_afforestation_rate,community_plot_ratio," \
              "community_households_number,community_parking_number,community_property_company,community_property_cost," \
              "community_traffic_situation) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'," \
              "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
              (item['community_housing_name'], item['community_housing_type'], item['community_housing_picture'],
               item['community_housing_price'], item['community_sales_status'], item['community_opening_time'],
               item['community_making_time'], item['community_housing_area'], item['community_housing_address'],
               item['community_main_model'], item['community_sales_address'], item['community_developers'],
               item['community_contact_phone'], item['community_property_type'], item['community_decorate_situation'],
               item['community_covers_area'], item['community_building_area'], item['community_afforestation_rate'],
               item['community_plot_ratio'], item['community_households_number'], item['community_parking_number'],
               item['community_property_company'], item['community_property_cost'], item['community_traffic_situation'])
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        # 下载图片
        self.download(item)
        return item

    def download(self, item):
        # 楼盘名字的文件夹
        estate_path = "./lianjia/" + item["community_housing_name"]
        self.create_dir(estate_path)
        suffix_estate = item['community_housing_picture'].split('.')[-1]

        filename_estate = item['community_housing_name'] + '.' + suffix_estate

        filepath_estate = os.path.join(estate_path, filename_estate)

        urllib.request.urlretrieve(item['community_housing_picture'], filepath_estate)

        model_path = "./lianjia/" + '/' + item["community_housing_name"] + '/' + 'model'
        self.create_dir(model_path)

        suffix_model = item['community_model_figure'].split('.')[-1]

        filename_model = item['community_model_figure'].split('/')[-1]

        filepath_model = os.path.join(model_path, filename_model)

        if suffix_model == 'jpg':
            urllib.request.urlretrieve(item['community_model_figure'], filepath_model)

        # estate_path = "./lianjia/" + '/' + item["community_housing_name"] + '/' + 'estate'
        # self.create_dir(estate_path)

        # suffix_photo = item['community_estate_photo'].split('.')[-1]

        # filename_photo = item['community_estate_photo'].split('/')[-1]

        # filepath_photo = os.path.join(estate_path, filename_photo)

        # if suffix_photo == 'jpg':
        #     urllib.request.urlretrieve(item['community_estate_photo'], filepath_photo)

    def close_spider(self, spider):
        # 关闭文件
        self.fp.close()
        # 关闭mysql数据库
        self.cursor.close()
        self.conn.close()
