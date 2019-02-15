# 1부터 100까지 짝수를 더하는 것
sum = 0
for i in range(2, 101, 2):
    print(i)
    sum += i
print(sum)

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('{} x {} = {}'.format(i, j, i * j))

# 1부터 100까지 짝수를 더하는 것
sumi = 0
for i in range(1, 101):
    sumi = sumi + i

a = 10
b = a
c = b
b = 10000000
c = 10000000
print(id(a))
print(id(b))
print(id(c))

# 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print(i, 'X', j, '=', i * j)
