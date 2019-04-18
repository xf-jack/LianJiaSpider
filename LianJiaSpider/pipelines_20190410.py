# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import urllib.request
import os


class LianjiaspiderPipeline(object):
    # 写到文件,打开文件
    def open_spider(self, spider):
        self.fp = open('lianjia.json', 'w', encoding='utf8')

    def process_item(self, item, spider):
        # 将item转换成字典
        d = dict(item)
        # 将字典转换成json字符串
        string = json.dumps(d, ensure_ascii=False)
        self.fp.write(string + '\n')
        # 下载图片
        self.download(item)
        return item

    def download(self, item):
        # 判断文件夹是否存在
        dirname = 'lianjia'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        # 切割去后缀
        suffix_estate = item['community_housing_picture'].split('.')[-1]
        suffix_model = item['community_model_figure'].split('.')[-1]
        # 图片名称拼接
        filename_estate = item['community_housing_name'] + '.' + suffix_estate
        filename_model = item['community_model_name'] + '.' + suffix_model
        # 图片路劲拼接
        filepath_estate = os.path.join(dirname, filename_estate)
        filepath_model = os.path.join(dirname, filename_model)
        # 下载
        urllib.request.urlretrieve(item['community_housing_picture'], filepath_estate)
        urllib.request.urlretrieve(item['community_model_figure'], filepath_model)

    # 关闭文件
    def close_spider(self, spider):
        self.fp.close()
