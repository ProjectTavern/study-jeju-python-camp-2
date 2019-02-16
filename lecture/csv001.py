import csv

with open('sample.csv', mode='r', encoding='utf-8') as f:
    rows = csv.reader(f)
    for row in rows:
        print(row)
