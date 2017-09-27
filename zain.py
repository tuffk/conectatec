import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn import tree
from sklearn import preprocessing


def cast(board):
    global masks
    global masks_down
    global masks_up
    global masks_3x3
    global oponent_completness
    global own_completness
    global rows
    num = 0
    for i in board:
        for j in i:
            num = (num*10) + j
    return num

def recorre2(long, num):
    global masks
    global masks_down
    global masks_up
    global masks_3x3
    global oponent_completness
    global own_completness
    global rows
    cont = 0
    #print("long")
    #print(num)
    for mask in masks:
        for x in mask:
            if(cont == 0):
                #print("caso 1")
                recorre(long,num,5,5,x)
            elif(cont == 1):
                #print("caso 2")
                recorre(long,num,6,3,x)
            elif(cont == 2):
                #print("caso 3")
                recorre(long,num,5,3,x)
        cont += 1
            

def recorre(long, num, length, height, mask):
    global masks
    global masks_down
    global masks_up
    global masks_3x3
    global oponent_completness
    global own_completness
    global rows
    temp = 0.0
    temp_l = []
    times = int(1 + long/8)
    for i in range(times):
        #print("time: "+ str(i))
        for j in range(length):
            #print("len: " + str(j))
            #print("J: " + str(j))
            if i < height:
                temp, temp_l = wise(num, mask)
                #print(temp)
                if temp > own_completness:
                    own_completness = temp
                    rows = []
                    #print(temp_l)
                    #print(j)
                    for k in temp_l:
                        k += j
                        k %= 7
                        #k += 1
                        rows.append(k)
                    
            num=int(num/10)
        num=int(num/100)
     

def wise(num, mask):
    global masks
    global masks_down
    global masks_up
    global masks_3x3
    global oponent_completness
    global own_completness
    global rows
    res = 0
    pos = []
    cont = 0
    while(mask > 0):
        #print(mask)
        if((mask % 10 ) == 0):
            mask = int(mask/10)
            num = int(num/ 10)
            cont += 1
            continue
        if ((mask % 10) == (num % 10)):
            res += 25
        elif((num % 10) > 0 and not(mask%10 == 0)):
            return -1,[]
        else:
            pos.append(cont)
        mask = int(mask/10)
        num = int(num/ 10)
        cont += 1
    #print("pos")
    #print(pos)
    return res,pos

def main():
    global masks
    global masks_down
    global masks_up
    global masks_3x3
    global oponent_completness
    global own_completness
    global rows
    oponent_completness = 0.0
    own_completness = 0.0

    rows = []
    masks_down = [
            1110000010, # T normal
            100000111, # T invertida 
            ]
    masks_up = [
            100000110000001, # T palito izquierda
            1000000110000010, # T palito derecha
            ]
    masks_3x3 = [
            100000100000101,# T (45) inferior derecha
            10100000100000001,# T (135) superior derecha
            10000000100000101, # T (-45) inferior izquierda
            10100000100000100 # T (-135) superior izquierda
            ]
    masks = [
            masks_down, # reccore con (4,3) * 4
            masks_up, # recorre  (5,2) * 3
            masks_3x3 # recorre (4,3) * 3
            ]
#    test1 = [
#            [0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0],
#            [0,0,2,2,1,1,1],
#            [0,2,1,1,2,2,1]
#            ]
    test1 = [
            [0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,1,2,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
            ]
    kuz = cast(test1)
    recorre2(len(str(kuz)),kuz)
    #print(wise(kuz/100000, masks_up[1]))
    print("algo")
    print(own_completness)
    print(rows)



if __name__ == "__main__":
    main()