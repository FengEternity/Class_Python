# 1
# import numpy as np
#
# test_np = np.array([(1, 2, 3, 4),
#                     (5, 6, 7, 8),
#                     (9, 10, 11, 12),
#                     (13, 14, 15, 16)])
#
# all_sum = np.array(sum(sum(test_np)))
# col_mean = np.mean(test_np,axis=0)
# row_mean = np.mean(test_np,axis=1)
#
# res = np.hstack((all_sum, col_mean, row_mean))
#     # vstack()是垂直方向上的堆叠，hstack()是水平方向上的堆叠
# print(res)

# 2
# import numpy as np
#
#
# def mul(f, g):
#     print(np.poly1d(f)*np.poly1d(f))
#     return np.poly1d(f)*np.poly1d(g)
#
#
# if __name__ == "__main__":
#     f = np.array([2., 0, -1, 1.])
#     g = np.array([1., 2., 1.])
#     mul(f, g)

# import matplotlib.pyplot as plt
# import numpy as np
#
# x1 = np.arange(0., 2., 0.1)
# y1 = np.sin(x1)
#
# x2 = np.arange(0., 2., 0.1)
# y2 = np.cos(x2)
#
# flg, ax = plt.subplots(2, 1, figsize=(15, 10))
# line, = ax[0].plot(x1, y1)
# line.set_dashes([5, 2])
# ax[0].set_title('y=sin(x)')
#
# line, = ax[1].plot(x2, y2)
# line.set_dashes([5, 2])
# ax[1].set_title('y=cos(x)')
# plt.show()


# import pandas as pd
#
#
# def find_fail(df1, df2):
#     ave_points = (df1.数学 + df1.英语 + df1.语文) / 3
#     stu_list = []
#
#     for i in range(0, len(ave_points)):
#         if ave_points[i] < 60:
#             stu_list.append(df2.电话号码[i])
#
#     return stu_list
#
#
# if __name__ == "__main__":
#     df1 = pd.read_excel(r'stu_name.xls')
#     df2 = pd.read_excel(r'stu_phonenum.xls')
#     print(find_fail(df1, df2))

# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
#
# DateFrame = pd.read_excel(r'10_5.xlsx')
# # DateFrame = DateFrame.astyle(np.float32)
# plt.boxplot(DateFrame)
# plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_1 = pd.read_table(r'C:\Users\Monty _L\Documents\GitHub\Class_Python\ml-100k\u.data', encoding='utf8', header=None)
data_2 = pd.read_table(r'C:\Users\Monty _L\Documents\GitHub\Class_Python\ml-100k\u.user', encoding='utf8', header=None)

data_1.columns = ['id', 'item id', 'rating', 'timestamp']
data_1
data_2['id'], data_2['age'], data_2['gender'], data_2['occupation'], data_2['zip code'] = data_2[0].str.split('|').str

data = pd.merge(data_1, data_2, on=['id'])

data
