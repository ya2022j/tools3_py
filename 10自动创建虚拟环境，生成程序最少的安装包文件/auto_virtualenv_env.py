



import os

# 为了批量快速容器化python应用
# python创建虚拟环境，然后导出运行代码需要最少的包安装完，再到处安装包文件，并创建新的main.py文件
# 介绍python获取命令行参数的方法：getopt模和argparse模块。
import os
import re
import sys
import getopt
import time


import getopt
import sys



# 2. install library


def install_virtualenv(pythonfile):
    # 1. install virtualenv
    env_name = pythonfile.split(".py")[0]

    os.system("pip3  install virtualenv -i http://pypi.douban.com/simple --trusted-host pypi.douban.com ")
    os.system("virtualenv {0}".format(env_name))


    activate_path = os.path.join(os.path.join(first_path, env_name), "Scripts")

    os.chdir(activate_path)
    os.system("activate")

def install_library(pythonfile):
    library_list = []
    exec_file = os.path.join(first_path,pythonfile)
    with open(exec_file, "r",encoding="UTF-8") as f:
        line = f.readlines()
        for item in line:
            parse_string = item.split("\n")[0]
            if "import"  in item.split("\n")[0] or "from" in parse_string:
                if parse_string[:4] == "from":
                    library_list.append(parse_string.split(" ")[1])
                if parse_string[:4] == "impo":
                    library_list.append(parse_string.split(" ")[1])

    for item in set(library_list):
        os.system("pip3  install {0} -i http://pypi.douban.com/simple --trusted-host pypi.douban.com ".format(item))

    # 3. output requirements.txt
    requirements_filepath  = os.path.join(first_path,"requirements.txt")
    os.system("pip3 freeze > {0}".format(requirements_filepath))

    # 4. cp exec file ==>  main.py

    # os.system("cp {0} main.py".format(pythonfile))







def main(argv):
    """

    python3 ab_test.py -r 10000 -c 10 -a http:127.0.0.1
    :param argv:
    :return:
    """
    pythonfile =""

    try:
        options, args = getopt.getopt(argv, "hp:c:a:", ['help',"pythonfile="])

        for option, value in options:
            if option in ("-p", "--pythonfile"):
                pythonfile  = value



        install_virtualenv(pythonfile)
        time.sleep(0.5)
        install_library(pythonfile)



    except getopt.GetoptError:
        print("###################################################")
        print("\n")
        print("\n")
        print("\n")
        print("python3 auto_virtualenv_env.py-p forcontainer.py ")
        print("\n")
        print("\n")
        print("\n")
        print("###################################################")
        sys.exit()




if __name__ == '__main__':
    first_path = os.getcwd()
    main(sys.argv[1:])





