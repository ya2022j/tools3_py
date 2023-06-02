
#! -*- utf-8 -*-
import datetime
import os
import sys
import getopt



def main(argv):
    """
    python3 autopep8_exec.py -p folder_path
    :param argv:
    :return:
    """
    folder_path =""
    try:
        options, args = getopt.getopt(argv, "hp:", ['help',"folerpath="])

        for option, value in options:
            if option in ("-p", "--folerpath"):
                folder_path  = value

        file_list = []
        for (dirname, subdir, subfile) in os.walk(folder_path):
            ret_file = [os.path.join(dirname, x) for x in subfile]
            for item in ret_file:
                file_list.append(item)

        exec_pep8_cmd = "autopep8 --in-place --aggressive {0}"
        for item in file_list:
            exec_file = item.split("\\")[-1]
            if ".py" in exec_file and ".pyc" not in exec_file:

                os.system(exec_pep8_cmd.format(item))
            print("auto exec pep8 successfully !")




    except getopt.GetoptError:
        print("================================================================")
        print("\n")
        print("Please input command :  python3 autopep8_exec.py -p folder_path")
        print("\n")
        print("================================================================")
        sys.exit()




if __name__ == '__main__':
    main(sys.argv[1:])






