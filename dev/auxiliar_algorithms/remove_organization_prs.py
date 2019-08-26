#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Leonardo Furtado"
__contact__ = "leonardofurtado@ieee.org"

import re
import pandas as pd

projects = {
    "atom": ["atom", "github"],
    "cpython": [
        "python",
        "facebook",
        "capitalone",
        "google",
        "aws",
        "fastly",
        "bloomberg",
        "redhat",
        "indeed",
        "microsoft",
        "heroku",
    ],
    "d3": ["d3"],
    "django": [
        "django",
        "jetbrains",
        "instagram",
        "23andme",
        "sentry",
        "ledu",
        "kolonialno",
        "lights-on-software",
        "revsys",
        "zapier",
    ],
    "firefox-ios": ["mozilla-mobile", "firefox"],
    "brew": [
        "homebrew",
        "digitalocean",
        "macstadium",
        "commsworld",
        "bintray",
        "agileBits",
        "conservancy",
    ],
    "ionic": ["ionic", "ionic-team"],
    "mongo": [
        "mongodb",
        "ibm",
        "aws",
        "google",
        "googlecloudplatform",
        "microsoft",
        "azure",
        "infosys",
        "accenture",
        "pivotal",
    ],
    "php": ["php", "digitalocean", "jetbrains", "pantheon", "pantheon-systems"],
    "react": ["react", "reactjs", "github"],
    "laravel": [
        "laravel",
        "vehikil",
        "tightenco",
        "kirschbaum",
        "byte5",
        "64robots",
        "cubet",
        "devsquad",
        "ideil",
    ],
    "scikit-learn": [
        "google",
        "inria",
        "nyu",
        "telecom-parisTech",
        "columbia",
        "columbia university",
    ],
    "swift": ["apple", "apple inc."],
    "vscode": ["microsoft"],
    "vue": [
        "vuejs",
        "standard library",
        "stdlib",
        "teambit",
        "vehikil",
        "nativescript",
        "shopware",
        "uni-app",
        "laravel",
        "vue mastery",
    ],
}


def str_to_list(str):
    """remove unwanted characters from the string, making list conversion
    possible using the split() function."""
    return re.sub("'|\[|\]| ", "", str).split(",")


for project in projects:
    df = pd.read_csv("../../data/bases/" + project + ".csv")
    for index, row in df.iterrows():
        if [i for i in str_to_list(row["orgs"]) if i in projects[project]]:
            df = df.drop(index)
        elif str(row["company"]).replace("@", "").lower() in projects[project]:
            df = df.drop(index)

    df.to_csv("../../data/bases/orgs_remove/" + project + ".csv", index=False)
