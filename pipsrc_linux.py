# coding=utf-8
import os
import re


# 用户选择源函数
def Select_src():
    # 用户输入选择
    n = input("\n选择一个源:")
    # 自定义输入部分
    if n in ["n", "N"]:
        custom_src = input("请输入，以http(s)开头 /结尾：")
        # 正则匹配域名，未匹配到域名则要求重新输入
        if re.search('(?<=//).*?(?=/)', custom_src) is None:
            print("未匹配到源，请重新选择")
            return Select_src()
        else:
            return custom_src
    # 正确选择了数字
    elif n in [str(j + 1) for j in range(len(src))]:
        return src[int(n) - 1]
    # 选择不在范围内
    else:
        print("输入值不在范围内，请重新输入")
        return Select_src()


# 文件写入函数
def pip(s):
    # 生成源的内容
    l = re.search('(?<=//).*?(?=/)', s)
    content_src = "[global]\nindex-url = " + s + "\n[install]\ntrusted-host = " + l.group() + "\n"
    # 文件夹创建
    try:
        os.mkdir(".pip")
    except FileExistsError:
        print("文件夹已存在，直接修改配置文件\n")
    # 配置的写入
    try:
        # 定义当配置已存在时的选择函数
        def w_or_a():
            choose_wa = input("请选择一项：")
            if choose_wa == "1":
                with open(".pip/pip.conf", "a") as f:
                    f.write(content_src)
            elif choose_wa == "2":
                with open(".pip/pip.conf", "w") as f:
                    f.write(content_src)
            else:
                return w_or_a()

        # 若配置文件存在则让用户选择
        if os.path.exists(".pip/pip.conf"):
            print("检测到配置文件已存在！\n[1]追加配置 [2]直接覆盖\n")
            w_or_a()
        else:
            with open(".pip/pip.conf", "w") as f:
                f.write(content_src)
        # 创建结束
        print("\n成功创建文件!\n")

    except OSError:
        print("\n文件修改失败，请检查文件夹异常!\n")


# 源与对应的描述
src = ["https://pypi.tuna.tsinghua.edu.cn/simple/",
       "http://mirrors.aliyun.com/pypi/simple/",
       "http://pypi.mirrors.ustc.edu.cn/simple/",
       "http://pypi.hustunique.com/",
       "http://pypi.douban.com/simple/"]
detail = ["清华", "阿里", "中科大", "华科大", "豆瓣"]

# 初始化完毕，程序起始
print("-----pip换源器-----\n适用于linux下pip换源\n在用户文件夹内运行可为指定用户换源")

# 列出可选的源
print("-------可选的源-------")
for i in range(len(src)):
    print("[{}]".format(i + 1) + detail[i] + "：" + src[i])
print("[n]自定义输入，注意格式应与列表内相同")

# 开始选择
use_src = Select_src()
# 文件写入
pip(use_src)
# 程序结束
input("按下Enter退出...")
