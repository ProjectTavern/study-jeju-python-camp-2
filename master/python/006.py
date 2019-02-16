#006.py boolean
a = True       #1
b = False      #0
print(a and b) #and는 *
print(a or b)  #or는 +
print(not a)

print(bool(1))
print(bool('hello'))
print(bool(' '))
print(bool(''))
print(bool(0))

for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        
        