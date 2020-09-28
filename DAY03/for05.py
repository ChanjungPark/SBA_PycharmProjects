# for05.py
myString = input('문자열 입력 : ')   # python is very easy

myList = myString.split()
print(type(myList)) # type 함수는 해당 데이터의 유형을 알려주는 함수
print(myList)

for idx in range(len(myList)):
    if idx % 2 == 0:
        myList[idx] = myList[idx].upper()
    else:
        myList[idx] = myList[idx].lower()

result = '#'.join(myList)
print(result)