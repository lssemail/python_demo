myNumber = list(range(5))
for num in myNumber:
    print(num)

myInfo = dict()
myInfo['name'] = 'Python'
myInfo['height'] = 60

print(myInfo)
print(myInfo.get('name'))
print('height' in myInfo)
print(myInfo.get('name123'))
