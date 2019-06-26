import csv

campos_branco = 0
campos_preenchidos = 0
with open('vscode.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if row[4]:
            campos_preenchidos += 1
        else:
            campos_branco += 1

print("branco: ",campos_branco)
print("preenchido: ",campos_preenchidos)
