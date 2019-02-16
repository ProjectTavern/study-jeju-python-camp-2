#string
a = 'hello'
name = 'hojun'
nametwo = 'Python'
namethree = 'paullab CEO leehojun'
val = 10
print(type(a))
print(dir(a))
print('hello ', name, '!!, my name', nametwo)
print('hello {}!!, my name{}'.format(name, nametwo))
print(name[0])#h     #indexing
print(name[1])#o
print(name[2:4])
#변수명[start:stop:step]
print(namethree[2::2])   #slicing
print(namethree[::-1])
print(namethree[-1])
print(name.index('j'))
print(namethree.count('l'))
print(namethree.index('l'))
print(namethree.strip('   l    '))
x = '10'
y = '33'
print(x.zfill(4))
print(y.zfill(4))
print(dir(namethree))



