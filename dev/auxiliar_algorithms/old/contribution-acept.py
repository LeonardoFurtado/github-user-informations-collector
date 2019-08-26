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


for project in projects:
    zero_contribution = []
    one_contribution = []
    with open("contribution-rate/"+project+".csv") as csvfile:
        spamreader = csv.reader(csvfile, quotechar='|')
        for row in spamreader:
            if row[1] == row[2] == '1':
                one_contribution.append(row)
            if row[1] == '0':
                zero_contribution.append(row)

    with open("contributions.csv",'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([project,str(len(zero_contribution)), str(len(one_contribution))])
