# 第 6 题
'''
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
