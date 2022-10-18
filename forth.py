#题目一
#基于下表创建一个国家（键）和语言（值）映射的词典 nations ，完成如下操作：
#国家      语言      国家       语言
#China    Chinese   USA       English   
#France   French    Germany   German
#（1）显示字典的所有键
#（2）显示字典的所有值
#（3）显示字典的所有项
#（4）获取键'France'对应得值
#（5）创建一个新字典{'Spain':'Spanish','Japan':'Japamese'},将其加入字典 nations 中。
# sourcery skip: dict-assign-update-to-union
'''
update()函数：
    dict.update(dict2)
    #dict2:添加到指定字典 dict 里的字典
    #需要注意的是，有相同的键会被直接替换成 dict2中的值 
'''
'''
nations = {'China':'Chinese','USA':'English','France':'French','Germany':'German'}
print(nations.keys())#返回键
print(nations.values())#返回值
print(nations.items())#返回键值对
print(nations.get('France'))#返回键对应的值

NewNations = {'Spain':'Spanish','Japan':'Japamese'}
nations.update(NewNations)
print(nations)
'''

#题目二
#已知有三位学生参加了主题演讲得记录列表：
#names = ['xiaoma','xiaowang','xiaoma','xiaoliu','xiaoma','xiaoliu']
#请统计出每个学生参加活动的次数并记录到字典中，结果如下（顺序不做要求）：
#{'xiaowang':1,'xiaoma':3,'xiaoliu':2}
'''
get()函数：
    dict.get(key,default=None)
    参数：
        key:字典中要查询的键
        default:如果指定键不存在时，则返回该默认的值
'''

'''
names = ['xiaoma','xiaowang','xiaoma','xiaoliu','xiaoma','xiaoliu']
counts = {}
for i in names:
    counts[i] = counts.get(i,0)+1
print(counts)
'''


#题目三
#创建一个字典 users ,字典中保存了某一个网站已经注册的账号（用户名和密码对），查找是否存在用户'xiaoming'，若用户名存在则输出其密码，否则输出“not found”。

#users = {'xiaoming':'zxcv','xiaoming':'asdf'}#等同于users = {'xiaoming':'asdf'}
'''
users = {'xiaoming':'zxcv'}
if 'xiaoming' in users:
    print(users.values())
else:
    print('not found')
'''


#题目四
#已知有两个集合 footballSet 和 basketballSet ，分别存储选择了足球兴趣小组和篮球兴趣小组的学生姓名，请自行构建集合数据，计算并输出如下信息：
#（1）选了两个兴趣小组的学生姓名和人数；
#（2）仅选了一个兴趣小组的学生姓名和人数
'''
footballSet = {'a','b','c','d','e'}
basketballSet = {'a1','b','c','d1','e1'}

BothSet = footballSet & basketballSet
Soleset = footballSet ^ basketballSet

print(BothSet,len(BothSet))
print(Soleset,len(Soleset))
'''

