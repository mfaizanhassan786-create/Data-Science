## Starting the Numpy Library

# import numpy as np
# import time

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.shape)    # (2, 3)
# print(arr.ndim)     # 2
# print(arr.size)     # 6
# print(arr.dtype)    # int64 (or int32 on 32-bit platforms)
# # print(arr.itemsize) # 8 bytes (or 4 bytes for int32)  

## Time taken by Python List 

# py_list = list(range(1_000_000))
# py_result = []
# start_time = time.time()
# for i in py_list:
#     py_result.append(i + 2)
# end_time = time.time()
# print(f"Python List Time:", end_time - start_time)

## Time taken by Numpy Array 

# numpy_arr = np.array(range(1_000_000))
# numpy_result = numpy_arr + 5
# start_time = time.time()
# end_time = time.time()
# print(f"Numpy Array Time:", end_time - start_time)
