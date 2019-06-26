# output_file = open(r'final.csv', 'r', encoding='utf8')
# count = 0
# for line in output_file:
#     count += 1
#     print(count)
import csv

dictor = {}

with open('novo.csv','r',newline='') as novo:
    spamreader = csv.reader(novo, delimiter=',', quotechar='|')
    for row in spamreader:
        dictor[row[0]] = int(row[1])


with open('cpython.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row[1])
        if row[1] not in dictor:
            if row[0] == 'TRUE':
                dictor[row[1]] = 1
            else:
                dictor[row[1]] = 0
        else:
            if row[0] == 'TRUE':
                dictor[row[1]] += 1

with open('novo.csv','w',newline='') as novo:
    writer = csv.writer(novo)
    for k in dictor:
        writer.writerow([k, dictor[k]])
