# 第 6 题
'''
从键盘上输入一个字符串，用字典相关方法来统计每个字母（按字母顺序，且不区分大小写）出现的次数。例如，字符串“I am a student.”的统计结果为[2,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,2,1,0,0,0,0,0] \
表示字符'A'或'a'共出现了2次，字符'D'或'd'共出现了1次，依此类推。
'''
'''
test = input("输入一个字符串：")
test = test.lower()

dict = {}.fromkeys((chr(i) for i in range(97,123)),0) #生成26个字母的字典

for j in test:
    if j not in dict:
        dict[j] = 1
    else:
        dict[j] += 1

print(dict.values())
    
# 保留问题：取出字典的前 n 个值
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
