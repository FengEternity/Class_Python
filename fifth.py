# 第 6 题
'''
题目：
    从键盘上输入一个字符串，用字典相关方法来统计每个字母（按字母顺序，且不区分大小写）出现的次数。例如，字符串“I am a student.”的统计结果为[2,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,2,1,0,0,0,0,0] \
    表示字符'A'或'a'共出现了2次，字符'D'或'd'共出现了1次，依此类推。
'''
'''
# 实现对列表的切片
def dict_slice(adict, start, end):
    keys = adict.keys()
    dict_slice = {}
    for k in list(keys)[start:end]:
        dict_slice[k] = adict[k]
    return dict_slice


test = input("输入一个字符串：")
test = test.lower()


dict = {}.fromkeys((chr(i) for i in range(97,123)),0) #生成26个字母的字典

for j in test:
    if j not in dict:
        dict[j] = 1
    else:
        dict[j] += 1
        
res = dict_slice(dict,0,26)

print(res.values())
'''


# 第 7 题
'''
题目：
    从键盘输入一个 2-1000 之间的整数 n , 对其进行指数分解，输出分解后的式子。
'''
'''
x = int(input("请输入一个数："))
print(x ,'= ',end=' ')

temp = [] 
while x!=1:
    for i in range(2,x+1):
        if x % i == 0:
            temp.append(i) 
            x = x // i
            break

for i in range(len(temp)):
    if i!=len(temp)-1:
        print("%d * " % temp[i],end='')
    else:
        print("%d " % temp[i],end='')
'''

# 第 8 题
'''
题目：
    验证命题：如果三个整数是 37 的倍数，则这个整数循环左移后得到的两个三位数也是 37 的倍数。\
    命题为真则输出“这是一个真命题”；命题为假则输出“这是一个假命题”。
'''
'''
test = []

# 生成所有 37 倍数的三位整数
for i in range(0,1000):
    if i*37 > 99 and i*37 < 1000:
        test.append(i*37)
    else:
        continue
res = []
for j in test:
    a = j//100 # 个位
    b = j%100//10 # 十位 
    c = j%100%10 # 百位

    res_1 = b*100 + c*10 + a
    res_2 = c*100 + a*10 + b
    res.append(res_1)
    res.append(res_2)
    
for k in res:
    if k < 100 or k > 999: # 判断左移后存在 0 的数字
        continue
    if k%37 != 0 and k%37 != 0:
        print("这是一个假命题")
    else:
        print("这是一个真命题")

# 保留问题：如何只输出一个 “这是一个真命题”
'''

# 第 9 题
'''
题目：
    黑洞数（Kaprekar 问题）又称陷阱数，是具有奇特转换特性的整数，对于任何一个数字不全相同的 4 位整数，\
    经有限“重排求差”操作例如把组成该数的数字的数字重排后得到的最大数减去重排后的最小数得到一个新数\
    （在过程保持数字位数都是 4 ，不足根据数值补 0 ，例如一个 4 位 456 补 0后得到 0456），\
    反复执行如下操作，最后一定会得到 4 位数的黑洞数 6174 。输入一个 4 位正整数计算并输出到达黑洞数 6174 的完整过程，\
    若输入的 4 位整数各位数字完全相同则直接输出形如“X-X=0000”的表达式。
'''
'''
n = [x for x in input("请输入一个 4 位整数：")]

while len(n)<4:
    n.insert(0,'0')

if n[0] == n[1] and n[1] == n[2] and n[2] == n[3]:
    print(n[0]*4,'-',n[0]*4,'= 0000',end='')

else:
    while n!='6174':   
        a = sorted(n,reverse=True)
        b = sorted(n)
        a = a[0]+a[1]+a[2]+a[3]
        b = b[0]+b[1]+b[2]+b[3]
        n = int(a)-int(b)
        if n<1000:
            print(a,'-',b,'=','0'+str(n))
            n = '0'+str(n)
        else:
            print(a,'-',b,'=',n)
            n = str(n)
'''
