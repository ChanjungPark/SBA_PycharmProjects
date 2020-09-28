# generateList.py
kim = ['김유신', 10, 20]
lee = ['이순신', 30, 40]
park = ['박영희', 60, 50]
student = [kim, lee, park]
print(student)
print('-' * 60)

# myList = [] # empty list
myList = list() # empty list
print(myList)
print('-' * 60)

for subList in student :
    myList.append([subList[0], subList[1] + subList[2]])

print(myList)
print('-' * 60)