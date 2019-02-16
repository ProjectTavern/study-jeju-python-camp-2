import csv

with open('sample.csv', mode='r', encoding='utf-8') as f:
    r = csv.reader(f)
    result = [i for i in r]
with open('sampleNew.csv', mode='w', encoding='utf-8') as f:
    name = ','.join(result[0]) + ",밀도\n"
    f.write(name)
    for i in result[1:]:
        data = ','.join(i) + ',' + str(int(i[2])//int(i[3])) + "\n"
        f.write(data)