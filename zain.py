import numpy as np
import tensorflow as tf
import pandas as pd
import os
from sklearn import tree
from sklearn import preprocessing


def cast(board):
    num = 0
    for i in board:
        for j in i:
            num = (num*10) + j
    return num

def recorre2(long, num):
    cont = 0
    for mask in masks:
        for x in mask:
            if(cont == 0):
                recorre(long,num,4,4)
            elif(cont == 1):
                recorre(long,num,5,3)
            elif(cont == 2):
                recorre(long,num,4,3)
    cont += 1
            

def recorre(long, num, length, height, mask):
    temp = 0.0
    temp_l = []
    times = int(1 + long/7)
    linea = 0
    for i in range(times):
        for j in range(length):
            if i < height:
                temp, temp_l = wise(num, mask)
                if temp > own_completness:
                    own_completness = temp
                    rows = []
                    for k in temp_l:
                        k += length
                        k %= 7
                        k += 1
                        rows.append(k)
                    
            num/=10
        num/=1000
       
def recorreOponent(long, num):
    times = int(1 + long/7)
    linea = 0
    for i in range(times):
        for j in range(4):
            for m in masks_simple:
                oponent_completness, _ = wise(num, m)
            if i < 6:
                for m in masks_compl:
                    oponent_completness, _ = wise(num, m)
            num/=10
        num/=1000         

def wise(num, mask):
    res = 0
    pos = []
    cont = 0
    while(mask > 0):
        if((mask % 10 ) == 0):
            continue
        if ((mask % 10) == (num % 10)):
            res += .25
        elif((num % 10) > 0):
            return -1,[]
        else:
            pos.append(cont)
        mask /= 10
        num /= 10
        cont += 1
    return res,pos

def main():
    global masks, masks_down, masks_up, masks_3x3, oponent_completness, own_completness, rows
    oponent_completness = 0
    own_completness = 0
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
            10100000100000100# T (-135) superior izquierda
            ]
    masks = [
            masks_down, # reccore con (4,3) * 4
            masks_up, # recorre  (5,2) * 3
            masks_3x3 # recorre (4,3) * 3
            ]
    

def cehckMask():
    pass

def checPosible():
    pass


if __name__ == "__main__":
    main()