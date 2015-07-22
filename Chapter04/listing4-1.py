# coding:utf-8
# A simple database

# A dictionary with person names as keys. Each person is represented as
# another dictionary with the keys 'phone' and 'addr' referring to their phone
# number and address, respectively.

people = {

    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },

    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },

    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }

}

# Descriptive labels for the phone number and address. These will be used
# when printing the output.
labels = {
    'phone': 'phone number',
    'addr': 'address'
}

# name = raw_input('Name: ')
name = 'Alice'

# Are we looking for a phone number or an address?
#request = raw_input('Phone number (p) or address (a)? ')
request = 'a'


# Use the correct key:
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# Only try to print information if the name is a valid key in
# our dictionary:
if name in people: print "%s's %s is %s." % \
    (name, labels[key], people[name][key])


# 使用字典的格式化字符串
phonebook = {"Beth":'91023','Alice':"23457","Cecil":"5566"}
s = "Cecil's phone number is %(Cecil)s." % phonebook
print(s)

template = '''<html>
    <head><title>%(title)s</title></head>
    <body>
        <h1>%(title)s</h1>
        <p>%(text)s</p>
    </body>'''

data = {"title":"My Home Page","text":"Welcom to my home page"}
print(template % data)

d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)

d.clear()
print(d)

x = {"key":"Value"}
y = x
print(y)

x.clear();
print(y)

d  = {}
d.setdefault("name","To")
print(d)
d['name'] = 'JACK'

print('Age',42)

name = 'AngleaBaby'
salutaion = 'Mr'
greeting = 'no'
print(name,salutaion,greeting)

x,y,z = 1,2,3
print(x,y,z)
x,y = y,x
print(x,y)