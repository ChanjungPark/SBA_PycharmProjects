# word2vecTest.py
# 문재인대통령신년사.txt
'''
구현 절차
BeautifulSoup을 사용하여 분석할 텍스트 파일을 읽어들입니다.
Okt 클래스를 사용하여 형태소 분석을 합니다.
전처리 작업을 수행한 다음 텍스트 파일 형식인 'word2vec.prepro'파일로 저장합니다.
'word2vec.prepro'파일을 읽어서 Binary형식의 파일 'word2vec.model'으로 저장합니다.
'''
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from gensim.models import word2vec

print('파일이 생성됩니다... 잠시만 기다려 주십시오.')
myencoding = 'utf-8'
filename = '문재인대통령신년사.txt'
myfile = open(filename, 'rt', encoding=myencoding)
soup = BeautifulSoup(myfile, 'html.parser')
mydata = soup.text
# print(mydata)

results = []   # 결과 저장소
okt = Okt()

datalines = mydata.split('\n')
print(len(datalines))

for oneline in datalines:
    mypos = okt.pos(oneline, norm=True, stem=True)   # norm : 정규화
    # print(mypos)

    imsi = []   # 임시 리스트
    for word in mypos:
        if not word[1] in ['Josa', 'Eomi', 'Punctuation', 'Verb']:
            if len(word[0]) >= 2:
                imsi.append(word[0])

    temp = (' '.join(imsi)).strip()
    results.append(temp)
    # break   # 차후 삭제 예정

# print(results)

# 정제된 파일로 저장하기
prepro_file = 'word2vec.prepro'
with open(prepro_file, 'wt', encoding=myencoding) as myfile:
    myfile.write('\n'.join(results))

print(prepro_file + ' 파일 생성됨')

# word2vec : word(단어)들을 벡터로 만드는 알고리즘
# vec : 벡터(방향, 크기)
# 스칼라 : only 값
# 단어들의 유사도 : 코싸인 유사도, 유클리디언 유사도, 맨하탄 유사도
# http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/ 참고
# https://bkshin.tistory.com/entry/NLP-8-%EB%AC%B8%EC%84%9C-%EC%9C%A0%EC%82%AC%EB%8F%84-%EC%B8%A1%EC%A0%95-%EC%BD%94%EC%82%AC%EC%9D%B8-%EC%9C%A0%EC%82%AC%EB%8F%84 참고

# LineSentence : 분석을 하기 위한 sentence를 만들어 주는 함수
data = word2vec.LineSentence(prepro_file)
print(type(data))

# Word2Vec : 해당 sentence를 사용하여 word2vec에 대한 모델을 생성해줍니다.
# size : 벡터의 차원수, window : 윈도우 사이즈, min_count : 버리고자 하는 최소 빈도수
# sg : 1(skipgram), 0(cbow)
model = word2vec.Word2Vec(data, size=200, window=10, min_count=2, sg=1)
print(type(model))

model_filename = 'word2vec.model'

# 모델을 저장할 때는 save 함수를 사용합니다.
# 모델 파일은 바이트 형식의 파일입니다.
model.save(model_filename)
print(model_filename + ' 파일 생성됨')

print('finished')