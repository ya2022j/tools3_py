


# tsv文件的格式还是比较适合 阅读，所以选择从MySQL的数据表的字段中，第一行放那些字段，
# 其他的截断放在后面即可
import time
import csv

import pymysql
import datetime

def writeintoTSV_file(filename, data):
    with open(filename, 'a', encoding="utf-8") as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(data)
# Truncating strings for readable output
def truncate_string_for_readed(text):
    ret_list = []
    len_text = len(text)
    base_text_num = 88
    integer,remainder = divmod(len_text,base_text_num)
    # 整数,处理
    ret_list.append(text[0:base_text_num])
    for item in range(1,integer):
        ret_list.append(text[base_text_num*item:base_text_num*(item+1)])
    # 余数处理 - ok
    ret_list.append(text[integer*base_text_num:])
    return ret_list

def cleanup_content(string_item):
    ret = " ".join(string_item.split())
    return ret

def fetch_dt_output_tsv(dbname,tablename):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db=dbname,
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cur = connection.cursor()
    sql_check_field = "desc {0}".format(tablename)
    cur.execute(sql_check_field)
    # #获取所有记录列表
    fields = cur.fetchall()
    fields_ret = [x["Field"] for x in fields]
    # ['id', 'fulltime_title', 'fulltime_url', 'fulltime_content_66', 'fulltime_content', 'fulltime_siteno', 'stack_type', 'delete_flg', 'others', 'LastTime']
    title_field= ""
    url_field= ""
    content_field= ""
    stack_type_field= ""
    for item in fields_ret:
        if "title" in item:
            title_field = item
        elif "url" in item:
            url_field = item
        elif "content" in item and "66" not in item :
            content_field = item
        elif "stack_type" in item:
            stack_type_field = item



    sql_count_id = "select count(id) from  {0}".format(tablename)
    cur.execute(sql_count_id)
    # #获取所有记录列表
    sql_count_id_ret  = cur.fetchall()
    try:

        for num in range(1,sql_count_id_ret[0]["count(id)"]+1):
            sql_fetch_dt = "select {0},{1},{2},{3} from {4} where id ={5}; ".format(url_field,stack_type_field,title_field,content_field,tablename,num)
            cur.execute(sql_fetch_dt)
            dt_ret = cur.fetchone()
            writeintoTSV_file(tsvfile, ["="*128])
            writeintoTSV_file(tsvfile, [str(dt_ret[url_field]) + " "+ str(dt_ret[stack_type_field])])
            writeintoTSV_file(tsvfile, [str(dt_ret[title_field])])
            writeintoTSV_file(tsvfile, ["="*128])
            for one_content in truncate_string_for_readed(cleanup_content(str(dt_ret[content_field]))):
                writeintoTSV_file(tsvfile, [one_content])
            print("output ok")
    except:
        pass






if __name__ == "__main__":
    DBNAME = "fulltime"
    TABLENAME = "fulltime_work"
    tsvfile = datetime.datetime.now().strftime("%Y-%m-%d") + "-{0}.tsv".format(TABLENAME)

    fetch_dt_output_tsv(DBNAME,TABLENAME)



