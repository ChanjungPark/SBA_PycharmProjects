# konlpy_basic.py
# https://konlpy.org/ko/latest/api/konlpy.tag/#module-konlpy.tag._komoran 참고
from konlpy.tag import Komoran

text = '일등급 품질인 맛있는 딸기가 비닐 하우스에 들어가시나 ㅎㅎ'

komo = Komoran()
print(type(komo))

# pos : 단어와 품사를 튜플로 만들어 리스트 형태로 반환
result = komo.pos(text)
print(result)
print('-' * 30)

# 형태소 : 의미있는 최소의 단위
# 텍스트 마이닝 : 수많은 텍스트에서 의미있는 데이터만 추려내는 행위
print('전체 확인하기')
for myitem in result:
    somedata = '단어 : %s, 품사 : %s' % (myitem[0], myitem[1])
    print(somedata)
print('-' * 30)

print('3글자 이상의 명사만 추출해보기')
only_nouns = []
for myitem in result:
    if myitem[1] in ['NNG', 'NNP']:
        if len(myitem[0]) >= 3:
            somedata = '단어 : %s, 품사 : %s' % (myitem[0], myitem[1])
            only_nouns.append(myitem[0])
        else:
            print(myitem[0] + '은 제외합니다.')
print(only_nouns)
print('-' * 30)

print('명사만 추출해보기')
nouns = komo.nouns(text)
print(nouns)
print('-' * 30)

# userdic 매개변수 : 사용자 정의 사전을 활용하는 방법
sentence = '딸기 복숭아 최우수 FRUIT, 박찬정, 가나다라'
komo = Komoran(userdic='user_dict.txt')
print(komo.pos(sentence))
# [('딸기', 'NNP'), ('복숭아', 'NNP'), ('최우', 'NNP'), ('수', 'NNB'), ('FRUIT', 'SL'), (',', 'SP'), ('박찬', 'NNP'), ('정', 'NNP'), (',', 'SP'), ('가나', 'NNP'), ('다라', 'NNP')]
# [('딸기', 'NNP'), ('복숭아', 'NNP'), ('최우수', 'NNP'), ('FRUIT', 'SL'), (',', 'SP'), ('박찬정', 'NNP'), (',', 'SP'), ('가나다라', 'NNP')]
print('-' * 30)

print('finished')