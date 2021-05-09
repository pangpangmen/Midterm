"""
Created on Mon Apr 11 20:58:18 2021

@author: 123
"""

medals=[]
list2=[]
n=int(input("輸入筆數n："))
while (n<=4):
    for i in range(0,n):
        name,num=input("").split(" ")
        medals.append(name)
        list2.append(num)
    for j in range(len(medals)):
        print(str(medals[j])+"牌得到"+str(list2[j])+"面")