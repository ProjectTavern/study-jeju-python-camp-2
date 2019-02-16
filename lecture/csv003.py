import csv

with open('sample.csv', mode='r', encoding='utf-8') as f:
    for i in csv.DictReader(f):
        print(i)
