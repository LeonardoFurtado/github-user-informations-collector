import pandas as pd

df = pd.read_csv("../../data/african_countries.csv")
df_2 = pd.read_csv("../../data/bases/all_projects.csv")
dale = df_2["country"].value_counts()

count = 0
for country in df["country"]:
    if country in dale:
        print(country, dale[country])
        count += dale[country]

print(count)
