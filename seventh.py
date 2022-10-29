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
with open('addressbook.txt','r+') as f:

    test_str = input("输入需查询姓名:")
    lines = f.read().splitlines()
    print(lines)
    if test_str in f:
        print("Y")
    else:
        print("N")


