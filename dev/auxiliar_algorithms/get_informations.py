import pandas as pd

# login,name,email,bio,company,blog,location,merged,merged_by,orgs

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

total_pull_requests = 0
total_contributors = 0
print("{:>12}  {:>12}  {:>12}".format("Project", "Total PR", "Total Contributors"))

for project in projects:
    df = pd.read_csv("../../data/bases/" + project + ".csv")
    print(
        "{:>12}  {:>12}  {:>12}".format(
            project, df["login"].count(), df["login"].nunique()
        )
    )
    total_pull_requests += df["login"].count()
    total_contributors += df["login"].nunique()

print("{:>12}  {:>12}  {:>12}".format("Total", total_pull_requests, total_contributors))
