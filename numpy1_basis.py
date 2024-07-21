import numpy as np

# selector = "-----------------------"
# data = np.array([[1, -2, -4, 5], [4, 8, 3, 2]])
# print(data)
# print(selector)
#
# print(data*data)
# print(selector)
#
# print(data+10)
# print(selector)

print(np.arange(100))
print(np.zeros(12, dtype=int))
print(np.empty(12, dtype=int))

print(np.zeros_like(12, dtype=int))
print(np.empty_like(12, dtype=int))

print(np.full((2, 3), 4))
print(np.eye(4, 4))

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

float_arr = arr.astype(np.float64)
print(float_arr.dtype)

print(arr * arr)

arr = np.arange(10)
print(arr[5])
print(arr[5:8])
arr[5:8] = 12
print(arr)

arr_slice = arr[5:8]
print(arr_slice)

arr_copy = arr[4:8].copy()
print(arr_copy)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])
print(arr2d[2][1])

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])
print(arr3d[1, 0])

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

data_names = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])

print(names, data_names)
print(" ")
print(data_names[(names == 'Will')])
print(" ")
print(data_names[~(names == 'Will')])  #Tylda jest odwróceniem ogólnego warunku
print(" ")
print(data_names[names != 'Bob'])
print(" ")

mask = (names == 'Bob') | (names == 'Will')
print(" ")
print(mask)

mask2 = (names == 'Bob') & (names == 'Will')
print(" ")
print(mask2)

data = np.arange(-11, 12)
print(data)

data[data < 0] = 0
print(data)

data[names != 'Bob'] = 7
print(data)
