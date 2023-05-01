import pandas as pd
import numpy as np

class NumpyAssignment:
    def input(self):
        data=pd.read_excel("commute.xlsx",sheet_name="Sales",index_col="Date")
        price= pd.read_excel("commute.xlsx", sheet_name="Price", header= None).transpose()
        return data,price

    def normalization_data(self):
        data, price = self.input()
        data.replace(["Yes","No"],[1,0], inplace=True)
        # print(data)
        # data["Date"]= pd.to_datetime(data["Date"], errors="raise", format="%Y-%m-%d")
        data_np= np.array(data)
        return data,data_np

    def normalization_price(self):
        data,price= self.input()
        price.columns=price.iloc[0]
        price=price.drop(0).reset_index( drop = True)
        price= price.iloc[0].str.extract('(\d*\.\d+|\d+)', expand=False).astype(float)
        price=np.array(price)
        # print(price)
        return price

    def solution(self):
        data_pandas,data= self.normalization_data()
        price=self.normalization_price()
        # print(data.shape)
        # print(price.shape)
        daily_expense= data.dot(price)
        total_expense=daily_expense.sum()
        maximum_expense=daily_expense.argmax()
        print(data_pandas.index[maximum_expense].strftime("%Y-%m-%d"))


class PandasAssignment:
    def input(self):
        data=pd.read_excel("data.xlsx",sheet_name="Orders",header=3,index_col="Row ID")
        return data
    def solution(self):
        data=self.input()
        data["Order Date"]=pd.to_datetime(data["Order Date"],errors="raise",format="%Y-%m-%d")

        data["month_year"]=data["Order Date"].dt.strftime("%m-%Y")
        gb=data.groupby("month_year")
        gb_list=[]
        for df in gb.groups:
            gb_list.append(gb.get_group(df))

        gb_list
        for df in gb_list:
            file_name=df["month_year"].iloc[0]
            df.to_excel(f"Test/{file_name}.xlsx".format(file_name),index=False)