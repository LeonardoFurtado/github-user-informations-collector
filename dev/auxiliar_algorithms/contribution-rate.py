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

#users = {}

for project in projects:
    users = {}
    with open("bases/"+project+".csv") as csvfile:
        spamreader = csv.reader(csvfile, quotechar='|')
        for row in spamreader:
            if row[1] in users:
                if row[3].lower() == 'true':
                    users[row[1]][0] += 1
                    users[row[1]][1] += 1
                else:
                    users[row[1]][1] += 1
            else:
                users[row[1]] = [0,0,row[5]]
                if row[3].lower() == 'true':
                    users[row[1]][0] += 1
                    users[row[1]][1] += 1
                else:
                    users[row[1]][1] += 1



    with open("contribution-rate/"+project+".csv",'a') as csvfile:
        writer = csv.writer(csvfile)
        for user in users:
            writer.writerow([user, users[user][0],users[user][1],users[user][2]])
