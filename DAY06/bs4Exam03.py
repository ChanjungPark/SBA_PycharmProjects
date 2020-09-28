# bs4Exam03.py
'''
사이트 주소 : https://movie.naver.com/movie/sdb/rank/rmovie.nhn

수집할 내용 :
순위 : 숫자 2자리 형식으로 가져오기(zfill() 함수)
제목 :
변동 : 불변, 상승, 강등
변동 값 : 숫자

<table>
    <tr>
        <td></td>
        <td></td>
    </tr>
</table>

크롤링 순서
순위를 나타내는 항목들이 표(table) 형식으로 구성되어 있습니다.

모든 행과 관련된 <tr> 태그를 찾습니다.
    <td class="title">인 항목을 찾습니다.
    None이 아닌 경우에 한하여
        순위를 지정합니다.
        제목은 <div class='tit3'>인 항목을 찾습니다.
        변동 여부를 위하여 3번째 <td> 요소를 찾습니다.
            하위 img 태그의 'alt'속성에 대하여 분기 처리합니다.
        변동된 숫자를 찾기 위하여 <td class="range ac"> 요소를 찾습니다.

        totallist에 append 시킵니다.
'''
import urllib.request

from bs4 import BeautifulSoup
from pandas import DataFrame

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))

tags = soup.findAll('div', attrs={'class':'tit3'})
print(tags)
print('-' * 30)

for tag in tags:
    print(tag.a.string)
print('-' * 30)

print('<a> 태그의 href 전체 태그')
url_header = 'https://movie.naver.com'
for tag in tags:
    print(url_header + tag.a['href'])
print('-' * 30)

mytrs = soup.find_all('tr')
print(len(mytrs))
print('-' * 30)

no = 0  # 순서를 의미하는 번호
totallist = []  # 전체를 저장할 리스트

for one_tr in mytrs:
    # print(one_tr)
    # print('@' * 30)

    title = ''
    up_down = ''    # '상승/하강/불변'을 위한 설명 문구

    mytd = one_tr.find('td', attrs={'class':'title'})
    if(mytd != None):
        no += 1
        newno = str(no).zfill(2)

        mytag = mytd.find('div', attrs={'class':'tit3'})
        # string 속성 : 해당 태그가 가지고 있는 문자열을 출력
        title = mytag.a.string

        # td 태그 중에서 3번째 요소를 찾기
        mytd = one_tr.select_one('td:nth-of-type(3)')
        myimg = mytd.find('img')
        if myimg.attrs['alt'] == 'up':
            up_down = '상승'
        elif myimg.attrs['alt'] == 'down':
            up_down = '강등'
        else:
            up_down = '불변'

        change = one_tr.find('td', attrs={'class':'range ac'})
        change = change.string

        # print(newno + '/' + title + '/' + up_down +'/' + change)
        totallist.append(newno, title, up_down, change)

mycolumn = ['순위', '제목', '변동', '변동값']
myframe = DataFrame(totallist, columns=mycolumn)

filename = 'naverMovie.csv'

myframe.to_csv(filename)

print(filename + '파일 저장됨')
print('-' * 30)