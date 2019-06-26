file_name = "atom.csv"
paises = []
with open(file_name, mode='r') as csv_file:
    for line in csv_file:
        spliting = line.split(",")
        if spliting[len(spliting)-1] not in paises:
            paises.append(spliting[len(spliting)-1])

for i in paises:
    print(i)
#38
