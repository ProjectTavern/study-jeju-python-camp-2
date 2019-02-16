#list, tuple, dict, set
l = [100, 200, 300, 400]
'''
1. 리스트 안에는 다른 Object들이 들어갈 수 있습니다.
2. 값을 변화시킬 수 있습니다.
3. 순서가 있습니다.
'''
print(l[3])
print(l[:4:2])
#print(l[start:stop:step])
l[3] = 1000
print(l)
print(type(l))
print(dir(l))
l.append(100)
#l.clear()
#c = l.copy()
print(l.count(100))
l.extend([100, 200, 300])
print(l.index(1000))
l.insert(3, 100000)
print(l)
l.pop()
l.remove(100)
print(l)
l.reverse()
l.sort()
print(l)