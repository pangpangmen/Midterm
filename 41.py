# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 00:08:45 2021

@author: 123
"""

a=int(input("請輸入a值"))
b=int(input("請輸入b值"))
c=int(input("請輸入c值"))

x1=(-b+(((b**2)-(4*a*c))**0.5))/2*a
x2=(-b-(((b**2)-(4*a*c))**0.5))/2*a
x3=(-b)/(2*a)
if (b**2)-(4*a*c)>0:
    ans=(x1,x2)
if (b**2)-(4*a*c)==0: 
    ans=(x3)
if (b**2)-(4*a*c)<0:
    ans=(0)
print(ans)    