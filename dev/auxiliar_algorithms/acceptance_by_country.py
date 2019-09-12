import pandas as pd

df = pd.read_csv("../../data/bases/all_projects.csv")

total = (
    df.groupby("country")["country"]
    .count()
    .rename("Total de requisições")
    .reset_index()
)

requisicoes = (
    df.groupby("country")["merged"]
    .value_counts()
    .rename("countRequisicoes")
    .reset_index()
)

requisicoes = pd.pivot(
    requisicoes, values="countRequisicoes", index="country", columns="merged"
).reset_index()

total = total.merge(requisicoes, on="country")
total.to_csv("../../data/acceptance_by_country.csv", index=False)
