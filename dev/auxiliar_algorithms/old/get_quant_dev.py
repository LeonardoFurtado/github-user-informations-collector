import csv

projects = [
"atom",
"d3",
"php",
"vscode",
"django",
"mongo",
"ionic",
"cpython",
"react",
"firefox-ios",
"swift",
"homebrew",
"scikit-learn",
"laravel",
"vue"
]

devs = {}

for project in projects:
    with open("algoritmos/bases/"+project+".csv") as csvfile:
        spamreader = csv.reader(csvfile, quotechar='|')
        for row in spamreader:
            if row[5] not in devs:
                devs[row[5]] = [row[1]]
            else:
                if row[1] not in devs[row[5]]:
                    devs[row[5]].append(row[1])
with open("get_quant_devs.csv",'w') as csvfile:
    writer = csv.writer(csvfile)
    for k in devs:
        writer.writerow([k, len(devs[k])])
