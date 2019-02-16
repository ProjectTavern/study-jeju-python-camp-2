#001.py
age = input('나이를 입력하세요:')
intage = int(age) #형변환
print('제 나이는', age+age, '입니다')
print('제 나이는', intage+intage, '입니다')
print(type(age)) #age의 정체를 알 수 있어요.
print(type(intage)) #intage의 정체를 알 수 있어요.
print(dir(age)) #age의 속성들을 볼 수 있습니다.
print(dir(intage)) #intage의 속성들을 볼 수 있습니다.