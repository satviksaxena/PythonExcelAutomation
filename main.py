# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from src.NumpyBasics import Basics
from src.PandasBasics import PandasBasics
from src.ExcelBasics import ExcelBasic
from src.Assignment import NumpyAssignment,PandasAssignment
from src.OSpythonBasics import Basics
from src.ImportantFunctions import ImportantFunc
from src.AdvancedFunc import Advance
from src.Visualization import Visual

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#todo

if __name__ == '__main__':
    print_hi('PyCharm')
    # obj = Basics()
    # obj.func()
    # obj.funcNumpyMultiDimentional()
    # obj.funcMethods()

    # obj= PandasBasics()
    # obj.funcDataFrame()


    # obj = ExcelBasic()
    # obj.dfGroupBy()

    # obj = PandasAssignment()
    # obj.solution()

    # obj = Basics()
    # obj.readFileFromFolderAndAddToOneXLSX()

    # obj = ImportantFunc()
    # obj.vlookup("data.xlsx","commute.xlsx","Postal Code","Zip_Code","Mean")

    # obj = Advance()
    # obj.pivotTable()
    # obj.if_function()
    # obj.applyStringFunc()

    obj= Visual()
    # obj.basics()
    obj.advanceExcelPlotting()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
