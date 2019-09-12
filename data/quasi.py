import pandas as pd
import csv

# df = pd.read_csv("quasi.csv")
# df = df.groupby("country").size().to_csv("quasis.csv")
df = pd.read_csv("quasis.csv")
df_2 = pd.read_csv("contri_per_country.csv")

output_file = open(r"quasi_rate.csv", "a", encoding="utf8")
writer = csv.writer(output_file)
for index, row in df.iterrows():
    for index_2, row_2 in df_2.iterrows():
        if row["country"] == row_2["country"]:
            writer.writerow(
                [row["country"], row_2["country"], row["total"], row_2["qtd"]]
            )
