import pandas as pd

df = pd.read_csv("Fish.csv")

# Calculate the average length for each species group
avg_per_species = df.groupby("Species")["Length1"].mean()
print(avg_per_species)