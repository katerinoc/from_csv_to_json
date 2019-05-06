import csv, json
import pandas as pd

csvreader = csv.reader(open('оценки2.csv'), quotechar=';')

data = []
listi=[]
_list = []
for row in csvreader:
    _dict = {}
    _dict1 = {}
    estlist = []
    estlist1 = []
    estlist2 = []
    estlist3 = []
    estlist4 = []
    new_list = []
    result = (row[0].split(';'))
    name = 'e' + result[6];
    estlist.append(result[1])
    _dict['criteriaID'] = 'К.НУА.1'
    _dict['estimation'] = estlist
    new_list.append(_dict)
    estlist1.append(result[2])
    _dict['criteriaID'] = 'К.НУА.2'
    _dict['estimation'] = estlist1
    new_list.append(_dict)
    estlist2.append(result[3])
    _dict['criteriaID'] = 'К.НУА.3'
    _dict['estimation'] = estlist2
    new_list.append(_dict)
    estlist3.append(result[4])
    _dict['criteriaID'] = 'К.МУА.1'
    _dict['estimation'] = estlist3
    new_list.append(_dict)
    estlist4.append(result[5])
    _dict['criteriaID'] = 'К.ЭТУА.1'
    _dict['estimation'] = estlist4

    new_list.append(_dict)
    _dict1['Name of project'] = result[0]
    _dict1['criteria2Estimation'] = new_list
    _final_dict = {}
    _final_dict[name] = _dict1
    _list.append(_final_dict)
print(_list)
with open("list.json", "w", encoding="utf-8") as file:
    json.dump(_list[1::], file, indent=2, ensure_ascii=False)