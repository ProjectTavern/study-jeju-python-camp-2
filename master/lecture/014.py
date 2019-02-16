a = True #1
b = False #0
print(a and b) #and는 곱
print(a or b) #or는 합
print(not a)

sumi = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sumi += i
print(sumi)
