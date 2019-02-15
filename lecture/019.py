list = []
for i in range(2, 10):
    for j in range(1, 10):
        list.append('{} X {} = {}'.format(i, j, i * j))
print(list)

ll = ['{} X {} = {}'.format(i, j, i * j) for i in range(2, 10) for j in range(1, 10)]

print(ll)
