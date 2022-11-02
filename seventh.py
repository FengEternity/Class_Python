# 1
'''
from math import sqrt

def isPrime(i):
    if i == 1:
        return False
    else:
        k = int(sqrt(i))
        for j in range(2,k+1):
            if i%j == 0:
                return False
        return True

if __name__ == "__main__":
    fp = open("out.txt", "a+")
    m, n = input("输入正整数m,n\n要求m<n,以','隔开:").split(",")
    for i in range(int(m), int(n)+1):
        if isPrime(i) == True:
            fp.write(str(i)+" ")
        else:
            continue
    fp.write("\n")
'''

# 2
'''
with open('date.txt','r+') as f:
    lines = f.read().splitlines()  # 按行读取文件且忽略末尾换行
    f.write("\n")
    for line in lines:
        reline = line[::-1]
        f.write(f"{line}-{reline}\n")
'''

# 3
'''
def found(test_str):
    with open('addressbook.txt','r+') as f:
        for line in f.read().splitlines():
            line = str(line)
            if test_str in line:
                print(line)
                return True

test_str = input("输入需查询姓名:")
if found(test_str) == None:
    print("Not found")
'''


# 4
'''
def RLE(line):
    line_list = list(line)
    count = 0
    for i in range(len(line_list)-1):
        # 将一个字符串分割成相同字符组成的字符串

        if line[i] != line[i+1]:
            count += 1
            line_list.insert(i+count, '#')
    res_list = ''.join(line_list).split('#')

    for j in res_list:
        print(f"{j[0]}{len(j)}", end='')


if __name__ == "__main__":
    with open('file1.txt', 'r+') as f:
        line = str(f.read())
        RLE(line)
'''

# 5
'''
strip():
    用于移除字符串首尾指定的字符串，默认为空格和换行符
'''
'''
with open('subtitles.srt','r+',encoding='utf-8') as f_read:
    with open('7_4_result.txt','a+',encoding='utf-8') as f_write:
        new = []
        for line in f_read.readlines():
            if line[0] not in list('\n0123456789') and line[-2] not in list('0123456789'):
                new.append(line)
        new = [ele.strip() for ele in new]

        for line in new:
            f_write.write(line+'\n')
'''


# 6
