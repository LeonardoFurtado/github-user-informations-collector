import csv

projetos = ["atom","cpython","d3","django","firefox-ios","homebrew","ionic",
"mongo","php","react","laravel","scikit-learn","swift","vscode","vue"]

for project in projetos:

    dicionario = {}

    with open('novo.csv','r',newline='') as novo:
        spamreader = csv.reader(novo, delimiter=',', quotechar='|')
        for row in spamreader:
            dicionario[row[0]] = int(row[1])

    with open(project+'.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if row[1] not in dicionario:
                if row[0].lower() == 'true':
                    dicionario[row[1]] = 1
                else:
                    dicionario[row[1]] = 0
            else:
                if row[0].lower() == 'true':
                    dicionario[row[1]] += 1

    with open('novo.csv','w',newline='') as novo:
        writer = csv.writer(novo)
        for k in dicionario:
            writer.writerow([k, dicionario[k]])
