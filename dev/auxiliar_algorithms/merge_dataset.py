import pandas as pd

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

for project in projects:
    current_df = pd.read_csv("../../data/bases/fullybase.csv")
    next_df = pd.read_csv("../../data/bases/" + project + ".csv")
    frames = [current_df, next_df]
    output = pd.concat(frames)
    output.to_csv("../../data/bases/fullybase.csv", index=False)
