import json
 
# JSON
jsonString = '{"name": "이호준", "age": 32, "phone": "010-0000-0000", "address": "jeju"}'
 
# JSON 디코딩
test_dict = json.loads(jsonString)
 
# Dictionary 형태로 변환 체크
print(test_dict['name'])

