# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import urllib.request
import os


class LianjiaspiderPipeline(object):
    def open_spider(self, spider):
        self.fp = open('lianjia.json', 'w', encoding='utf8')

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
        self.fp.close()
