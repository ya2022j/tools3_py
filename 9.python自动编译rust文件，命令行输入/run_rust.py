

# ab -n 10000 -c 100  http://localhost:8080/

# 介绍python获取命令行参数的方法：getopt模和argparse模块。
import os
import sys
import getopt




import getopt
import sys


def main(argv):
    """

    python3 ab_test.py -r 10000 -c 10 -a http:127.0.0.1
    :param argv:
    :return:
    """
    rustfile =""

    try:
        options, args = getopt.getopt(argv, "hr:c:a:", ['help',"rustfile="])

        for option, value in options:
            if option in ("-r", "--rustfile"):
                rustfile  = value



        cmd_compile = "rustc {0}  # 编译 {0}文件".format(rustfile)
        compiled_file = rustfile.split(".rs")[0]
        cmd_exec = "./{0}".format(compiled_file)
        print("cmd_compile-->",cmd_compile)
        print("cmd_exec-->",cmd_exec)

        os.system(cmd_compile)
        print("-------   The content is as follows  -------    ")
        print("\n")

        os.system(cmd_exec)


    except getopt.GetoptError:
        print("###################################################")
        print("\n")
        print("\n")
        print("\n")
        print("python3 run_rust.py -r test.rs")
        print("\n")
        print("\n")
        print("\n")
        print("###################################################")
        sys.exit()




if __name__ == '__main__':
    main(sys.argv[1:])
