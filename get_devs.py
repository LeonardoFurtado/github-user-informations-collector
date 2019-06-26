import csv
result = {}
with open('bases/atom.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #Dev Name/ ID / Location / PRs / aceitos / recusados
        print(row[1], row[3])

        if result[row[1]]:
            if row[3].lower() == "true":
                result[row[1]] =
        else:
            result[row[1]] = [row[0], row[1], row[4], 0, 0, 0]
            if row[3].lower() == "true":
                result[row[1]] = [row[0], row[1], row[4], 1, 1, 0]
            else:
                result[row[1]] = [row[0], row[1], row[4], 1, 0, 1]
