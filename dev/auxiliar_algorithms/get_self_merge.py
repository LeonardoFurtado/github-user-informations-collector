import pandas as pd
import csv

projects = [
    "atom",
    "cpython",
    "d3",
    "django",
    "firefox-ios",
    "brew",
    "ionic",
    "mongo",
    "php",
    "react",
    "laravel",
    "scikit-learn",
    "swift",
    "vscode",
    "vue",
]

output_file = open("../../data/self_merge.csv", "a")
writer = csv.writer(output_file)
writer.writerow(["project", "total_pull_requests", "self_merges"])

for project in projects:
    df = pd.read_csv("../../data/bases/" + project + ".csv")
    count = 0
    for index, row in df.iterrows():
        if row["login"] == row["merged_by"]:
            count += 1

    writer.writerow([project, df.shape[0], count])
