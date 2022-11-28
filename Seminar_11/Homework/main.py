# -*- mode: python ; coding: utf-8 -*-
from sympy import *
x = Symbol('x')
function_1 = x**3 - 50*x
function_2 = - x**4 + 88*x**2 - 241
common_function = function_1 - function_2
plot(function_1,function_2)
plot(common_function)
x_list = solve(common_function)
x_list[0] = x_list[0].evalf(10, chop=True)
x_list[1] = x_list[1].evalf(10, chop=True)
x_list[2] = x_list[2].evalf(10, chop=True)
x_list[3] = x_list[3].evalf(10, chop=True)
x1 = x_list[0]
x2 = x_list[1]
x3 = x_list[2]
x4 = x_list[3]
y1 = function_1.subs(x, x1)
y2 = function_1.subs(x, x2)
y3 = function_1.subs(x, x3)
y4 = function_1.subs(x, x4)
print(f'Точки пересечения функций {function_1} и {function_2}:\nТочка 1: x = {x1} y = {y1}\nТочка 2: x = {x2} y = {y2}\nТочка 3: x = {x3} y = {y3}\nТочка 4: x = {x4} y = {y4}')
