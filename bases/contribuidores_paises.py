import csv

dictor = {}
dictor['lenght'] = 0

# with open('contribuidores_paises.csv','r',newline='') as novo:
#     spamreader = csv.reader(novo, delimiter=',', quotechar='|')
#     for row in spamreader:
#         dictor[row[0]] = int(row[1])


with open('laravel.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row[1])
        if row[1] not in dictor:
            dictor[row[1]] = 1
            dictor['lenght'] += 1


with open('contribuidores_paises.csv','a',newline='') as novo:
    writer = csv.writer(novo)
    writer.writerow(['laravel', dictor['lenght']])
