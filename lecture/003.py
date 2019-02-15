# 003.py
# class str

a = 'hello world'
print(a[0])
print(a[1])
print(a[2])
print(a[0], end='')
print(a[1], end='')
print(a[2], end='')
print(a[0:2])  # slicing
print(type(a))
print(dir(a))


name = 'sherlock'
age = '35'
print('제 이름은 {}입니다. 제 나이는 {}입니다.'.format(name, age))
print('제 이름은 {1}입니다. 제 나이는 {0}입니다.'.format(name, age))
print('제 이름은', name, '입니다.')

b = a.split()
print(b)
print(','.join(b))
