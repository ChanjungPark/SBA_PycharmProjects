# operatorTest02.py
x = 5   # 기호는 대입 연산자

# 복합 연산자
x += 3  # x = x + 3
print('x : ', x)
print('-' * 30)

x *= 4
print('x : ', x)
print('-' * 30)

x %= 5
print('x : ', x)
print('-' * 30)

x -= 1
print('x : ', x)
print('-' * 30)

x += 7
print('x : ', x)
print('-' * 30)

# ; : 한 줄에 여러개의 서로 다른 코딩을 하고자 할 때 사용한다.
# 1부터 10까지의 합은 55입니다.
total = 0
total += 1;   total += 2;   total += 3;
total += 4;   total += 5;   total += 5;
total += 7;   total += 8;   total += 9;
total += 10;
print('total : ', total)