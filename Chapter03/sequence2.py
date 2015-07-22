# coding:utf-8
__author__ = 'Administrator'
numbers = [1,7,5]
numbers[1:2] = [2,3,4]
print(numbers)
number = [1,2,3,4,5]
number[1:4] = []
print(number)

numbers.append([12,2,3])
print(numbers)

a = [1,2,3]
b = [4,5,6]
a + b
a[len(a):] = b
print(a)
knights = ['We', 'are', 'the','knights','who', 'say', 'ni']
try:
    print(knights.index('whoshui'))
except ValueError:
    print("ValueError:'whoshui' is not in list")


# insert
numbers = [1,2,3,4,5]
numbers.insert(2,"two")
print(numbers)
numbers.pop(2)
print(numbers)
print(numbers.pop(1))

x = [1,2,8,4,5,7]
y = sorted(x)
print(y)

group = (1,2,3)
print(group)
print(3*(40,))

#tuple转换序列Wie元组
z= tuple([1,2,3])
print(z)
y = tuple('21212')
print(y)
groupCount = group.count(2)
print(groupCount)
print(len(group))