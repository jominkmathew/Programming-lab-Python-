import csv
csv_columns = ['sl.no','subject']
dict_data = [
{'sl.no': 1, 'subject': 'Maths'},
{'sl.no': 2, 'subject': 'Physics'},
{'sl.no': 3, 'subject': 'Chemistry'},
{'sl.no': 4, 'subject': 'Computer'},
{'sl.no': 5, 'subject': 'Biology'},
]
csv_file = "datas.csv"
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)
with open('datas.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
