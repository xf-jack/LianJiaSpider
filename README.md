# lianjia-spider
# 本项目是一个爬虫项目，仅供学习参考使用
# 1.安装依赖
# 2.进入spider目录中
cd LianJiaSpider/spiders/
# 3.运行启动爬虫命令
scrapy crawl lianjia
# 保存csv文件
scrapy crawl lianjia -o lianjia.csv  
 
# 建库
create database lianjia charset utf8;
# 建表
create table lianjia(
 id int primary key auto_increment,
 community_housing_name varchar(200),
 community_housing_type varchar(200),
 community_housing_picture varchar(200),
 community_housing_price varchar(200),
 community_sales_status varchar(200),
 community_opening_time varchar(200),
 community_making_time varchar(200),
 community_housing_area varchar(200),
 community_housing_address varchar(200),
 community_main_model varchar(200),
 community_sales_address varchar(200),
 community_developers varchar(200),
 community_contact_phone varchar(200),
 community_property_type varchar(200),
 community_decorate_situation varchar(200),
 community_covers_area varchar(200),
 community_building_area varchar(200),
 community_afforestation_rate varchar(200),
 community_plot_ratio varchar(200),
 community_households_number varchar(200),
 community_parking_number varchar(200),
 community_property_company varchar(200),
 community_property_cost varchar(200),
 community_traffic_situation varchar(200)
);
 
 

