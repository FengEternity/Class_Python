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
# 题目的要求似乎并没有完全遵循 Python 命名规范
'''
pytohn 合法标识符命名规范：
    1. 标识符是由字符(A-Z和a-z)、下划线和数字组成，但第一个字符不能是数字；
    2. 标识符不能和 python 中的保留字相同
    3. Python 标识符中，不能包含空格、@、% 以及 $ 等特殊字符
'''

'''
def isIdentifier(s):

    a = (ord(s[0]) >= ord("A") and ord(s[0]) <= ord("Z"))  # 判断首字符是否在 A-Z 之间
    b = (ord(s[0]) >= ord("a") and ord(s[0]) <= ord("z"))  # 判断首字符是否在 a-z 之间
    c = (ord(s[0]) >= 48 and ord(s[0]) <= 57)              # 判断首字符是否为数字

    if a == True or b == True or c == True:
        for i in s:
            e = (ord(i) >= ord("A") and ord(i) <= ord("Z"))
            f = (ord(i) >= ord("a") and ord(i) <= ord("z"))
            g = (ord(i) >= 48 and ord(i) <= 57)
            if e == True or f == True or g == True or ord(i) == 95:
                continue
            print("Error.Other chars must be alphas number or _.")
            return False
    else:
        print("Error. First char must be alphas or number.")
        return False


if __name__ == "__main__":
    s = input("输入待判断的标识符：")
    if isIdentifier(s) != False:
        print("Valid identifier.")
'''

# 7
'''
定义一个函数 count_str() 统计给定的字符串中各个单词出现的次数并将结果存入一个字典并返回，
__main__模块中定义了一个字符串将它作为实参传入 count_str() 中进行统计，并分别按键和值的升序形式将返回的结果在屏幕上输出。
测试数据：
    str1 = "Python C++ Java Go Java PHP Python Java"
'''

'''
def count_str(test_str):
    test_list = test_str.split()
    res_dict = {}
    for i in test_list:
        if i not in res_dict:
            res_dict[i] = 1
        else:
            res_dict[i] += 1
    sort_keys = dict(sorted(res_dict.items()))
    sort_values = dict(sorted(res_dict.items(), key=lambda x: x[1]))
    print("【 按键输出 】")
    for i, j in sort_keys.items():
        print(i, j)
    print("【 按值顺序，值相同时按键顺序排序 】")
    for i, j in sort_values.items():
        print(i, j)


if __name__ == "__main__":
    str1 = "Python C++ Java Go Java PHP Python Java"
    count_str(str1)
'''

# 8
'''
自定义函数 minNum(*args) 将传入的参数中的数字（均为个位数）组成一个最小的数并返回，
要求首位不允许为0.输入几个数(可能不止一个0),调用 minNum() 函数获得组合成的最小数输出 
'''
'''
from itertools import permutations
def minNun(*args):
    num_list = list(args)
    res_0 = []
    for i in permutations(num_list, len(num_list)):
        res_list = list(i)
        res_str = "".join('%s' % id for id in res_list)
        res_0.append(res_str)

    res = []
    for i in res_0:
        if i[0] == '0':
            continue
        else:
            res.append(i)

    print(min(res))


if __name__ == "__main__":
    minNun(0, 2, 3, 3, 4, 1, 2, 0, 0)

'''
# 9
'''
将一个正整数所有数字的平方相加可得到一个新的数，不断重复这个过程直到新的数已经在之前出现过，这样构成了一个数字链。

例如：
1->1
89->145->42->20->4->16->37->58->89

理论上证明了从任一整数开始，平方和数字链最终都会到达 1 或 89,因此寻找某正整数的平方和数字链到 1 或 89 即可。
自定义函数 numsChain(num) , 寻找从 num  到 1 或 89 的平方和数字链中的所有数并将结果返回。
主模块中从键盘输入一个数字字符串（正整数），调用 numsChain() 函数寻找并输出完整的平方和数字链。
'''
'''
# 待改进
    1.最后输出时删去"->"
    2.输入 89/1 不进入循环

def numsChain(num):
    res = 0
    if num == 1 or num == 89:
        return 0
    else:   
        for i in str(num):
            res += (int(i)*int(i))
        if res != 1 or i != 89: 
            print(f"{res}->",end="")
        else:
            print(res)
        return numsChain(res)
    
if __name__ == "__main__":
    test_num = int(input("输入测试数值："))
    numsChain(test_num)
'''

# 10
'''
自定义函数函数 twonumSum(n,lst), 在列表 lst 中查找是否有两数之和等于 n , 若有则返回两数的下标，否则返回 -1 。
对于一个不包含重复数字的有序列表[1,4,5,6,7,8,9,10,11,12,13,15,18,19,20,21,29,34,54,65],
从键盘上输入 n , 调用函数 twonumSum() 输出满足条件的两个数的索引（找到一组即可且要求其中的一个数尽量小），
若所有数均不满足条件则输出"not found"
'''
import itertools


def twonumSum(n,lst):
    for i ,j in 

if __name__ == "__main__":
    lst = [1,4,5,6,7,8,9,10,11,12,13,15,18,19,20,21,29,34,54,65]
    n = int(input("测试数据n:"))
    twonumSum(n,lst)

# 11
'''
扑克牌除大王和小王外有 13 张不同牌面的牌：A、2、3、…、10、J、Q、K，
如果大于或等于五张连续的牌在一起成为顺子，自定义函数 playCard(cards) 简易模拟判断已抓的牌（大于等于 5 张，牌面只包含2-9这8张牌）中是否包含顺子（假定牌的张数为5张）并将结果返回。
__main__模块中输入一组扑克牌的牌面字符，调用 playCard() 函数，寻找并输出其中的顺子，找不到则输出对应的提示。
'''


# 12
'''
编写辗转相除法求最大公约数的递归函数。
'''

'''
def gcd(a, b):
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    a, b = input("输入两个正整数（用','隔开）：").split(',')
    print(gcd(int(a), int(b)))
'''
