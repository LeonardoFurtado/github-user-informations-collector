import pandas as pd

df = pd.read_csv("../../data/bases/fullybase.csv")

df.groupby("country").size().to_csv("dale.csv")
