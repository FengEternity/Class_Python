# 1
'''
使用 time 函数库中的函数求当前系统的日期，并计算出当前是本年度的第几天
'''
'''
import time

date_today = time.localtime()
print(
    f"当前系统的日期为: {date_today.tm_year}-{date_today.tm_mon}-{date_today.tm_mday}")
print(f"当前日期是本年度的第 {date_today.tm_yday} 天")
'''

# 2
'''
使用 randon 函数库中的函数产生两个 100 以内的随机函数，并判断他们是否互质
'''
'''
import random

# 辗转相除法判断互质
def gcd(a,b):
    if a ==1 or b ==1:
        print("True")
        return True
    while(1):
        t = a %b
        if t == 0:
            break
        else:
            a = b
            b = t
    if b > 1:
        print("False")
        return False
    else:
        print("True")
        return True

if __name__=="__main__":
    a = random.randint(1,99)
    b = random.randint(1,99)
    gcd(2,4)
'''
# 3
'''
编写判断素数的函数并找出前 5 个默尼森数。
P 是素数且 M 也是素数，并且满足等式 M=2^p-1 ,则称 M为莫尼森数。例如,P=5,M=2^p-1=31,5和31都是素数，因此31是莫尼森数。
'''
'''
from math import sqrt

def isPrime(x):
    # 判断素数

    if x == 1:
        return False
    k = int(sqrt(x))
    for j in range(2,k+1):
        if x %j == 0:
            return False
    return True

def monisen(n):
    # 判断莫尼森数

    count = 0
    P = 2
    res_list = []

    while count != n:
        if isPrime(P) == 1:
            M = 2**P-1
            if isPrime(M) == 1:
                res_list.append(M)
                count += 1
        P += 1
    return res_list

if __name__ =="__main__":

    res_list = monisen(5)
    print(res_list)
'''

# 4
'''
有一个咖啡列表['32Latte','_Americano30','/34Cappuccino','Mocha35'],
列表中每一个元素都是咖啡名称、价格和一些其他非字母字符组成，编写一个函数 clean_list() 处理此咖啡列表，处理后列表中只含咖啡名称，并将此列表返回。
__main__ 模块中初始化咖啡列表，调用 clean_list() 函数获得处理后的咖啡列表，并将咖啡名称进行编号后输出，输出形式如下：
1 Latte
2 Americano
3 Cappuccino
4 Mocha
'''
'''
import numbers

def clean_list(t_list):
    # 获得处理后的咖啡列表，并将咖啡名称进行编号后输出

    for i,j in enumerate(t_list):
        print(i+1,end=" ")
        for k in j:
            if ord(k) >=65 and ord(k) <= 90:
                print(k,end="")
            elif ord(k) >= 97 and ord(k) <= 122:
                print(k,end="")
        print("\n")

if __name__ == "__main__":
    test_list = ['32Latte','_Americano30','/34Cappuccino','Mocha35']
    clean_list(test_list)
'''


# 5
'''
有5个好朋友小明、阿花、大壮、大毛和小毛他们的QQ号分别是88888、5555555、11111、1234321和1212121，用字典将这些数据组织起来，实现如下程序功能;
(1) 定义函数 find_QQ() ，功能是根据主调函数传入的存放姓名和对应QQ号的字典及某个人的姓名在字典中查找对应的QQ号，
若找到，则返回该QQ号；若找不到，则返回None
(2)定义函数 find_luckyguys() ,查询所有拥有QQ靓号（5位数或小于5位数）的人的姓名，将其放入一个列表中，返回该列表。
(3)在__main__模块中创建一个包含5个好朋友姓名和对应QQ号的字典，输入要查询的姓名调用 find_QQ() 函数，如果找到，则输出该QQ号；
   如果输入的姓名不在字典中，则输出提示信息允许再次输入并调用 find_QQ() 函数查询；
   如果输入3次仍未找到，则结束查询；
   调用 find_luckguys() 函数，输出所有拥有QQ靓号的人的姓名
'''
'''
def find_QQ(res_name,tes_dict):
    # 查找姓名对应的QQ
    # 返回 QQ

    for key,val in tes_dict.items():

        if key == res_name:
            print(f"QQ号为 {val}")
            return val
    return None   # 当循环中所有元素都不匹配时，返回 None


def find_luckyguys(tes_dict):
    # 查询靓号

    res_list = []
    for key,val in tes_dict.items():
        if len(val) <= 5:
            res_list.append(val)

    return res_list



if __name__ == "__main__":
    name_list = ["小明","阿花","大壮","大毛","小毛"]
    QQ_list = ["88888","5555555","11111","1234321","1212121"]
    mes_dict = dict(zip(name_list,QQ_list))

    for i in range(3):
        test_name = input("输入需查询的姓名：")
        res = find_QQ(test_name,mes_dict)
        if res != None:
            break
        else:
            print("查询姓名不存在，请重新查询")
    else:
        print("查询三次仍不存在，结束查询")

    print(find_luckyguys(mes_dict))
'''

# 6
'''
字符串有一个 isidentifier() 方法，功能是用来判断给定的字符串是否为合法的标识符，请自行实现此方法的相似功能，定义一个函数 isIdentifier() ,
函数从 __main__ 模块中接收参数 s ，判断 s 是否为合法标识符，输出判断结果的信息：
(1)若合法，则输出'Valid identifier.';
(2)若首字母不合法，则输出'Error. First char must be alphas or number.';
(3)若首字母合法而其他字符不合法，则输出'Error.Other chars must be alphas number or _.'
'''
'''
pytohn 合法标识符命名规范：
    1. 标识符是由字符(A-Z和a-z)、下划线和数字组成，但第一个字符不能是数字；
    2. 标识符不能和 python 中的保留字相同
    3. Python 标识符中，不能包含空格、@、% 以及 $ 等特殊字符
'''


from tkinter import E


def isIdentifier(s):

    a = (ord(s[0]) >= ord("A") and ord(s[0]) <= ord("Z"))  # 判断首字符是否在 A-Z 之间
    b = (ord(s[0]) >= ord("a") and ord(s[0]) <= ord("z"))  # 判断首字符是否在 a-z 之间
    c = (ord(s[0]) >= 48 and ord(s[0]) <= 57)              # 判断首字符是否为数字

    if a == True or b == True or c == True:
        for i in s:
            e = (ord(i) >= ord("A") and ord(i) <= ord("Z"))
            f = (ord(i) >= ord("a") and ord(i) <= ord("z"))
            g = (ord(i) >= 48 and ord(i) <= 57)
            if e == True or f == True or g == True  or ord(i) == 95:
                continue
            print("Error.Other chars must be alphas number or _.")
            return False
    else:
        print("Error. First char must be alphas or number.")
        return False
    


if __name__ == "__main__":
    s=input("输入待判断的标识符：")
    if isIdentifier(s) != False:
        print("Valid identifier.")
