









#{
#   "list": [
#     {
#       "id": 1,
#       "value": 1,
#       "label": "动态选项1",
#       "children": [
#         {
#           "id": 2,
#           "value": 2,
#           "label": "动态选项1-1"
#         }
#       ]
#     }
#   ]
# }
#

#  label  value
import re
import time
from lxml import etree
import requests
import html
import json

def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l
def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items

def writeinto_jsonfile(filename,list_data):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(list_data, fw, indent=2, ensure_ascii=False)



if __name__ == "__main__":
    f_list = []
    for item in range(1,48):
        url  = "https://ecitizen.jp/Sac/{0}".format(item)
        res = requests.get(url)
        items = re.findall(re.compile("<h2>(.*?)</h2>",re.S),res.text)
        title = html.unescape(items[0]).split("の")[0]
        parent_item = {}
        parent_item["id"] =  item
        parent_item["value"] = item
        parent_item["label"] =  title
        parent_item["children"] =  []

        element = etree.HTML(res.text)

        code = element.xpath(
            '/html/body/div/div[1]/div[1]/table/tbody/tr/td[1]/text()')
        f_code = RemoveDot(remove_block(code))
        city = element.xpath(
            '/html/body/div/div[1]/div[1]/table/tbody/tr/td[2]/text()')
        f_city = RemoveDot(remove_block(city))
        for i1,i2,i3  in  zip(range(1,len(f_city)+1),f_code,f_city):

            sub_dict = {}
            sub_dict["id"] = i1
            sub_dict["value"] = i1
            sub_dict["label"] = i3
            sub_dict["zip_code"] = i2
            parent_item["children"].append(sub_dict)
        print("parent_item-->", parent_item)


        f_list.append(parent_item)
        time.sleep(0.1)
    print(f_list)
    writeinto_jsonfile("jp_zipcode_city.json",f_list)
