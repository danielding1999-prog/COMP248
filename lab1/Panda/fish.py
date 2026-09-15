import pandas as pd
import numpy as np



def LoadData(filename):
    df = pd.read_csv(f"{filename}")
    return df

def CalculateAverageLength(df):
    df["Average Length"] = (df["Length1"] + df["Length2"] + df["Length3"]) /3

# avg_length_specie = df.groupby("Species").mean()
# print(avg_length_specie)

def CalculateFishIndex(df):
    df["Mass Index"] = (df["Height"] / df["Weight"])
    
def GenerateColumnDtypes(df):
    x = ""
    dfOBJ = df.dtypes
    for columnName, dtypes in dfOBJ.items():
        x += (f"Column Name: {columnName}, Column Type: {dtypes}\n")
    return x

def GenerateColumnNullNum(df):
    dfOBJ = df.dtypes
    
def GenerateReport(df):
    row, column = df.shape
    print(f"Number of Rows: {row}, Number of Columns: {column}")
    
def main():
    fishDF = LoadData("Fish.csv")
    CalculateAverageLength(fishDF)
    CalculateFishIndex(fishDF)
    # print(fishDF.dtypes)
    # fishObj = fishDF.dtypes
    # print(fishObj)
    # for column, dtypes in fishObj.items():
        # print(f"Column Name: {column}, Column Type: {dtypes}")
    # print(fishObj.items())
    # print(fishDF.isnull())
    # print(GenerateColumnDtypes(fishDF))
    x = (True, True, False)
    a = sum(x)
    print(a)
if __name__ == "__main__":
    main()
