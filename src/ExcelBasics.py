import pandas as pd
class ExcelBasic:
    def input(self):
        data= pd.read_excel("data.xlsx", sheet_name="Orders", header=3, index_col="Row ID")
        data.drop("Product Name", axis=1, inplace=True)

        return data

    def calculations(self):
        data = pd.read_excel("data.xlsx", sheet_name="Orders", header=3, index_col="Row ID")

        data["Postal Code"]= data["Postal Code"].astype(str)
        data["Order Date"]= data["Order Date"].astype(str)

        data["Order Date"] = pd.to_datetime(data["Order Date"], errors="raise", format="%Y-%m-%d")
        data["month"]= data["Order Date"].dt.month

        data["string date"]=data["Order Date"].dt.strftime("%b-%Y")

        # Get all the NAN values
        newdata=data[data.isna().sum(axis=1)==0]
        newdata.fillna()
        newdata.dropna()
        print(data.dtypes)
        print(data)
        print(newdata)

    def concatMergeJoin(self):
        # for stacking side by side-> concatenate
        pd.concat([nutrition,menu], axis=1, ignore_index=False)

        # for fetching among common valuesm -> merge
        menu.merge(nutrition, how="left")
        menu.merge(nutrition, how="right")
        menu.merge(nutrition, how="outer",left_on="items_menu", right_on="items")
        menu.merge(nutrition, how="inner")

        #setindex and reset index
        menu.set_index("items",inplace=True)
        menu.reset_index(drop=False, inplace=True)

        # Join -> like vlookup -> it performs the left join-> left merge
        menu.set_index("items").join(nutrition.set_index("item"))

    def dfGroupBy(self):
        mydata = self.input()
        print("Hello")
        print(mydata.groupby("Region").count())
        print(mydata.groupby(['Region','Category']).count())
        print(mydata.groupby(['Region','Category']).count().unstack())

        gp=mydata.groupby("Region")
        gp.groups  #returns the dictionary of all the values



