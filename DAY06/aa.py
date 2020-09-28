# aa.py
'''
임시 파일을 만들어서 아래 코딩을 테스트 해주세요.
'''
from konlpy.tag import Komoran

sentence = '국정 농단 태블릿 PC, 설진욱, 가나다라'
print('# before user dic')
komo = Komoran()
print(komo.pos(sentence))