
"""
Created on Mon Apr 11 19:58:18 2021

@author: 123
"""


m=int(input("輸入月份:"))
d=int(input("輸入日:"))
s=(m*2+d)%3
if s==0:
    print("普通")
elif s==1:
    print("吉")
elif s==2:
    print("大吉")