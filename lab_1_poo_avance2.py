# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import numpy as np

n_cartas = int(input("ingrese la cantidad de cartas que se jugarán:"))
print("El numero de cartas que habrán seran:", n_cartas*2, ", es decir habran ", n_cartas, "pares en juego.")

cards = list(range(1,n_cartas+1))
random.shuffle(cards)
cards = cards*2

mat = list(np.arange(1,n_cartas+1))
mat2 = list(np.arange(1,n_cartas+1))
random.shuffle(mat)
random.shuffle(mat2)

tablero = []
tablero.append(mat)
tablero.append(mat2)
hided_cards = np.matrix(tablero)


def ast_mat():    #funcion matriz de *s
    ma = tablero.copy()
    for i in range(2):
        for j in range(n_cartas):
            ma[i][j] = '*'
    return ma
mat_ast = np.matrix(ast_mat())                  #Esta es la matriz que se muestra
print(hided_cards)                              #Matriz con la que trabajo


points_p1 = 0
points_p2 = 0
turn = 1

while True:
    if turn == 1:
        print("Player 1 ingress your coordinates ")
        x1,y1 = int(input()),int(input())        
        print("your chosed card is: ", hided_cards[x1,y1])
        c1 = hided_cards[x1,y1]
        showed_mat = mat_ast.copy()
        showed_mat[x1,y1] = c1
        print(showed_mat)
        x2,y2 = int(input()),int(input())
        print("your second chosed card is: ", hided_cards[x2,y2])
        c2 = hided_cards[x2,y2]
        showed_mat[x2,y2] = c2
        print(showed_mat)
        if c1 == c2:
            print("You won! It is still your turn...")
            points_p1 += 1
            turn = 1 
            mat_ast[x1,y1] = ""
            mat_ast[x2,y2] = ""
            print(mat_ast)
            print("Player 1: ", points_p1, "v/s Player 2: ", points_p2)
        else:
            print("Wrong card, now is Player 2´s turn...")
            turn = 0
            print("Player 1: ", points_p1, "v/s Player 2: ", points_p2)
            print(mat_ast)
    elif turn == 0:
        print("Player 2 ingress your coordinates ")
        x3,y3 = int(input()),int(input())
        print("your chosed card is: ", hided_cards[x3,y3])
        c3 = hided_cards[x3,y3]
        showed_mat = mat_ast.copy()
        showed_mat[x3,y3] = c3
        print(showed_mat)
        x4,y4 = int(input()),int(input())
        print("your second chosed card is: ", hided_cards[x4,y4])
        c4 = hided_cards[x4,y4]
        showed_mat[x4,y4] = c4
        print(showed_mat)
            
        if c3 == c4:
            print("You won! It is still your turn...")
            points_p2 += 1
            turn = 0
            mat_ast[x3,y3] = ""
            mat_ast[x4,y4] = ""
            print(mat_ast)
            print("Player 1: ", points_p1, "v/s Player 2: ", points_p2)
        else:
            print("Wrong card, now is Player 1´s turn...")
            turn = 1
            print("Player 1: ", points_p1, "v/s Player 2: ", points_p2)
            print(mat_ast)















