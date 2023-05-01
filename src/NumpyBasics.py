import numpy as np


class Basics:

    def __init__(self):
        pass

    def func(self):
        py_list=[3,12,24,9]
        np_array= np.array(py_list)
        np_array*=3
        zero_array= np.zeros(4)
        space_array=np.linspace(7,40,12)
        random_array= np.random.randint(0,13,4)
        print(np_array)
        print(zero_array)
        print(random_array)

    def funcNumpyMultiDimentional(self):
        np_2d_array= np.array([[4,5,6],[2,341,5]])
        np_2d_array=np.reshape(np_2d_array, (3,2))
        np_2d_array=np_2d_array.flatten()
        print(np.shape(np_2d_array))
        print(np_2d_array)

    def funcMethods(self):
        np_2d_array= np.array([[4,7,6],[2,341,5]])
        # np.sort makes a copy
        # sorted_array=np.sort(np_2d_array)

        #axis =1 is default row, axis 0 is column wise
        sorted_array=np.sort(np_2d_array,axis=1)
        np_2d_array.sort()
        print(np_2d_array)
        # print(sorted_array)


