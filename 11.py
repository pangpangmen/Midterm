"""
Created on Mon Apr 11 20:17:18 2021

@author: 123
"""


m,d=input("輸入月及日為：").split(' ')
m=int(m)
d=int(d)

d=m*100+d

if d>=121 and d<=218:
    print("星座為：Aquarius")
elif d>=219 and d<=320:
    print("星座為：Pisces")
elif d>=321 and d<=420:
    print("星座為：Aries")
elif d>=421 and d<=521:
    print("星座為：Taurus")
elif d>=522 and d<=621:
    print("星座為：Gemini")
elif d>=622 and d<=722:
    print("星座為：Cancer")
elif d>=723 and d<=823:
    print("星座為：Leo")
elif d>=824 and d<=923:
    print("星座為：Virgo")
elif d>=924 and d<=1023:
    print("星座為：Libra")
elif d>=1024 and d<=1122:
    print("星座為：Scorpio")
elif d>=1123 and d<=1221:
    print("星座為：Sagittarius")
elif d>=1222 or d<=120:
    print("星座為：Capricorn")