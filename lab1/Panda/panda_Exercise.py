import pandas as pd
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)


# print(df)

ages = df["Age"]

# print(ages)

ages = pd.Series([22, 35, 58], name="Age")

# print(ages)
# print(ages.max())
print(df.describe())
