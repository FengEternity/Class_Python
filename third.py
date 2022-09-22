#题目1
#将原字符串（自定义）按字符的ASCII码值顺序排序后输出。
#测试数据：dfacd
#输出：acddf
# sourcery skip: avoid-builtin-shadow
'''
sorted()函数：
    1.sort 与 sorted 区别：
        (1)sort是应用在 list 上的方法, sorted 可以对所有的可迭代对象进行排序操作
        (2)list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted() 方法返回的是一个新的 list ，而不是在原来的基础上进行的操作
    2.语法:sorted(iterable,cmp=None,reverse=False)
        参数说明:llterable:可迭代对象
                cmp:比较的函数，这个具有两个参数，参数的值都是从可迭代的对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0（一般省略）
                key:主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取决于可迭代对象中，指定可迭代对象的一个元素来进行排序
                reverse:排序规则，reserve=True 降序，反之，升序
'''
'''
from ntpath import join
x = sorted(input("请输入一个字符串："))
str1 = ''.join(x)#将列表转化为字符串
print(str1)
'''

#题目2
#使用语句"mark='My GPA is:3.5.'"存储一个字符串，从字符串mark中提取出 GPA 的值3.5，结果为浮点类型。
'''
find()方法:
    str.find(str,beg=0,end=len(string))
        str:指定检索的字符串
        beg:开始索引，默认为0
        end:结束索引，默认为字符串的长度
'''
'''
mark='My GPA is:3.5.'
Aindex = mark.find("GPA")
result = mark[Aindex+7:Aindex+10]
print(result) 
'''

#题目3
#寻找字符串"I think hope is a good thing."中字符串"hope"的下标，并将字符串中的"hope"替换成其他事物，将新字符保存到变量 result 中并在屏幕上输出。
'''
replace()方法：
    str.replace(old,new[,max])
        old:将被替换的字符串
        new:新字符串，用于替换old字符串
        max:可选字符串，替换不超过 max 次
'''
'''
test  = 'I think hope is a good thing.'
Aindex = test.find('hope')
result = test.replace('hope','love')
print(result)
'''

#题目4
#某地组织了一场歌手比赛，每个歌手的得分由10位评委和观众决定，最终得分的规则是去掉10位评委所打分数的一个最高分和一个最低分，在加上所有观众评委分数后的平均值。
#评委打出的10个分数为：9、9、8.5、10、7、8、8、9、8和10，观众评委打出的综合评分为9，请计算该歌手的最终得分。
'''
aList = [9,9,8.5,10,7,8,8,9,8,10]
bList = [9]

aList.sort()#aList进行排序
aList.pop(0)#抛出下标为0的元素
aList.pop(8)
sum = 0 
#对aList列表中元素进行求和
for i in aList:
    sum+=i
sum +=bList[0] 
print(sum)
'''

#题目5
#中午去食堂打饭，已知有xiaoming、xiaoli、xiaohua、xiaohuang 这4名学生按顺序排在了队伍中等待开饭，xiaochen 因有特殊情况需要插入到队伍的第一个，xiaohua 也来打饭,排在了队伍最后一个
#请模拟队伍的变换并输出最先和最后一个打饭学生的名字
'''
insert()方法：
    list.insert(index,obj)
        index:对象 obj 需要插入的索引位置
            #当 index = -1 时，是插在倒数第二个位置的
        obj:要插入列表中的对象
'''
'''
queue = ["xiaoming","xiaoli","xiaohua","xiaohuang"]
print(queue)
queue.insert(0,"xiaochen")
print(queue)
queue.append("xiaohua")
print(queue)
FirstPerson = queue[0]
LastPerson = queue[-1]
print(FirstPerson,LastPerson)
'''

#题目6
#请写出可以生成如下整数数列的range()函数，可以利用list()函数将range()函数生成的range对象转换成列表后进行查看：
#(1)[1,2,3,4,5,6,7,8,9,10]
#(2)[10,9,8,7,6,5,4,3,2,1]
#(3)[2,4,6,8,10,12,14,16,18,20]
#(4)[5,10,15,20,25,30,35,40,45,50]
'''
print(list(range(1,11)))
print(list(range(10,0,-1)))
print(list(range(2,21,2)))
print(list(range(5,51,5)))
'''
