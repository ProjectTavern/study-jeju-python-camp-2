for i in range(2, 10):
    for j in range(1, 10):
        print(i, 'X', j, '=', i*j)
        
l = [100, 200, 300, [100, 200, 300, [1000, 2000]]]
print(l[3][3][0])

ll = ['{} X {} = {}'. format(i, j, i*j) for i in range(2, 10) for j in range(1, 10)]
print(ll)

s = {100, 200, 300, 400, 400}


