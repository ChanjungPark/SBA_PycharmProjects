# file001.py
# 파일 입출력
# open() : 텍스트/바이너리(그림판으로 볼 수 있는 이미지) 파일을 읽거나 쓰기 위한 함수
# open(file='전체경로+파일이름', mode='w', encoding='utf-8')
# mode : r(read - 기본값)/w(write)/a(append)  t(text - 기본값)/b(binary)

# encoding : 인코딩 문자열('utf-8', 'utf-16')
myfile01 = open(file='newfile.txt', mode='w', encoding='utf-8')

for idx in range(1, 11):
    # 문자열 '\n'은 엔터키를 의미합니다.
    data = '%2d번째 줄입니다.\n' % (idx)
    myfile01.write(data)

myfile01.close()

# mode='a' : 기존 파일에 추가 모드로 작성하기
myfile02 = open(file='newfile.txt', mode='a', encoding='utf-8')

for idx in range(11, 101):
    data = '%3d번째 줄입니다.\n' % (idx)
    myfile02.write(data)

myfile02.close()

print('여러개 파일 만들기')
for idx in range(1, 10):
    filename = 'somefile' + str(idx).zfill(2) + '.txt'
    myfile = open(file=filename, mode='w', encoding='utf-8')
    data = '메롱' + str(idx).zfill(5)
    myfile.write(data)
    myfile.close()
    # print(filename)

# with 구문은 암시적으로 close를 수행해줍니다.
# 따라서, close() 함수를 사용하지 않아도 됩니다.
print('with 구문 사용하기')
with open(file='test.txt', mode='w', encoding='utf-8') as myfile:
    myfile.write('메롱\n')
    myfile.write('하하\n')
    print('가나다라', file=myfile)

print('-' * 30)

with open(file='test.txt', mode='r', encoding='utf-8') as myfile:
    # print(myfile.read())
    # print(type(myfile.read()))
    print(myfile.readlines())

print('finished')