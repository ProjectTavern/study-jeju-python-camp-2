for i in range(1, 10):
    print('{} X {} = {}'.format(2, i, 2*i))
    
for i in range(1, 10):
    print('{} X {} = {}'.format(3, i, 3*i))

for j in range(2, 10): 
    for i in range(1, 10):
        print('{} X {} = {}'.format(j, i, j*i))
        
l = []
for i in range(10):
    l.append(i)
    
l2 = [i for i in range(10)]

l3 = ['{} X {} = {}'.format(i, j, i*j) 
      for i in range(2, 10) 
          for j in range(1, 10)]

print(l)
print(l2)
print(l3)
#리스트 안에 공백은 병합
l4 = [
    '제주코딩베이스캠프7기',
    '제주코딩베이스캠프8기',
]

