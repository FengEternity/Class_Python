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
'''
with open('article.txt', 'r') as f:
    article_str = f.read()
    article_str = article_str.lower()
    word_list = article_str.split()
    pop_list = []
    # print(len(word_list))
    count = 0

    for word in word_list:

        # 將含有非26字母字符的元素輸出
        # word_list:儲存全是字母的元素
        # pop_list:儲存含非字母元素
        # 輸出正確,則len(word_list)=len(word_list)+pop_list    (後一個word_list為pop后的)

        for i in word:
            if ord('a') <= ord(i) <= ord('z'):
                continue
            else:
                word_list.pop(count)
                pop_word = word.replace(i, '')
                pop_list.append(pop_word)
        count += 1
    # print(len(word_list))
    # print(len(pop_list))

    res_list = word_list + pop_list
    res = max(res_list,key=len)
    print(res)

'''

# 7


def find(digit):
    with open('date2.txt', 'r') as f:
        sum_list = []
        line_list  = f.read().splitlines()

        for line in line_list:
            digit_list = []

            for i in line:
                if ord(i) >= ord('0') and ord(i) <= ord('9'):
                    digit_list.append(i)

            sum = 0
            for j in digit_list:
                sum += int(j)
            sum_list.append(sum)

            if digit in sum_list:
                print(f"行数：{int(sum_list.index(digit))+1}\n对应数据为:{line_list[int(sum_list.index(digit))]}")
                return True


if __name__ == "__main__":
    digit = int(input("輸入待查詢整數："))
    if find(digit) == None:
        print("輸入數字不滿足題意")
