import pandas as pd

map_data = pd.read_csv('teste.csv')
# print(map_data)
pega = map_data.duplicated('cidade')

print(pega)

print(map_data.ix[1])

new_map = map_data.drop(1)
print(new_map)

new_map = map_data.drop(1)
print(new_map)
