jeju = {'banana':1000, 'orange':300, 'apple': 100}
print(type(jeju))
print(dir(jeju))
seoul = jeju.copy()
#listx = listy[:]
print(id(seoul))
print('---------')
print(id(jeju))
jeju['orange'] = 10000
print(seoul)
print(jeju.items())
