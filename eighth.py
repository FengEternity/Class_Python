# 1 and 2
'''
class BMI:
    '身体质量指数'

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.BMI = self.weight/(self.height*self.height)

    def printBMI(self):
        res = round(self.BMI, 1)
        print(f"BMI为{res}")


class ChinaBMI(BMI):
    def printBMI(self):
        res = round(self.BMI, 1)
        classification = ['偏瘦', '正常', '偏胖', '肥胖', '重度肥胖']
        dangerous = ['低（但其他疾病危险性高）', '平均水平', '增加', '中度增加', '严重增加']
        if res < 18.5:
            print(
                f"BMI:{res}\nBMI分类:{classification[0]}\n相关疾病发病的危险性:{dangerous[0]}")
        elif res >= 18.5 and res <= 23.9:
            print(
                f"BMI:{res}\nBMI分类:{classification[1]}\n相关疾病发病的危险性:{dangerous[2]}")
        elif res >= 24 and res <= 26.9:
            print(
                f"BMI:{res}\nBMI分类:{classification[2]}\n相关疾病发病的危险性:{dangerous[3]}")
        elif res >= 27 and res <= 29.9:
            print(
                f"BMI:{res}\nBMI分类:{classification[3]}\n相关疾病发病的危险性:{dangerous[4]}")
        elif res >= 30:
            print(
                f"BMI:{res}\nBMI分类:{classification[4]}\n相关疾病发病的危险性:{dangerous[5]}")


if __name__ == '__main__':
    test = ChinaBMI(55, 1.68)
    test.printBMI()
'''

# 3
from math import sqrt
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __sub__(self,other):
        return sqrt((self.x-other)*(self.x-other)+(self.y-other)*(self.y-other))

if __name__ == '__main__':
    print(Point(3,4) - Point(6,0))

