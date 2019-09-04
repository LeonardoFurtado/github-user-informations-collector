#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Leonardo Furtado"
__contact__ = "leonardofurtado@ieee.org"

import pandas as pd
import csv

from common.email_utils import is_commercial

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
    df = pd.read_csv("../../data/bases/" + project + ".csv")
    for index, row in df.iterrows():
        if is_commercial(row["email"]):
            df = df.drop(index)
    df.to_csv("output/" + project + ".csv", index=False)
