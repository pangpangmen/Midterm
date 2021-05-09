
"""
Created on Mon Apr 11 20:12:58 2021

@author: 123
"""

data=int(input("測試的資料量："))
for i in range(data):
    f,m,k=input("父、母、子女的血型：").split(" ")
    if f=="O" and m=="O" and k=="O":
        print("YES")
    elif f=="O" and m=="A" and (k=="A" or k=="O"):
        print("YES")
    elif f=="O" and m=="B" and (k=="B" or k=="O"):
        print("YES")
    elif f=="O" and m=="AB" and (k=="A" or k=="B"):
        print("YES")
    elif f=="A" and m=="A" and (k=="A" or k=="O"):
        print("YES")
    elif f=="A" and m=="B" and (k=="A" or k=="B" or k=="O" or k=="AB"):
        print("YES")
    elif f=="A" and m=="AB" and (k=="A" or k=="B" or k=="AB"):
        print("YES")
    elif f=="B" and m=="B" and (k=="B" or k=="O"):
        print("YES")
    elif f=="B" and m=="AB" and (k=="A" or k=="B" or k=="AB"):
        print("YES")
    elif f=="AB" and m=="AB" and (k=="A" or k=="B" or k=="AB"):
        print("YES")
    else:
        print("IMPOSSIBLE")
    
    

    
    