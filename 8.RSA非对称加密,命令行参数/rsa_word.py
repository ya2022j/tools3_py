

#  https://www.cnblogs.com/baijinshuo/p/10446399.html
import rsa
import binascii


# ab -n 10000 -c 100  http://localhost:8080/

# 介绍python获取命令行参数的方法：getopt模和argparse模块。
import os
import sys
import getopt




import getopt
import sys

# 命令行参数
# 使用网页中获得的n和e值，将明文加密
def rsa_encrypt(rsa_n, rsa_e, message):
    # 用n值和e值生成公钥
    key = rsa.PublicKey(rsa_n, rsa_e)
    # 用公钥把明文加密
    message = rsa.encrypt(message.encode(), key)
    # 转化成常用的可读性高的十六进制
    message = binascii.b2a_hex(message)
    # 将加密结果转化回字符串并返回
    return message.decode()

def main(argv):
    """
    python3 ab_test.py -r 10000 -c 10 -a http:127.0.0.1
    :param argv:
    :return:
    """
    rsa_message =""

    try:
        options, args = getopt.getopt(argv, "hr:c:a:", ['help',"rsa=", "concurrency=", "address="])

        for option, value in options:
            if option in ("-r", "--rsa"):
                rsa_message  = value

        rsa_encrypt(rsa_n, rsa_e, rsa_message)
        print("公钥n值长度：", len(pubkey_n))
        if len(rsa_message) == 0:
            raise
        message_rsa = rsa_encrypt(rsa_n, rsa_e, rsa_message)[:88]
        # python如何只保留英文字母字符串
        print("".join([x for x in filter(str.isalpha, message_rsa)]))





    except getopt.GetoptError:
        print("###################################################")
        print("\n")
        print("\n")
        print("\n")
        print("python3 rsa_word.py -r helloworld")
        print("\n")
        print("\n")
        print("\n")
        print("###################################################")
        sys.exit()











if __name__ == '__main__':
    # RSA的公钥有两个值n和e，我们在网站中获得的公钥一般就是这样的两个值。
    # n常常为长度为256的十六进制字符串
    # e常常为十六进制‘10001’
    pubkey_n = '8d7e6949d411ce14d7d233d7160f5b2cc753930caba4d5ad24f923a505253b9c39b09a059732250e56c594d735077cfcb0c3508e9f544f101bdf7e97fe1b0d97f273468264b8b24caaa2a90cd9708a417c51cf8ba35444d37c514a0490441a773ccb121034f29748763c6c4f76eb0303559c57071fd89234d140c8bb965f9725'
    pubkey_e = '10001'
    # 需要将十六进制转换成十进制
    rsa_n = int(pubkey_n, 16)
    rsa_e = int(pubkey_e, 16)
    # 要加密的明文
    main(sys.argv[1:])

