# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 详细信息
    community_housing_name = scrapy.Field()  # 楼盘名称
    community_housing_type = scrapy.Field()  # 楼盘类型
    community_housing_picture = scrapy.Field()  # 楼盘图片
    community_housing_price = scrapy.Field()  # 楼盘均价
    community_sales_status = scrapy.Field()  # 销售状态
    community_opening_time = scrapy.Field()  # 开盘时间
    community_making_time = scrapy.Field()  # 交房时间
    community_housing_area = scrapy.Field()  # 楼盘区域
    community_housing_address = scrapy.Field()  # 楼盘详细地址
    community_main_model = scrapy.Field()  # 主要户型
    community_sales_address = scrapy.Field()  # 售楼地址
    community_developers = scrapy.Field()  # 开发商
    community_contact_phone = scrapy.Field()  # 售楼电话
    # 户型
    community_model_figure = scrapy.Field()  # 户型图
    community_model_name = scrapy.Field()  # 户型名
    # 相册
    community_estate_photo = scrapy.Field()  # 相册图
    community_estate_photo_name = scrapy.Field()  # 相册名
    # community_estate_photo_xiaoguo = scrapy.Field()  # 效果图
    # community_estate_photo_xiaoguo_name = scrapy.Field()  # 效果图名
    # 概况
    community_property_type = scrapy.Field()  # 物业类型
    community_decorate_situation = scrapy.Field()  # 装修情况
    community_covers_area = scrapy.Field()  # 占地面积
    community_building_area = scrapy.Field()  # 建筑面积
    community_afforestation_rate = scrapy.Field()  # 绿化率
    community_plot_ratio = scrapy.Field()  # 容积率
    community_households_number = scrapy.Field()  # 总户数
    community_parking_number = scrapy.Field()  # 车位数
    community_property_company = scrapy.Field()  # 物业公司
    community_property_cost = scrapy.Field()  # 物业费用
    community_traffic_situation = scrapy.Field()  # 交通情况
