import pandas as pd

df = pd.read_csv("../../data/bases/all_projects_final.csv")
df = df.loc[df["country"] != "undefined"]
df.to_csv("../../data/bases/all_projects_ur.csv")
