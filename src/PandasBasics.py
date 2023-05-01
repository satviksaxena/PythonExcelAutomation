import pandas as pd
import numpy as np

class PandasBasics:

    def func(self):
        # Series object
        np_array = np.array([2,6,1,3])
        pd_series= pd.Series(np_array)
        pd_series= pd.Series(np_array, index=["a","b","c","d"])# instead 012 index will be abc
        # pandas series is numpy array with index

    def funcDataFrame(self):
        # while using np.array
        mydf=pd.DataFrame(np.array([[1,2,3],
            [4,5,4],
            [7,8,9]]),
             columns=["a","b","g"]
             )
        print(mydf)


        #Normal way of doing it
        df= pd.DataFrame({
            'a':[1,2,3],
            'b':[6,7,8],
            'c':[4,8,5]
        })
        df.index=["m","n","o"]
        print(df)
        print(type(df["a"]))
        print(df.loc["n","c"])
        print(df.loc["n":,"b":])




