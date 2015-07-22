# -*- coding: utf-8 -*-

# ====================
# File: abop.py
# Author: Wendy
# Date: 2013-12-03
# ====================

# eclipse pydev, python3.3
from math import pi

age = 25
name = 'Caroline'

print('{0} is {1} years old. '.format(name, age))  # 输出参数

s = 'Using repr %s ' % '3232L rEPS'
print(s)
s = '%10f' % pi
print(s)

s = '%.2f ' % pi
print(s)  # 精度为2

s = '%.5s' % 'Guido van Rossum•'
print(s)

s = '%.*s' % (7, 'Guidos van Rossum•')
print(s)

# 符号 对齐和0填充
s = '%010.2f' % pi
print(s)

# 减号(-)左对齐
s = '%-10.2f' % pi
print(s)
print(len(s))

# 空白("")
print('% 5d' % 10 + '\n' + '% 5d' % -10)

# 打印价格列表
width = input('Please enter width:')

price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
format = '%-*s%*.2f'

print '=' * width

print header_format % (item_width, 'Item', price_width, 'Price')

print '-' * width

print format % (item_width, 'Apple', price_width, 48.123)

print '=' * width

