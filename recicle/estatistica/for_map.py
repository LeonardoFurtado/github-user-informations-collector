import csv

vector = []
with open('for_map.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    for row in spamreader:
        #print(row[1])
        if int(row[0]) <= 10:
            vector.append(1)
        elif int(row[0]) <= 25:
            vector.append(2)
        elif int(row[0]) <= 50:
            vector.append(3)
        elif int(row[0]) <= 75:
            vector.append(4)
        elif int(row[0]) <= 100:
            vector.append(5)


for i in vector:
    print(i)
with open('output_map.csv','a',newline='') as novo:
    writer = csv.writer(novo)
    for k in vector:
        writer.writerow([k, ""])
