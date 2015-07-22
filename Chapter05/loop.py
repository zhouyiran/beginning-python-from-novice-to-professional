# coding:utf-8
__author__ = 'Administrator'

from math import  sqrt

x = 1
while x <= 100:
    print(x)
    x += 1

# while循环
'''
name = ''
while not name:
    name = raw_input("Please enter your name")
print('Hell . %s!' % name)
'''

# for循环
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for nubmer in numbers:
    print(nubmer)

print(range(10, 20))

for number in range(1, 101):
    print(number)

d = {"x": 1, "y": 2, "z": 3}

for key in d:
    print(key, "corresponds to ", d[key])

for key, value in d.items():
    print(key, 'corresponds to ', value)

names = ['name', 'beth', 'george', 'damon']
ages = [12, 34, 423, 122]

for i in range(len(names)):
    print names[i], 'is', ages[i], 'years old'

ziploop = zip(names,ages)
print ziploop

for name,age in zip(names,ages):
    print name,'is',age,'years old'


# 编号迭代

strings = ['xx111x','zzz','vvv','xxx']
'''for string in strings:
    if 'xxx' in string:
        index = strings.index(string)
        strings[index] = '[censored]'

print(strings)
'''

index = 0
for string in strings:
    if 'xxx' in string:
        strings[index] = '[censored]'
    index +=1

print(strings)

for index,string in enumerate(strings):
    if '[censored' in string:
        strings[index] = 'xxxxxxxx'

print(strings)

sortedList = sorted([3,4,56,12,21,4235])
print(sortedList)
helloWordSorted = sorted('Hello,World!')
print(helloWordSorted)
reversedList = list(reversed('hello world'))
print(reversedList)


spaceBackJoin = ''.join(reversed('Hello,world!'))
print(spaceBackJoin)



print(range(99,0,-1))
for n in range(99,0,-1):
    root = sqrt(n)
    print(int(root),"xxxxxxxxxxxx")
    if root == int(root):
        print n
        break

# while True/break
word = 'dummy'
while word:
    word = raw_input('Please enter a word')
    # 处理word
    print 'The word was' + word


'''
word = raw_input("Please enter a word")
while word:
    # 处理word
    print 'The word was' + word
    word = raw_input("Please enter a word")
'''

print([x*x for x in range(10)])

print([x*x for x in range(10) if x % 3 == 0])

print([(x,y) for x in range(3) for y in range(3)])


result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))


print(result)

girls = ['alice1', 'bernice','clarice']
boys= ['chri','ccccc','bob1']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]

#什么都没发生

if name == 'Ralph Auldus Melish':
    print 'Welcom'
elif name == 'Enid':
    pass
elif name == 'Bill Gates':
    print 'Access Denied'



x  = 1
del x
# print x


exec 'print "hello word"'

from math import sqrt
scope = {}
exec 'sqrt= 1' in scope
print(sqrt(4))
print(scope['sqrt'])

fibs = [0,1]
for i in range(8):
    fibs.append(fibs[-2]+fibs[-1])

print(fibs)




