# 1
"""
try:
    # AttributeError
    # a_list = (1, 2)
    # a_list.append(3)

    # IndexError
    # aList = []
    # print(aList[1])

    # KeyError
    # test = {'a': '1'}
    # print(test['d'])

    # NameError
    # print(a)

    # SyntaxError
    # 2 += 1

    # TypeError
    # a = {'test': 1}
    # a.values('Error')

    # ValueError
    # int("asdasf")

    pass

except AttributeError:
    print("AttributeError")
except IndexError:
    print("IndexError")
except KeyError:
    print("KeyError")
except NameError:
    print("NameError")
except SyntaxError:
    print("SyntaxError")
except TypeError:
    print("TypeError")
except ValueError:
    print("ValueError")
"""


# 2
# test_list = [2, 3, 4, 1, 4, 4, 6]
# while True:
#     try:
#         test_list = sorted(test_list)
#         index = int(input("输入要弹出元素的索引："))
#         test_list.pop(index)
#         print(test_list)
#     except:
#         print("Error")
#         break

# 3
# while True:
#     try:
#         num = int(input("输入面包个数："))
#         price = eval(input("输入单价："))
#         print(f"价格总额为：{price*num}")
#     except ValueError:
#         print("Please input a True number")
#     else:
#         break

# 4
# 不是很明白题目啥意思，好抽象啊
#
# while True:
#     try:
#         name = input("Enter name:")
#         age = int(input("Enter age:"))
#         res = zip([name], [age])
#         print(res)
#     except ValueError:
#         print("Error")
#     else:
#         print(f"name:{name},age:{age}")
# 5
# while True:
#     try:
#         s = str(input("输入四则运算表达式："))
#         print(eval(s))
#     except:
#         break
#     finally:
#         judge = input("输入‘0’中止程序\n或输入任意键继续\n")
#         if judge == "0":
#             break
#

# 6
#
# user_dict = {'xiaoming': '1003', 'xiaohua': '1011', 'xiaoteng': '1045', 'xiaoyi': '1047', 'xiaoyang': '1051'}
# while True:
#     try:
#         user_name = input("Enter name:")
#         user_ID = user_dict.get(user_name)
#         if user_ID is None:
#             raise Exception
#         print(f"该用户ID为：{user_ID}")
#     except Exception as e:
#         print("未查询到该用户姓名")
#     else:
#         break

# 7
def countLines(fname):
    try:
        with open(fname) as f:
            date = f.readlines()
    except FileNotFoundError:
        print(fname + " does not exist")
    else:
        lens = len(date)
        print(fname + ' has ' + str(lens) + ' lines')


if __name__ == '__main__':
    fname = 'date.txt'
    countLines(fname)
