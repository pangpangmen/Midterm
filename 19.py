"""
Created on Mon Apr 12 23:27:08 2021

@author: 123
"""

group=int(input("組數為："))
for i in range(group):
    i+=1
    a,c=input("第%d組為：" % i).split(" ")
    a=int(a)
    c=int(c)
    fee=(a*250)+(c*175)
    print("第%d組應收費用：%d" % (i,fee))