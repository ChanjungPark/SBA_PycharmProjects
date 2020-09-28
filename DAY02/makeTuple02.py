# makeTuple02.py
tuple01 = ('김철수', 40, 50, 60)
tuple02 = ('박영희', 50, 60, 70)

myTuple = (tuple01, tuple02)
print(myTuple)

print('총 인원수 : ', len(myTuple), '명', sep='')

saram = myTuple[0][0]
jumsu = myTuple[0][1:]
print(saram)
print(jumsu)

hap = sum(jumsu)
myLen = len(jumsu)
average = hap/myLen
print('이름 : ', saram, ', 평균 : ', average, '점', sep='')

print('국어의 평균')
kor = myTuple[0][1] + myTuple[1][1]
print(kor/2)