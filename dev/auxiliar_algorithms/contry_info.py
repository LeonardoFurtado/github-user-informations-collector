import pandas as pd
import numpy as np

df = pd.read_csv("../../data/bases/complete_dataset.csv")
df_accepted = df.loc[df["merged"] != False]
df_rejected = df.loc[df["merged"] == False]

# print(df.groupby("country").groups["undefined"])
print(len(df.groupby("country").groups["undefined"]))

# Total pull requests by country
# df.groupby("country").size().to_csv("total.csv")

# Pull requests accepted by country
# df_accepted.groupby("country").size().to_csv("accepted.csv")

# Pull requests rejected by country
# df_rejected.groupby("country").size().to_csv("rejected.csv")

# df.sort_values("name", inplace=True)
# df = df.drop_duplicates(subset="name", inplace=False)
# print(df["name"].count())
#
# print(df["name"].nunique())

# Contributos by country
