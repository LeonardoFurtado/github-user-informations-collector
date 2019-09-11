import pandas as pd
import numpy as np
import csv

df = pd.read_csv("../../data/bases/all_projects.csv")
df_accepted = df.loc[df["merged"] != False]
# df_rejected = df.loc[df["merged"] == False]

# % accepted and rejected
# rejected = df.loc[df["merged"] == False]
# accepted = df.loc[df["merged"] != False]
# print(rejected["login"].count())
# print(accepted["login"].count())

# True  19435
# False 24593

# # Total de contribuidores
# print("Total de pull requests: ", df["login"].count())
# print("Total de contribuidores: ", df["login"].nunique())
#
# # Total de pull requests
# print("Total de pull requests: ", df["login"].count())
#
# # Contribuicoes por pais
# df.groupby("country").size().to_csv("total.csv")
#
# # Contribuicoes aceitas
df_accepted.groupby("country").size().to_csv("accepted.csv")
#
# # Pull requests rejected by country
# df_rejected.groupby("country").size().to_csv("rejected.csv")


# print(df.groupby("country").groups["undefined"])
# print(df.groupby("country").groups())

# contribuidores por pais
# df.sort_values("login", inplace=True)
# df_2 = df.drop_duplicates(subset="login", inplace=False)
# df_2.groupby("country").size().to_csv("contripercountry.csv")


# Contributos by country
# df = pd.read_csv("total.csv")
# df_2 = pd.read_csv("contripercountry.csv")
# dict_1 = dict(zip(list(df["country"]), list(df["number"])))
# dict_2 = dict(zip(list(df_2["country"]), list(df_2["number"])))
#
# output_file = open(r"prbycontributor.csv", "a", encoding="utf8")
# writer = csv.writer(output_file)
#
# for key in dict_1:
#     writer.writerow([key, dict_1[key], dict_2[key], dict_1[key] / dict_2[key]])
