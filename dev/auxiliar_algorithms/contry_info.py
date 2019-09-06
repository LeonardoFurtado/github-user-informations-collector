import pandas as pd
import numpy as np

df = pd.read_csv("../../data/bases/all_projects_last.csv")
df_accepted = df.loc[df["merged"] != False]
df_rejected = df.loc[df["merged"] == False]

# # Total de contribuidores
print("Total de contribuidores: ", df["login"].count())
print("Total de contribuidores: ", df["login"].nunique())
#
# # Total de pull requests
# print("Total de pull requests: ", df["login"].count())
#
# # Contribuicoes por pais
# df.groupby("country").size().to_csv("total.csv")
#
# # Contribuicoes aceitas
# df_accepted.groupby("country").size().to_csv("accepted.csv")
#
# # Pull requests rejected by country
# df_rejected.groupby("country").size().to_csv("rejected.csv")


# print(df.groupby("country").groups["undefined"])
# print(df.groupby("country").groups())


# df.sort_values("login", inplace=True)
# df_2 = df.drop_duplicates(subset="login", inplace=False)
# df_2.groupby("country").size().to_csv("contripercountry.csv")


# Contributos by country
