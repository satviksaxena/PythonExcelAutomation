import os
import pandas as pd
class ImportantFunc:
    def mufun(self):
        sales = pd.read_excel("data.xlsx", sheet_name="Orders", header=3)
        zip_income = pd.read_csv("zipcode_income.csv", engine="python", encoding='latin-1')

        my_merge= sales.merge(zip_income.loc[:,["Zip_Code","Mean"]].rename(columns={"Zip_Code":"Postal Code", "Mean":"Mean Income"}),
                              how="left", left_on="Postal Code", right_on="Postal Code")

        my_merge.drop_duplicates(subset=["Row ID"],keep= "first" ,inplace=True)

        my_merge.isna().sum()
        print(my_merge)

    def vlookup(self,left_df,right_df,left_key,right_key,right_value):
        left=pd.read_excel(left_df)
        left.reset_index(inplace=True)
        right=pd.read_csv(right_df,engine='python')
        right= right.loc[:,[right_key,right_value]].rename(columns={right_key:left_key})
        temp=left.merge(right,how="left",on=left_key)
        temp.drop_duplicates(subset=["index"],keep="first",inplace=True)
        return temp.set_index("index")



