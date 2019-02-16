x = 10
def one(a):
    a = a + 10
    return a
x = one(x)
print(x)

i = 10
def changei():
    global i
    i += 10
changei()
print(i)