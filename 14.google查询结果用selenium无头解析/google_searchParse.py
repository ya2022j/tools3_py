



#! coding:utf-8

import csv


from selenium import webdriver
from lxml import etree
import os
import sys
from bs4 import BeautifulSoup

# sys.path.append(os.path.abspath(os.path.join(os.getcwd(),"utils")))


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# from utils.fullRemote_config import SIDEWORK_SITE_8 as url_list
# from utils.fullRemote_config import STACK_LIST as stack_list
# from utils.model import Model






class BS4Parse():
    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def parseOneElement(self, tagName):
        trans_list = []
        for single_tag in self.soup.select(tagName):
            trans_list.append(" ".join(single_tag.text.split()))
        tagText = " ".join(trans_list)
        return tagText, trans_list
    def parseClassAttribute(self,outsidetag,classAttribute):
        trans_list = []
        ret = self.soup.findAll(name=outsidetag, attrs={"class":classAttribute})

        for item in ret:
            trans_list.append("".join(item.text))
        tagText = " ".join(trans_list)
        return tagText, trans_list


    def parseIDAttribute(self,DAttribute):
        trans_list = []
        ret = self.soup.findAll(id=DAttribute)

        for item in ret:
            trans_list.append("".join(item.text))
        tagText = " ".join(trans_list)
        return tagText, trans_list


    def fetchAllText(self):
        AllText = "".join(self.soup.get_text().split())
        return AllText






def writeinto_htmlfile(filename, data):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        f.write(data)
        f.write("\n")

def writeintoTSV_file(filename, data):
    with open(filename, 'a', encoding="utf-8") as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(data)

from functools import reduce

def list_dict_dulicate_removal(list_item):
    run_func = lambda x,y:x if y in x else x+[y]
    return reduce(run_func,([[],]+list_item))




    # if "お探しの条件のお仕事は見つかりませんでした。" not in str(html):
    #     # 暴力翻页，直接都去遍历8页，
    #     element = etree.HTML(html)
    #     title = element.xpath('/html/body/main/div[4]/div/div[2]/div/div/div/a/h3/text()')
    #     url = element.xpath('/html/body/main/div[4]/div/div[2]/div/div/div/a/@href')
    #     f_url = ["https://crowdtech.jp{0}".format(x) for x in url]
    #     b = BS4Parse(html)
    #     _, ret = b.parseClassAttribute("div","job-text-container")
    #
    #     for i1,i2,i3 in zip(title,f_url,ret):
    #         # 先去重，再去整理
    #         first_list = [i1,i2,i3[:60] + " ...",i3,"8"," ".join([x for x in stack_list if x in i3 ]),"0"]
    #
    #         f_list.append(first_list)
    # else:
    #     pass







if __name__ == '__main__':


    # 创建浏览器对象
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Chrome()  # 不加 chrome_options 参数就是正常的打开一个浏览器，进行操作




    url = "https://www.google.com/search?q=アーゲル食品有限会社"
    driver.get(url)
    # time.sleep(3)
    html = driver.page_source
    # time.sleep(3)
    b = BS4Parse(html)
    ret,_ = b.parseIDAttribute("center_col")
    print(ret)

    driver.quit()

    # model_instance = Model()
    #

    # f_list = []
    #
    #
    # for item1 in range(1,9):
    #     for item2 in url_list:
    #         item_url = item2.format(str(item1))
    #         use_selenium_request(item_url)
    #
    # f_list_removal = list(set([tuple(t) for t in f_list]))
    # for item in f_list_removal:
    #     insert_param = {}
    #     insert_param["sidework_title"]= item[0]
    #     insert_param["sidework_url"]= item[1]
    #     insert_param["sidework_content_66"]= item[2]
    #     insert_param["sidework_content"]= item[3]
    #     insert_param["sidework_siteno"]= item[4]
    #     insert_param["stack_type"]= item[5]
    #     insert_param["delete_flg"]= item[6]
    #     model_instance.insert("sidework_fullremote", [insert_param])
    #
    # driver.quit()

#
#
# create table sidework_fullremote (id int not null primary key auto_increment,
# sidework_title  varchar(255),
# sidework_url  varchar(255),
# sidework_content_66 text,
# sidework_content text,
# sidework_siteno varchar(255),
# stack_type varchar(255),
# delete_flg varchar(1) NOT NULL DEFAULT '0',
# others  varchar(255) not null DEFAULT '',
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;
#
