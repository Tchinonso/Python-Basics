fruits = ['mango','orange','cherry']
python = ['pie','pear','carrot','banana','apple']

print(fruits)
fruits[2]='kiwi'
print(fruits)
for x in fruits:
 print(x)
fruits.append('kiwi')
print(fruits)
fruits.extend(python)
print(fruits)
fruits.remove('orange')
print(fruits)
fruits.pop(3)
print(fruits)
fruits.insert(1,'pie')
print(fruits)
fruits.insert(3,'banana')
print(fruits)
fruits.insert(2,'apple')
print(fruits)
print(fruits[7])
print(fruits[2:7])