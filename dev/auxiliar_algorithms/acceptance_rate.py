import pandas as pd
import numpy as np
import csv

df = pd.read_csv("../../data/bases/all_projects.csv")
total_contributions = pd.read_csv("total.csv")
dict_1 = dict(
    zip(list(total_contributions["country"]), list(total_contributions["number"]))
)

loc_rejection = []
loc_acceptance = []
for key in dict_1:
    count_rejection = 0
    count_acceptance = 0
    for index, row in df.iterrows():
        if row["country"] == key:
            if row["merged"] == False:
                count_rejection += 1
            else:
                count_acceptance += 1
    loc_rejection.append(count_rejection)
    loc_acceptance.append(count_acceptance)

total_contributions["accepted"] = loc_acceptance
total_contributions["rejected"] = loc_rejection
total_contributions.to_csv("new_total.csv", index=False)
print(count_rejection)
print(count_acceptance)

# Contributos by country
# df_2 = pd.read_csv("contripercountry.csv")
# dict_2 = dict(zip(list(df_2["country"]), list(df_2["number"])))
#
# writer = csv.writer(output_file)
#
# for key in dict_1:
#     writer.writerow([key, dict_1[key], dict_2[key], dict_1[key] / dict_2[key]])
