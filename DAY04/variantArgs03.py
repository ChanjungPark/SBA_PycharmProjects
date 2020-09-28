# variantArgs03.py
# 매개 변수에 별 2개는 dict(사전)으로 인식합니다.
def myFunction(a, b=10, *args, **kwargs):
    print('a =', a)
    print('b =', b)
    print('*' * 30)

    print('튜플 출력')
    for item in args:
        if type(item) == str:
            print('문자열 :', item)
        elif type(item) == int:
            print('정수 :', item)
        elif type(item) == float:
            print('실수 :', item)
        else:
            print('기타 :', item)
    print('-' * 30)

    print('사전 출력')
    for key, value in kwargs.items():
        print('키 : {}, 값 : {}'.format(key, value))
    print('#' * 30)

# myFunction(10)
# myFunction(10, 20)
# myFunction(10, 20, 30, 'abc')
# myFunction(10, 20, 30, 'abc', 12.345, 50)
myFunction(10, 20, 30, 'abc', 12.345, 50, kim=(40, 50), park=30)