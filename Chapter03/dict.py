# coding:utf-8
__author__ = 'Administrator'

# 建立字典
items = [('name','GongBi'),('age','43')]
d = dict(items)
print(d['name'])

d = dict(name='Js',age=42)
print(d['name'])
print('name' in d)


x = {}
x[42] = 'foobar'
print(x)
print(x[42])


dict = {}
c = dict.setdefault("a",[])
print(c)