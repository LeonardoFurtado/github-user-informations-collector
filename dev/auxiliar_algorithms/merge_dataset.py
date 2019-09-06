import pandas as pd
import os

projects = [
    "atom",
    "angular",
    "angular-cli",
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
for project in projects:
    current_df = pd.read_csv("../../data/bases/all_projects.csv")
    next_df = pd.read_csv("../../data/bases/" + project + ".csv")
    frames = [current_df, next_df]
    output = pd.concat(frames)
    output.to_csv("../../data/bases/all_projects.csv", index=False)
