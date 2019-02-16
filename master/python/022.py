print(range(10000)) #range(0, 10)
print(type(range(10))) #class 'range'

for i in range(10):
    print(i) 
print('--------')
for i in range(2, 10, 2):
    print(i)
print('--------')
sumi = 0
for i in range(2, 101, 2):
    sumi += i
print(sumi)