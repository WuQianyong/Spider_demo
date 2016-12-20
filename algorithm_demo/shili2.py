# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:20:54 2016

@author: wqy
"""

# 用户输入数字
num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')

# 求和
sum = float(num1) + float(num2)

# 显示计算结果
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))


"""
计算二次方程
ax**2 +bx +c =0
"""
import cmath
a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))
# 计算
d = (b**2) - (4*a*c)

# 两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('结果为 {0} 和 {1}'.format(sol1,sol2))