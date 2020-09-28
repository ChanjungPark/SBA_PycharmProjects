# getUrl.py
# 네이버 사이트의 url 정보 취득

# client-server 환경
import urllib.request

url = 'https://www.naver.com'   # 요청 url

# 파라미터 추가
# ? : url과 parameter의 구분자 역할
# = : parameter 이름과 실제 값의 구분자 역할
# & : parameter 간의 구분자 역할
parameter = '?'
parameter += 'id=asdf'
parameter += '&password=1234'
parameter += '&message=hahaha'

url += parameter

print(url)
print('-' * 30)

# req : 요청 객체
req = urllib.request.Request(url)

# response : 응답 객체
response = urllib.request.urlopen(req)
print(response)
print('-' * 30)

# 응답 객체를 바이트 형태로 바꾼(read()) 다음, 볼 수 있도록 텍스트로 변환합니다.
print(response.read().decode('utf-8'))