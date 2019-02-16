import csv

with open('sample.csv', mode='r', encoding='utf-8') as f:
    r = csv.reader(f)
    for row in r:
        print(row)