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

import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(0., 2., 0.1)
y1 = np.sin(x1)

x2 = np.arange(0., 2., 0.1)
y2 = np.cos(x2)

flg, ax = plt.subplots(2, 1, figsize=(15, 10))
line, = ax[0].plot(x1, y1)
line.set_dashes([5, 2])
ax[0].set_title('y=sin(x)')

line, = ax[1].plot(x2, y2)
line.set_dashes([5, 2])
ax[1].set_title('y=cos(x)')
plt.show()
