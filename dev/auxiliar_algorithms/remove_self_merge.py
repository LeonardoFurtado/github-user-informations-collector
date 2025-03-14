#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Leonardo Furtado"
__contact__ = "leonardofurtado@ieee.org"

import pandas as pd
import csv

projects = [
    "atom",
    "angular",
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
    "zulip",
]

for project in projects:
    df = pd.read_csv("../../data/bases/" + project + ".csv")
    for index, row in df.iterrows():
        if row["login"] == row["merged_by"]:
            df = df.drop(index)
    df.to_csv("output/" + project + ".csv", index=False)
