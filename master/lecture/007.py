for i in 'leehojun':
    print(i)
    
for i in [100, 200, 300]:
    print(i)

for i in range(0, 100, 2):
    print(i)
    
#1부터 100까지의 짝수를 더하는 것
#구구단 출력
sumi = 0
for i in range(1, 101):
    sumi = sumi + i
    
a = 10
b = a
c = b
print(id(a))
print(id(c))
a = 100000
b = 100000
print(a)
print(b)
a = 100
b = 100
print(a)
print(b)

for i in range(2, 10):
    for j in range(1, 10):
        print(i, 'X', j, '=', i*j)
        