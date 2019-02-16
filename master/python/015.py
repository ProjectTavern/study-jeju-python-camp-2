#tuple
t = (100, 200, 300, 400)
l = [100, 200, 300]
t2 = (100, 200, 300, l)
'''
1. 순서가 있습니다.
   예)print(t[0])
   
2. 값을 바꿀 수 없습니다.
   예)t[0] = 10000 (X)
'''
print(t2)
l[0] = 1000
print(t2)
def change(x):
    print(id(x))
    x[0] = 10000
change(l)
print(id(l))
print(l)


