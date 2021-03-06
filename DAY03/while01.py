# while01.py
# 1부터 10까지의 총합을 구해보겠습니다.

total = 0
i = 1   # 초기식 정의

# while 조건식 :
while i < 11:
    total += i
    i += 1  # 증감식

print('총합01 : %d' % (total))
print('-' * 30)

# 2 + 5 + 8 + ... + 47 + 50 = 442
total = 0
i = 2

while i <= 50:
    total += i
    i += 3

print('총합02 : %d' % (total))
print('-' * 30)

# 1 + 3 + 5 + ... + 97 + 99 = 2500
total = 0
i = 1

while i < 100:
    total += i
    i += 2

print('총합03 : %d' % (total))
print('-' * 30)