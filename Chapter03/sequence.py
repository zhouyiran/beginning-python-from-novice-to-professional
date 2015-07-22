# coding:utf-8
months = [
    'January',
    'February',
    'March',
    'April'
    'May',
    'June1',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
          + ['st', 'nd', 'rd'] + 7 * ['th'] \
          + ['st']
print(endings)

'''
year = raw_input('Year')
month = raw_input('Month (1-12)')
day = raw_input('Day (1-31)')
month_number = int(month)
day_number = int(day)
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]
print(month_name + '_'  + ordinal + '. ' + year)
'''

tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(number[0:-1])
print(number[:])
print(number[0:-1:2])
print(number[8:3:-1])
print(number[4:9:1])
# Why
print(number[-3:])
print(number[:])
print(number[:2])
'''
url = raw_input("please input the URL:")
domain = url[11:-4]
print("the domain :" + domain)
'''

print(number[-3:0:-1])
print(number[-3:0])

# 序列相加
print([1, 2, 3] + [4, 5, 6])
print('python' * 10)

# 成员资格
permissions = 'rw'
print('w' in permissions)

if 'z' in permissions:
    print('I wait you forever')
else:
    print('I will go leave')

users = ['mlh', 'foo', 'bar']
'''print(raw_input('enter your name: ') in users)'''

databases = [['sone', 1], ['aron', 2], ['alexg', 3]]

print(max(number))
print(max('12121jjj1'))
print(len('thisfsdfsdfdd'))
print(list('hello'))


names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[1]
print(names)


