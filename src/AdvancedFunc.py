import os
import glob
import pandas as pd
import numpy as np
class Advance:
    def pivotTable(self):
        cwd = os.getcwd()
        filenames= glob.glob(cwd+"\\Test\\*\\*xlsx")
        print(filenames)
        consolidated= pd.DataFrame(columns= pd.read_excel(filenames[0].columns))

        for file in filenames:
            temp=pd.read_excel(file)
            consolidated = consolidated.append(temp,ignore_index=True)

        columns =["Region"]
        rows=["segment","Category","Sub-Category"]
        values = ["Profit"]

        relevant_df = consolidated.loc[:,columns+rows+values]
        # //unstack -> unstack the last row in the columns
        pivot_df = relevant_df.groupby(rows+columns).sum().unstack([-1,-2])
        pivot_df.to_excel("pivot.xlsx")

    def if_function(self):
        sales_data= pd.read_excel("data.xlsx",sheet_name="Orders", header=3, index_col="Row ID")
        sales_data["Profit after TAX"] = np.where(sales_data["Category"]=="Furniture",0.8*sales_data["Profit"],
                                                  np.where(sales_data["Category"] == "Office Supplies",
                                                           0.7 * sales_data["Profit"],
                                                           np.where(sales_data["Category"] == "Technology",
                                                                    0.7 * sales_data["Profit"],
                                                                    0
                                                  )))
        print(sales_data)

    def applyStringFunc(self):
        sales_data = pd.read_excel("data.xlsx", sheet_name="Orders", header=3, index_col="Row ID")
        # use STR functions to enable all the string functionality

        #to extract from 3 to 6 characters
        mydata=sales_data["Order ID"].str[3:7] #mid
        #first two-> left
        mydata=sales_data["Order ID"].str[:2]
        #last two -> right
        mydata=sales_data["Order ID"].str[-2:]

        mydata=sales_data["Order ID"].str.split("-").str[1]

        #Trim ->>> strip
        sales_data["Order ID"].str.strip()

        #concatenate
        sales_data["Location"] = sales_data["State"] + "_" + sales_data["City"]
        sales_data["Location"].str.upper()
        sales_data["Location"].str.lower()
        sales_data["Location"].str.find("Fort") # gives 0 and -1

        # String fuctions-> countif
        # Count of quantity > 5
        len(sales_data[sales_data["Quantity"]>5])
        count_qt = sales_data[sales_data["Quantity"]>5].shape[0]
        count_qt_and_kentucky= len((sales_data[sales_data["Quantity"]>5]) & (sales_data["Quantity"] > 5))

        #Imp Filter data
        sales_data[sales_data["City"].str.contains("Fort")]
        #Starts with Fort
        sales_data = sales_data[sales_data["City"].str[:4] == "Fort"]
        # Get all fort and on its profit do sum
        sales_data = sales_data[sales_data["City"].str[:4] == "Fort"]["Profit"].sum()

        #above using loc
        sales_data = sales_data.loc[sales_data["City"].str[:4] == "Fort","Profit"].sum()

        print(mydata)
