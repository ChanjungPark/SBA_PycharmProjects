# variantArgs02.py
# minval : 튜플 요소에서 가장 큰 수와 가장 작은 수를 반환하는 함수 만들기
# def minval(*args):
#     myMin = min(args)
#     myMax = max(args)
#     return myMin, myMax

def minval(*args):
    myList = [ item for item in args]
    myList.sort()
    return myList[0], myList[-1]

print(minval(3, 5, 8, 2))   # (2, 8)