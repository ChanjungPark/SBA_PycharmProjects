# makeDictionary.py
myDict = {'김철수':35, '박영희':50, '홍길동':40}
print(myDict)
print('-' * 30)

# 관련 함수 : for()

for key in myDict.keys():
    print(key)

print('-' * 30)

for value in myDict.values():
    print(value)

print('-' * 30)

for key in myDict.keys():
    print('{}의 나이는 {}살입니다.'.format(key, myDict[key]))

print('-' * 30)

for key, value in myDict.items():
    print('{}의 나이는 {}살입니다.'.format(key, value))

print('-' * 30)

findKey = '심형래'
if findKey in myDict:
    print(findKey + "은 존재함")
else :
    print(findKey + "은 존재 안 함")

result = myDict.pop('홍길동')
print('pop 이후 내용 : ', myDict)
print('pop된 내용 : ', result)