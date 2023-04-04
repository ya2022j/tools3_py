import os


def readDatafile(filename):
    line_list = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line_list.append(line)
    return line_list




if __name__ == "__main__":
    ret = readDatafile("init_vue2_app")
    for item in ret:
        if "npm" in item or "yarn" in item:
            print(item)
            os.system("{0}".format(item))

