import pandas as pd

df = pd.DataFrame({
    "column1": [1, 2, 3],
    "column2": [4, 5, 6]
})

df.to_csv("output.csv", index=False)