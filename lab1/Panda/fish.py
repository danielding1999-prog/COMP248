import pandas as pd


def LoadData(filename):
    df = pd.read_csv(f"{filename}")
    return df

def CalculateAverageLength(df):
    df["Average Length"] = (df["Length1"] + df["Length2"] + df["Length3"]) /3

avg_length_specie = df.groupby("Species").mean()
print(avg_length_specie)

