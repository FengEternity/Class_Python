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
'''
from math import sqrt
class Point:
    '计算直线欧几里得距离'
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __sub__(self,other):
        res = sqrt((self.x-other.x)*(self.x-other.x)+(self.y-other.y)*(self.y-other.y))
        return res

if __name__ == '__main__':
    print(Point(3,4) - Point(6,0))

'''

# 4


class Vehiclea:
    '定义车辆类'

    def __init__(self, name_Dmv):
        '初始化车管所信息'
        self.name_Dmv = name_Dmv
        self.total = 0
        self.info = []

    def insert_Veh(self, number, entry, brand, check):
        '车辆信息添加'
        for x in self.info:
            if number in x:
                print("该车信息已添加至车管所")
                return False
        self.total += 1
        self.info.append([number, entry, brand, check])
        return True

    def del_Veh(self, number):
        '车辆信息删除'
        for x in self.info:
            if number in x:
                print(f"车牌号为{number}的车辆删除成功")
                self.info.remove(x)
                self.total -= 1
                return True
        print("该车信息在此车管所不存在")
        return False

    def search_Veh(self, number):
        '根据车牌号码查询信息'
        for x in self.info:
            if number in x:
                print(f"所查询车辆信息为：{x}")
                return True
        print("该车信息在此车管所不存在")
        return False

    def print_Veh(self):
        '输出所有车辆信息'
        print('该车管所车辆信息如下：')
        for x in self.info:
            print(x)

    def sort_Veh(self):
        '根据车牌号从小到大排序'
        def takefirst(num):
            return num[0]
        self.info.sort(reverse=False, key=takefirst)

    def sear_check(self):
        for x in self.info:
            year = (x[3])[:4]
            if year != '2022':
                print(f"{x}本年度未年检")


if __name__ == '__main__':
    car = Vehiclea("test")
    car.insert_Veh('12345', '2022/10/1', 'Audi', '2022/11/7')
    car.insert_Veh('12333', '2022/10/1', 'Cadillac', '2021/11/7')
    car.insert_Veh('12Y14', '2022/10/1', 'Lexus', '2020/11/7')
    car.del_Veh('12333')
    car.search_Veh('12Y14')
    car.sear_check()
    car.sort_Veh()
    car.print_Veh()
