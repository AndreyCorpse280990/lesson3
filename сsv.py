import csv
list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
with open('test.csv', 'w', encoding='utf-8') as f:
    field = ['name', 'age', 'job']
    writer = csv.DictWriter(f, field, delimiter=';')
    writer.writeheader()
    for user in list:
        writer.writerow(user)