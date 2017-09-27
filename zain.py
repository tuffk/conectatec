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
        cont += 1
    return res,pos

def main():
    global masks
    masks = [
            100000110000001, # T palito izquierda
            1110000010, # T normal
            100000111, # T invertida 
            1000000110000010, # T palito derecha
            100000100000101,# T (45) inferior derecha
            10100000100000001,# T (135) superior derecha
            10000000100000101, # T (-45) inferior izquierda
            10100000100000100# T (-135) superior izquierda
            ]
    #zain = int(bin(11) & bin(11))
    print(100001 & 10001)

def cehckMask():
    pass

def checPosible():
    pass


if __name__ == "__main__":
    main()