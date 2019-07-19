file_name = "project_here.csv"
contries = []
with open(file_name, mode='r') as csv_file:
    for line in csv_file:
        spliting = line.split(",")
        if spliting[len(spliting)-1] not in contries:
            contries.append(spliting[len(spliting)-1])

return contries
