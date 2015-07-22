# coding:utf-8

__author__ = 'Administrator'
print(True + False + 42)

s = bool('I think Im tired')
print(s
      )
bool([])

# name = raw_input("Entery your name ")
name = 'Jack'
if name.endswith("Jack"):
    print("hello , Jack")
else:
    print("Hello stanger")

# num = input("Enter a number")
num = 12
if num > 0:
    print 'The number is positive'
elif num < 0:
    print 'The number is negative'
else:
    print 'The number is zero'



# 嵌套代码块
name = 'Mr Gumby'
if name.endswith('Gumby'):
    if name.startswith("Mr"):
        print("hello Mr Gumby")
    elif name.startswith("Mrs"):
        print("Hello Mrs Gumby")
    else:
        print("Hello Gumby")
else:
    print("hell stranger")

# 相等运算符号
print("foo"=="bar")


# 同一性运算符
x=y=[1,2,3]
z=[1,2,3]
print(x==y)
print(x==z)
print(x is z)

x = [1,2,3]
y = [2,4]
print(x is not y)
del x[2]
y[1] =1
y.reverse()
print(x==y)
print(x is y)

# 成员资格
name = 'Jms'
if 's' in name:
    print("your name contains letter 's'")
else:
    print("your name not contains letter 's'")


# 字符串和序列比较
print('alpha' < 'beta')
print([2,[1,3]]< [2,[1,5]])

# 布尔运算符
number = 7
if number>=1 and number <=10:
    print("Great")
else:
    print("Wrong")