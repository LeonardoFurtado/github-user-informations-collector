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
zero_contribution = {}
one_contribution = {}
for project in projects:
    with open("contribution-rate/"+project+".csv") as csvfile:
        spamreader = csv.reader(csvfile, quotechar='|')
        for row in spamreader:
            if row[1] == row[2] == '1':
                if row[3] in one_contribution:
                    one_contribution[row[3]] = one_contribution[row[3]] + 1
                else:
                    one_contribution[row[3]] = 1
            if row[1] == '0':
                if row[3] in zero_contribution:
                    zero_contribution[row[3]] = zero_contribution[row[3]] + 1
                else:
                    zero_contribution[row[3]] = 1

with open("zero_contribution.csv",'w') as csvfile:
    writer = csv.writer(csvfile)
    for k in zero_contribution:
        writer.writerow([k,zero_contribution[k]])

with open("one_contribution.csv",'w') as csvfile:
    writer = csv.writer(csvfile)
    for k in one_contribution:
        writer.writerow([k,one_contribution[k]])
