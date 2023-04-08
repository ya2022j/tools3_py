#! -*- utf-8 -*-
import copy
import re
import json
import time

import requests
from lxml import etree
from selenium import webdriver
import csv
import pymysql
driver = webdriver.Chrome()


def request_insertDB(area,firm,line,url):
    driver.get(url)

    html = driver.page_source
    element = etree.HTML(html)

    stations = element.xpath(
        '//*[@id="main"]/div[1]/ul/li/a/text()')
    f_area = len(stations)*[area]
    f_firm = len(stations)*[firm]
    f_line = len(stations)*[line]
    for i1,i2,i3,i4 in zip(f_area,f_firm,f_line,stations):
        content = [(i1,i2,i3,i4)]


        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='jp_lines',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        cursor = connection.cursor()
        try:
            cursor.executemany('insert into JP_line_station_all (area,firm,line,station) values (%s,%s,%s,%s)', content)
            connection.commit()
            connection.close()
            print('向MySQL中添加数据成功！')
        except TypeError :
            pass


if __name__== "__main__":
    for item in range(1,48):
        url = "https://transit.yahoo.co.jp/station/pref/{0}".format(str(item))
        driver.get(url)

        html = driver.page_source
        element = etree.HTML(html)

        area = element.xpath(
            '//*[@id="mdSearchLine"]/div/h1/text()')
        lines_len = element.xpath(
            '//*[@id="mdSearchLine"]/ul/li/dl/dt/text()')
        for num in range(1,len(lines_len)+1):
            single_firm = element.xpath(
                '//*[@id="mdSearchLine"]/ul/li[{0}]/dl/dt/text()'.format(str(num)))
            single_line = element.xpath(
                '//*[@id="mdSearchLine"]/ul/li[{0}]/dl/dd/ul/li/a/text()'.format(str(num)))
            single_line_url = element.xpath(
                '//*[@id="mdSearchLine"]/ul/li[{0}]/dl/dd/ul/li/a/@href'.format(str(num)))
            f_url = ["https://transit.yahoo.co.jp{0}".format(x) for x in single_line_url]
            f_area = area * len(f_url)
            f_single_firm = single_firm * len(f_url)
            f_single_line = single_line * len(f_url)
            for i1,i2,i3,i4 in zip(f_area,f_single_firm,f_single_line,f_url):
                print(i1,i2,i3,i4)
                request_insertDB(i1,i2,i3,i4)
                time.sleep(1)




# # name是mysql的关键字！ (area,firm,line,station)
# create table JP_line_station_all(
# id int not null primary key auto_increment,
# area varchar(50),
# firm varchar(50),
# line varchar(50),
# station varchar(50)
# ) engine=InnoDB default charset=utf8;




# 全国 车站 和线路 按照铁路公司 排列
# SELECT  firm ,COUNT( DISTINCT  line) AS `线路数`,COUNT(station) AS `车站数`  FROM `jp_lines`.`jp_line_station_all` GROUP BY   firm ORDER BY `车站数` desc LIMIT 20 ;
# SELECT area, firm ,COUNT( DISTINCT  line) AS `线路数`,COUNT(station) AS `车站数`  FROM `jp_lines`.`jp_line_station_all` GROUP BY   firm ORDER BY `车站数`  LIMIT 20 ;



#  SELECT DISTINCT  line,firm,count(station) as "station_count" FROM `jp_lines`.`jp_line_station_all`  where area="東京" group by  line order by station_count desc ;




