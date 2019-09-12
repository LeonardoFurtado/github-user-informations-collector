import pandas as pd

df = pd.read_csv("../../data/bases/all_projects.csv")

total = (
    df.groupby(["login", "country"])["login"]
    .count()
    .rename("Total de prs")
    .reset_index()
)
requisicoes = (
    df.groupby("login")["merged"].value_counts().rename("countPrs").reset_index()
)

requisicoes = pd.pivot(
    requisicoes, values="countPrs", index="login", columns="merged"
).reset_index()

total = total.merge(requisicoes, on="login")
total.to_csv("testando_2.csv", index=False)
