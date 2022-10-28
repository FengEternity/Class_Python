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


