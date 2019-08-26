import csv
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

file = "countries/countries.csv"


def get_country(city, file):
    """Through the name of the city, find your country."""
    city = city.lower()
    with open(file, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in spamreader:
            if city == row[0] or city == row[1] or city == row[2] or city == row[3]:
                return row[2]
    return "undefined"


for project in projects:
    df = pd.read_csv("../../data/bases/" + project + ".csv")
    for index, row in df.iterrows():
        print(row["location"])

#         with open("laravel_rate.csv", "a", newline="") as novo:
#             writer = csv.writer(novo)
#             if row[4].replace('"', ""):
#                 # row.append(get_country(row[4].replace('"',''), file))+"\n"
#                 # novo.write(row)
#                 if get_country(row[4].replace('"', ""), file) == "Undefined":
#                     writer.writerow(["Undefined"])
#                 else:
#                     writer.writerow([get_country(row[4].replace('"', ""), file)])
