# list, tuple, dict, set

list = [100, 200, 300, 400]
'''
1. 리스트 안에는 다른 object들이 들어갈 수 있습니다.
2. 값을 변화시킬 수 있습니다.
3. 순서가 있습니다.
'''

print(list[3])
print(list[:4:2])
# print(list[start:stop:step])
list[3] = 1000
print(list)
print(type(list))
print(dir(list))

list.append(100)
# list.clear()
# c = list.copy
print(list.count(100))
list.extend([100, 200, 300])
print(list.index(1000))
list.insert(3, 100000)
print(list)
list.pop()
list.remove(100)
print(list)
list.reverse()
print(list)
list.sort()
print(list)
