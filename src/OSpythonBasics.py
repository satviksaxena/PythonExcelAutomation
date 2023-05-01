import os
import shutil
import glob
import pandas as pd
class Basics:
    def commands(self):
        cwd=os.getcwd()
        print(cwd)

        # move file in python
        os.rename(os.path.join(cwd,"Test","01-2014.xlsx"),os.path.join(cwd,"Test","2014","01-2014.xlsx"))
        # os.replace(os.path.join(cwd,"Test","01-2014.xlsx"),os.path.join(cwd,"Test","2014","01-2014.xlsx"))

        os.chdir("/")
        # shutil.copy("src.txt","destination.txt")

        filenames= glob.glob("*")

        # all file which end with 2016
        filenames= glob.glob("*2016.xlsx")

        # all file which has 2016
        filenames = glob.glob("*2016*")

        # Search among 3 level of folders
        all_xlsx=glob.glob(cwd+"\\*\\*\\*.xlsx")


    def moveFilesIntoFolder(self):
        cwd=os.getcwd()
        os.chdir(os.path.join(cwd,"Test"))
        cwd=os.getcwd()
        print(cwd)

        filenames=glob.glob("*.xlsx")

        for file in filenames:
            year=file.split(".")[-2][-4:]
            try:
                int(year)
            except:
                continue

            if os.path.isdir(year)== False:
                os.mkdir(year)

            os.rename(file,os.path.join(cwd,year,file))

    def readFileFromFolderAndAddToOneXLSX(self):
        cwd = os.getcwd()
        os.chdir(os.path.join(cwd, "Test"))

        filenames=glob.glob(cwd+"\\*\\*xlsx")

        consolidated= pd.DataFrame(columns = pd.read_excel(filenames[0]).columns)
        for file in filenames:
            temp=pd.read_excel(file)
            consolidated=consolidated.append(temp,ignore_index = True)

        consolidated.to_excel("consolidated.xlsx")
