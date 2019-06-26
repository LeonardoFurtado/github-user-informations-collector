import csv
file = "countries.csv"

def get_country(city, file):
    """Through the name of the city, find your country."""
    city = city.lower()
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if(city == row[0] or city == row[1] or city == row[2] or city == row[3]):
                return row[2]
    return "Undefined"


paises_detectados = 0
paises_undefined = 0
with open('laravel.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        with open('laravel_rate.csv','a',newline='') as novo:
            writer = csv.writer(novo)
            if row[4].replace('"',''):
                #row.append(get_country(row[4].replace('"',''), file))+"\n"
                #novo.write(row)
                if get_country(row[4].replace('"',''), file) == "Undefined":
                    paises_undefined += 1
                    writer.writerow(["Undefined"])
                else:
                    paises_detectados += 1
                    writer.writerow([get_country(row[4].replace('"',''), file)])
            else:
                writer.writerow(["blank field"])

print("detectados: ", paises_detectados)
print(paises_undefined)
