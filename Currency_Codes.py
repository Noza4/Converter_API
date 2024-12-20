import json

with open("rates.json", 'r') as file:
    data = json.load(file)

data_ls = []
for cur in data[0]['currencies']:
    data_ls.append(cur['code'])

data = data_ls
