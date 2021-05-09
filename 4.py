# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 01:42:46 2021

@author: 123
"""

x=int(input("請輸入x值"))
y=int(input("請輸入y值"))
if x>0 and y>0:
    ans ="第一象限"
    a=(x**2+y**2)**0.5
if x<0 and y>0:
    ans ="第二象限"
    a=(x**2+y**2)**0.5
if x<0 and y<0:
    ans ="第三象限"
    a=(x**2+y**2)**0.5
if x>0 and y<0:
    ans ="第四象限"
    a=(x**2+y**2)**0.5
if x==0 and y==0:
    ans ="原點"
    a=(x**2+y**2)**0.5
if x==0 and y!=0:
    ans ="y軸上"
    a=(x**2+y**2)**0.5
if y==0 and x!=0:
    ans ="x軸上"
    a=(x**2+y**2)**0.5      
print(ans,"原點距離是",a)    