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
    requestNum =""
    concurrency =""
    address =""
    try:
        options, args = getopt.getopt(argv, "hr:c:a:", ['help',"requestNum=", "concurrency=", "address="])

        for option, value in options:
            if option in ("-r", "--requestNum"):
                requestNum  = value

            if option in ("-c", "--concurrency"):
                concurrency  = value

            if option in ("-a", "--address"):
                address  = value

        ab_test_cmd = "ab -n {0} -c {1}  {2}".format(requestNum,concurrency,address)
        print(ab_test_cmd)

        os.system(ab_test_cmd)


    except getopt.GetoptError:
        print("###################################################")
        print("\n")
        print("\n")
        print("\n")
        print("python3 ab_test.py -r 10000 -c 10 -a http:127.0.0.1")
        print("\n")
        print("\n")
        print("\n")
        print("###################################################")
        sys.exit()




if __name__ == '__main__':
    main(sys.argv[1:])
