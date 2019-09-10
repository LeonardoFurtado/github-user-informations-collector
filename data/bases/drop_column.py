import pandas as pd

df = pd.read_csv("all_projects.csv")

df = df.drop("country", axis=1)
# df = df.drop("dale", axis=1)

print(df.head())

df.to_csv("dale.csv", index=False)
