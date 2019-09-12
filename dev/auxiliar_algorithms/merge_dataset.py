import pandas as pd
import os

projects = [
    "atom",
    "angular",
    "zulip",
    "cpython",
    "d3",
    "django",
    "firefox-ios",
    "brew",
    "ionic",
    "mongo",
    "php",
    "react",
    "react-native",
    "laravel",
    "tensorflow",
    "scikit-learn",
    "spyder",
    "swift",
    "vscode",
    "vue",
]
path = "../../data/bases/zips/orgs_pr_removed/all_projects.csv"
for project in projects:
    current_df = pd.read_csv(path)
    next_df = pd.read_csv("../../data/bases/zips/orgs_pr_removed/" + project + ".csv")
    frames = [current_df, next_df]
    output = pd.concat(frames, sort=False)
    output.to_csv(path, index=False)
