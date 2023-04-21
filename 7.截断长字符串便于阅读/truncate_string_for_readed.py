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
