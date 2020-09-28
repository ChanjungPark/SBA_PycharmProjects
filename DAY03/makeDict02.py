# makeDict02.py
fruits = [('바나나', 10), ('수박', 20), ('오렌지', 30)]

# myDict = {} # empty dict
myDict = dict() # empty dict

for key, value in fruits:
    myDict[key] = value

print(myDict)
print('-' * 40)

myDict.clear()

fruits = [('바나나', 10), ('수박', 20), ('오렌지', 30), ('바나나', 50)]

for key, value in fruits:
    if not(key in myDict):   # 들어있지 않으면
        myDict[key] = value
    else :
        imsi = myDict[key]
        myDict[key] = imsi + value

print(myDict)
print('-' * 40)