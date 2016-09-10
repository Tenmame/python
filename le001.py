#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

print "你好\n"
s1 = set([1,2,3])
print s1
def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y


# list define
names = ['Tom', 'Kely']

# tuple => value can not be changed
classmates = ('Tom','Bob')
# define tuple which length is 1
t = (1,)
# define tuble which value is 1
t1 = (1)
# dictionary <==> map  key-value
names = {'Michel': 95,'Bob' :78}

# set define  =>key
s = set([1, 2, 3])

# 默认参数
def cals(n, m = 2):
	pass

# 可变参数 * tuble
def calc(*numbers):
	pass
# 关键字参数 参数名和值同时做参数 dic
def person(name,age, **kw)