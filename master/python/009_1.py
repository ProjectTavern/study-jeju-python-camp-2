#009_1.py
def one(X):
    def two(Y):
        return Y ** X
    return two

f = one(2)
print(f(3))
print(f(4))
f2 = one(3)
print(f(3))
print(f(4))

hojun = print
hojun('hello world')
