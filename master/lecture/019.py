l = []
for i in range(2, 10):
    for j in range(1, 10):
        l.append('{} X {} = {}'.format(i, j, i*j))
print(l)
ll = ['{} X {} = {}'.format(i, j, i*j) for i in range(2, 10) for j in range(1, 10)]
print(ll)
