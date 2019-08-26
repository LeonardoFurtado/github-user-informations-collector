import csv

dictor = {}
paises = {}

with open('contribuidores_paises.csv','r') as novo:
     spamreader = csv.reader(novo, delimiter=',', quotechar='|')
     for row in spamreader:
         paises[row[0]] = int(row[1])


with open('vue.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row[0])
        if row[0] not in dictor:
            dictor[row[0]] = row[1]
            if row[1] not in paises:
                paises[row[1]] = 1
            else:
                paises[row[1]] += 1

with open('contribuidores_paises.csv','w',newline='') as novo:
    writer = csv.writer(novo)
    for k in paises:
        writer.writerow([k, paises[k]])
