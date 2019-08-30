import pandas as pd
import numpy as np

df = pd.read_csv("../../data/bases/fullybase.csv")

# df.groupby("country").size().to_csv("dale.csv")
# print(df.groupby("country").groups["undefined"])

family = np.where((df["merged"] != "False", "accepted", "recused"))
df.groupby(family)["dale"].mean()
