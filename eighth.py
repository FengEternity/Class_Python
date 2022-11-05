# 1
class BMI:
    '身体质量指数'
    def __init__(self,weight,height):
        self.weight = weight
        self.height = height
        self.BMI = self.weight/(self.height*self.height)

    def printBMI(self):
        res = round(self.BMI,1)
        print(f"BMI为{res}")

class ChinaBMI(BMI):
    def __init__(self)
test = BMI(55,1.68)
test.printBMI()