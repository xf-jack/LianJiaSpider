# -*- coding: UTF-8 -*-

"""
@author: XueFei
@date: 2019-04-09 17:28:47
"""
import random

str2 = "   Runoob      "  # 去除首尾空格
# print(str2.strip())

delay = random.randint(1, 5)
# print(delay)

import re

string = '[丛台区]中华大街与北环路交叉口北行50米路东（北湖公园南岸）'
p1 = re.compile(r'[[](.*?)[]]', re.S)  # 最小匹配
p2 = re.compile(r'[(](.*)[)]', re.S)  # 贪婪匹配
p = re.findall(p1, string)
# print(''.join(p))
# print(re.findall(p2, string))

# number = table.xpath('.//td/div/div/span[last()]/text()')[0]
# 取出评价人数里面的数字部分
pattern = re.compile(r'[[](.*?)[]]')
ret = re.findall(pattern, string)
# 判断有没有匹配成功
# if ret:
# 	number = ret.group()
# else:
# 	number = '0'
# print(type(''.join(ret)))

s = "物业类型：住宅"
s1 = s.split("：")[-1]
# print(s1)

import requests
import json

url = 'http://www.toutiao.com/api/pc/focus/'
wbdata = requests.get(url).text
data = json.loads(wbdata)
news = data['data']['pc_feed_focus']
for n in news:
    title = n['title']
    img_url = n['image_url']
    url = n['media_url']
    print(url, title, img_url)
