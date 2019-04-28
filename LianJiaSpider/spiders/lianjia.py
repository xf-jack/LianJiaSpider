# -*- coding: utf-8 -*-
import time
import random
import re

import scrapy

from LianJiaSpider.items import LianjiaspiderItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['www.ljia.net']
    start_urls = ['http://www.ljia.net/new/p-1.html']

    delay = random.randint(1, 4)

    # url = 'http://www.ljia.net/new/p-{}.html'
    # page = 1

    def parse(self, response):
        estate_detail_url_list = response.xpath('//div[@class="conlist"]/div/ul/h3/a/@href').extract()
        for estate_detail_url in estate_detail_url_list:
            estate_url_list = 'http://www.ljia.net' + estate_detail_url
            yield scrapy.Request(url=estate_url_list, callback=self.parse_detail)
            time.sleep(self.delay)

        # if self.page <= 45:
        #     self.page += 1
        #     url = self.url.format(self.page)
        #     yield scrapy.Request(url=url, callback=self.parse)
        next_pages = response.xpath('//div[@class="page"]/a[@class="next"]/@href').extract_first()
        if next_pages:
            next_page = "http://www.ljia.net" + next_pages
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_detail(self, response):
        item = LianjiaspiderItem()
        item['community_housing_name'] = response.xpath('//div[@class="wrap"]/div/h2/a/text()').extract_first()

        housing_type = response.xpath('//div[@class="wrap"]/div/h2/i/span/text()').extract_first()

        if housing_type:
            item['community_housing_type'] = housing_type
        else:
            item['community_housing_type'] = '无'

        item['community_housing_picture'] = response.xpath('//div[@id="banner"]/img/@src').extract_first()

        item['community_housing_price'] = response.xpath(
            '//div[@class="wrap"]/div/div/dl/dd/span/i/text()').extract_first().strip('\r\n\t')

        item['community_sales_status'] = response.xpath('//div[@class="wrap"]/div/div/dl[2]/dd/text()').extract_first()

        opening_time = response.xpath('//div[@class="wrap"]/div/div/dl[3]/dd/text()').extract_first()
        if opening_time:
            item['community_opening_time'] = opening_time
        else:
            item['community_opening_time'] = '待定'

        making_time = response.xpath('//div[@class="wrap"]/div/div/dl[4]/dd/text()').extract_first()
        if making_time:
            item['community_making_time'] = making_time
        else:
            item['community_making_time'] = '待定'

        housing_area = response.xpath('//div[@class="wrap"]/div/div/dl[5]/dd/text()').extract_first().strip('\r\n\t')
        pattern = re.compile(r'[[](.*?)[]]')
        ret = re.findall(pattern, housing_area)
        item['community_housing_area'] = ''.join(ret)

        item['community_housing_address'] = response.xpath(
            '//div[@class="wrap"]/div/div/dl[5]/dd/text()').extract_first().strip('\r\n\t')

        main_model = response.xpath(
            '//div[@class="wrap"]/div/div/dl[6]/dd[1]/text()').extract_first().strip('\t')
        if main_model:
            item['community_main_model'] = main_model
        else:
            item['community_main_model'] = '无'

        sales_address = response.xpath('//div[@class="wrap"]/div/div/dl[6]/dd[2]/text()').extract_first()
        if sales_address:
            item['community_sales_address'] = sales_address
        else:
            item['community_sales_address'] = '暂无资料'

        item['community_developers'] = response.xpath('//div[@class="wrap"]/div/div/dl[7]/dd/text()').extract_first()

        item['community_contact_phone'] = response.xpath(
            '//div[@class="wrap"]/div/div/dl/div/div/p[2]/text()').extract_first()

        # estate_photo_url = response.xpath('//div[starts-with(@class,"lista")][2]/ul/li/a[2]/@href').extract()
        # for estate_photo in estate_photo_url:
        #     photo_url_list = 'http://www.ljia.net' + estate_photo
        #     yield scrapy.Request(url=photo_url_list, callback=self.parse_photo_detail, meta={'item': item})
        #     time.sleep(self.delay)

        item['community_property_type'] = \
            response.xpath('//div[@class="houseLeft"]/div[1]/p[1]/text()').extract_first().split('：')[-1]

        item['community_decorate_situation'] = \
            response.xpath('//div[@class="houseLeft"]/div[1]/p[2]/span[2]/text()').extract_first().split('：')[-1]

        item['community_covers_area'] = \
            response.xpath('//div[@class="houseLeft"]/div[1]/p[4]/span[1]/text()').extract_first().split('：')[-1]

        item['community_building_area'] = \
            response.xpath('//div[@class="houseLeft"]/div[1]/p[4]/span[2]/text()').extract_first().split('：')[-1]

        item['community_afforestation_rate'] = \
            response.xpath('//div[@class="houseLeft"]/div[1]/p[8]/span[1]/text()').extract_first().split('：')[-1]

        item['community_plot_ratio'] = \
            response.xpath('//div[@class="houseLeft"]/div[1]/p[8]/span[2]/text()').extract_first().split('：')[-1]

        item['community_households_number'] = \
            response.xpath('//div[@class="houseLeft"]/div[1]/p[10]/span[1]/text()').extract_first().split('：')[-1]

        parking_number = \
            response.xpath('//div[@class="houseLeft"]/div[1]/p[10]/span[2]/text()').extract_first().split('：')[-1]
        if parking_number:
            item['community_parking_number'] = parking_number
        else:
            item['community_parking_number'] = '待定'

        property_company = \
            response.xpath('//div[@class="houseLeft"]/div[1]/p[12]/span[1]/text()').extract_first().split('：')[-1]
        if property_company:
            item['community_property_company'] = property_company
        else:
            item['community_property_company'] = '待定'

        property_cost = \
            response.xpath('//div[@class="houseLeft"]/div[1]/p[12]/span[2]/text()').extract_first().split('：')[-1]
        if property_cost:
            item['community_property_cost'] = property_cost
        else:
            item['community_property_cost'] = '待定'

        traffic_situation = \
            response.xpath('//div[@class="houseLeft"]/div[1]/p[14]/text()').extract_first().split('：')[-1]
        if traffic_situation:
            item['community_traffic_situation'] = traffic_situation
        else:
            item['community_traffic_situation'] = '暂无资料'

        # 户型图
        model_figure_url = response.xpath('//div[starts-with(@class,"lista")][1]/ul/li/a[2]/@href').extract()
        for model_figure in model_figure_url:
            figure_url_list = 'http://www.ljia.net' + model_figure
            yield scrapy.Request(url=figure_url_list, callback=self.parse_model_detail, meta={'item': item})
            time.sleep(self.delay)

        yield item

    def parse_model_detail(self, response):
        item = response.meta['item']

        model_figure = response.xpath('//div[@class="showpic"]/div/div/img/@src').extract_first()
        if model_figure:
            item['community_model_figure'] = model_figure
        else:
            item['community_model_figure'] = '没有户型图'

        model_name = response.xpath('//div[@class="tit"]/h2/strong/text()').extract_first()
        if model_name:
            item['community_model_name'] = model_name
        else:
            item['community_model_name'] = '没有户型'

        yield item

    # def parse_photo_detail(self, response):
    #     item = response.meta['item']

    # estate_photo = response.xpath('//div[@class="showpic"]/div/div/img/@src').extract_first()
    # if estate_photo:
    #     item['community_estate_photo'] = estate_photo
    # else:
    #     item['community_estate_photo'] = '没有详情图'

    # estate_photo_name = response.xpath('//div[@class="tit"]/h2/strong/text()').extract_first()
    # if estate_photo_name:
    #     item['community_estate_photo_name'] = estate_photo_name
    # else:
    #     item['community_estate_photo_name'] = '没有图'

    # yield item
