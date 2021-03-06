# naverCartoon.py
'''
크롤링 :
    웹 페이지의 링크들을 돌아다니면서 데이터를 수집하는 행위
	어떤 페이지에서 필요한 정보를 추출하는 행위

크롤링 : BeautifulSoup4(정적 페이지), Selenium(동적 페이지, 자바 스크립트)

필요한 지식
	html, 자바 스크립트, css(스타일 시트) 이해
'''

# 사이트 주소 : https://comic.naver.com/webtoon/weekday.nhn
'''
크롤링 순서
<div class="thumb">인 항목을 찾습니다.
반복문을 사용하여 
    <a> 태그의 href 속성을 읽어 들입니다.
        replace() 함수로 치환합니다.
        split() 함수를 이용하여 요소를 분해합니다.
    <img> 태그를 읽습니다.
        title 속성을 읽어서 제목으로 처리합니다.
            '?'와 ':'는 파일 이름을 사용 불가능하므로 치환합니다.
        src 속성을 읽어서 임의 경로를 취득합니다.
        
    필요한 정보를 리스트에 추가합니다
    해당 이미지를 각 요일 폴더에 이미지로 저장합니다.
    
    데이터 프레임으로 만들어서 csv 파일로 저장합니다.
'''
from bs4 import BeautifulSoup

# urlopen : 네트워크에 존재하는 주소를 열어주는 함수
from urllib.request import urlopen

myparser = 'html.parser'
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
response = urlopen(myurl)
soup = BeautifulSoup(response, myparser)
print(type(soup))

# 요일별 폴더 생성
weekday_dict = {'mon':'월요일', 'tue':'화요일', 'wed':'수요일', 'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 'sun':'일요일'}

# shutil : shell utility - 쉘과 관련된 유틸리티
import os, shutil
myfolder = 'c:\\imsi\\'

# 각 이미지를 저장해주는 함수
def saveFile(mysrc, myweekday, mytitle):
    image_file = urlopen(mysrc)
    filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle + '.jpg'
    # print(mysrc)
    # print(filename)

    myfile = open(filename, mode='wb')
    myfile.write(image_file.read()) # 바이트 형태로 ㅈ장
    myfile.close()

try:
    if not os.path.exists(myfolder):
        os.mkdir(myfolder)

    for mydir in weekday_dict.values():
        mypath = myfolder + mydir

        if os.path.exists(mypath):
            # rmtree : remove tree
            shutil.rmtree(mypath)

        os.mkdir(mypath)

except FileExistsError as err:
    print(err)

mytarget = soup.find_all('div', attrs={'class':'thumb'})
print(len(mytarget))

myList = [] # 데이터를 저장할 리스트

for abcd in mytarget:
    myhref = abcd.find('a').attrs['href']
    myhref = myhref.replace('/webton/list.nhn?', '')
    result = myhref.split('&')
    # print(myhref)
    # print(result)
    mytitleid = result[0].split('=')[1]
    myweekday = result[1].split('=')[1]
    # print(mytitleid)
    # print(myweekday)

    imgtag = abcd.find('img')
    mytitle = imgtag.attrs['title'].strip()
    mytitle = mytitle.replace('?', '').replace(':', '')
    # print(mytitle)

    mysrc = imgtag.attrs['src']
    # print(mysrc)

    saveFile(mysrc, myweekday, mytitle)

    # break

    subList = []
    subList.append(mytitleid)
    subList.append(myweekday)
    subList.append(mytitle)
    subList.append(mysrc)
    myList.append(subList)

from pandas import DataFrame

mycolumns = ['타이틀 번호', '요일', '제목', '링크']
myframe = DataFrame(myList, columns=mycolumns)

filename = 'cartoon.csv'

myframe.to_csv(filename, encoding='utf-8', index=False)
print(filename + '파일로 저장됨')

print('finished')