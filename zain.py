import numpy as np
#import tensorflow as tf
#import pandas as pd
#from sklearn import tree
#from sklearn import preprocessing
from random import randint

def cast(board):
    global masks
    global masks_down
    global masks_up
    global masks_3x3
    global oponent_completness
    global own_completness
    global rows
    global oponent_rows
    num = 0
    for i in reversed(board):
        for j in i:
            num = (num*10) + j
    return num

def recorre2(long, num, shiftit):
    global masks
    global masks_down
    global masks_up
    global masks_3x3
    global oponent_completness
    global own_completness
    global rows
    global oponent_rows
    cont = 0
    #print("long")
    #print(num)
    for mask in masks:
        for x in mask:
            if(cont == 0):
                pass
                #print("caso 1")
                recorre(long,num,5,5,x, shiftit)
            elif(cont == 1):
                pass
                #print("caso 2")
                recorre(long,num,6,4,x, shiftit)
            elif(cont == 2):
                #pass
                #print("caso 3")
                recorre(long,num,5,4,x, shiftit)
        cont += 1


def recorre(long, num, length, height, mask, shiftit):
    global masks
    global masks_down
    global masks_up
    global masks_3x3
    global oponent_completness
    global own_completness
    global rows
    global oponent_rows
    temp = 0.0
    temp_l = []
    times = int(1 + long/8)
    #print("Numero: ", num)
    #print("Mascara: ",mask)
    for i in range(times):
        #print("time: "+ str(i))
        for j in range(length):
            #print("len: " + str(j))
            #print("J: " + str(j))
            if i < height:
                #print("Num:  ", num)
                temp, temp_l = wise(num, mask, shiftit)
                if (shiftit):
                    if temp > own_completness:
                        own_completness = temp
                        rows = []
                        #print(j)
                        for k in temp_l:
                            k += j
                            k %= 7
                            rows.append(k)
                else:
                    if temp > oponent_completness:
                        oponent_completness = temp
                        oponent_rows = []
                        #print(j)
                        for k in temp_l:
                            k += j
                            k %= 7
                            oponent_rows.append(k)
            num=int(num//10)

        if length == 6:
            num=int(num/10)
        elif length == 5:
            num = int(num/100)

        #print("Num :", num)


def wise(num, mask, shifit):
    global masks
    global masks_down
    global masks_up
    global masks_3x3
    global oponent_completness
    global own_completness
    global rows
    global oponent_rows
    mask << shifit
    res = 0
    pos = []
    cont = 0
    while(mask > 0):
        #print("Mask: ",mask)
        #print((mask % 10) == (num % 10))
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
        mask = int(mask//10)
        num = int(num//10)
        cont += 1
    #print("pos")
    #print("\n")
    return res,pos

def play(turn, board):
    global masks
    global masks_down
    global masks_up
    global masks_3x3
    global oponent_completness
    global own_completness
    global rows
    global oponent_rows
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
   # test1 = [
   #        [0,0,0,0,0,0,0],
   #         [0,0,0,0,0,0,0],
   #         [0,0,1,0,0,0,0],
   #         [0,0,0,1,2,2,2],
   #         [0,0,0,0,1,0,0],
   #         [0,0,0,0,0,0,0]
   #         ]
    kuz = cast(board)

    #print(kuz)
    recorre2(len(str(kuz)),kuz, 0)
    recorre2(len(str(kuz)), kuz, 1)
    #print(wise(kuz/100000, masks_up[1]))
    #print(own_completness)
    #print(rows)
    f = open('log.txt', 'a')
    f.write('matrix: ' + str(kuz))
    f.write('\nown: ' + str(own_completness))
    f.write('\nopo: ' + str(oponent_completness))
    if(oponent_completness >= 75 and own_completness < 75):
        f.write('\nMove: block')
        f.write('\n\n')
        f.close()
        return oponent_rows[0]
    if(own_completness == 0):
        f.write('\nMove: random')
        f.write('\n\n')
        f.close()
        return randint(0,6)
    place = rows[0]
    f.write('\nMove: informed')
    f.write('\n\n')
    f.close()
    return place

def completeness():
    global own_completness
    return own_completness

if __name__ == "__main__":
    play()
