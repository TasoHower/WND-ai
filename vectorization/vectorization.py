import numpy as np

def test_dot_func():
    w = np.array([1,2,3])
    x = np.array([4,5,6])
    b = 30

    result = np.dot(w,x)+b # np.dot 使用向量乘法

    print(result == 62)

test_dot_func()
