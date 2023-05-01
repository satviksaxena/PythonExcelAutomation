import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
class Visual:
    def basics(self):
        sales_data = pd.read_excel("data.xlsx", sheet_name="Orders", header=3, index_col="Row ID")
        my_plot= sales_data.groupby("Region")[["Sales","Profit"]].sum().plot(
            kind="bar",
            title="Regional Sales and Profits",
            subplots= True,
            layout = (1,2),
            sharey = True
        )
        # plt.show()
        my_plot= sales_data.groupby("Region")[["Sales","Profit"]].sum().plot(
            kind="bar",
            title="Regional Sales and Profits",
            stacked = True
        )
        plt.show()

    def advancePlotting(self):
        #The link of all the plots are here https://matplotlib.org/2.0.2/faq/usage_faq.html
        # object figure (diagram) has multiple axes class

        fig=plt.figure()

        ax1 = fig.add_axes([0,0,1,1])# left right width height last 1,1 gives complete
        ax2 = fig.add_axes([0.15,0.7,0.48,1])

        x=np.arange(1,10)
        ax1.plot(x,(x**2),color="r")
        ax2.plot(x, np.log(x) , ls = "--")

        plt.show()

    def advanceExcelPlotting(self):
        sales_data = pd.read_excel("data.xlsx", sheet_name="Orders", header=3, index_col="Row ID")
        def new_ticks(x,pos):
            return "${}k".format(round(x/1000))

        fig= plt.figure()
        fig.suptitle("City level Performance", x=0, y=1 ) #to move it left side

        #ax1
        ax1=fig.add_axes([0,0,1,0.9])
        ax1.set_title("Top Cities")
        ax1.yaxis.label.set_visible(False)  # to remove word "City" from axis
        ax1.set_xlabel("Sales")
        ax1.axvline(x=100000, color= "black", ls= "--", linewidth = 2)
        ax1.xaxis.set_major_formatter(tkr.FuncFormatter(new_ticks))

        ax2 = fig.add_axes([0.6,0.5,0.25,0.25])
        ax2.set_title("Poor Performing Cities")
        ax2.xaxis.label.set_visible(False)
        ax2.set_ylabel("Sales")

        #IMP see how axis is given in below query
        sales_data.groupby("City")["Sales"].sum().dropna().sort_values(ascending=False).iloc[:15].plot(kind="barh" , ax= ax1)
        sales_data.groupby("City")["Sales"].sum().dropna().sort_values(ascending=True).iloc[:5].plot(kind="bar" , ax= ax2)

        plt.show()
