import random
import numpy as np

print("How many cards do you want to play?: ")
while True:
    try:
        n_cards = int(input())
        break
    except:
        print("Enter a number please")

cards = list(range(1,n_cards+1))
random.shuffle(cards)
cards = cards*2

mat = list(np.arange(1,n_cards+1))
mat2 = list(np.arange(1,n_cards+1))
random.shuffle(mat)
random.shuffle(mat2)

table = []
table.append(mat)
table.append(mat2)
hided_cards = np.matrix(table)

def ast_mat():                                  #funcion matriz de *s
    ma = table.copy()
    for i in range(2):
        for j in range(n_cards):
            ma[i][j] = '*'
    return ma
mat_ast = np.matrix(ast_mat())                  #Esta es la matriz que se muestra
print(hided_cards)                              #Matriz con la que trabajo

def end_game():
    global points_p1, points_p2
    total_points = points_p1 + points_p2 
    if total_points == n_cards:
        if points_p1 > points_p2:
            print("Player 1 won!")
        elif points_p1 < points_p2:
            print("¨Player 2 won!")
        else:
            print("Draw!")
        return 0            
def sum_points(turn,card1,card2):
    if card1 == card2:
        print("You won! It is still your turn...")
        if turn == 1:
            global points_p1
            points_p1 += 1
            mat_ast[x1,y1] = ""
            mat_ast[x2,y2] = ""
        else:
            global points_p2
            points_p2 += 1
            mat_ast[x3,y3] = ""
            mat_ast[x4,y4] = ""
        print(mat_ast)
    else:
        
        if turn == 1:
            turn = 2
        else:
            turn = 1
        print("Wrong card, now is Player ",turn,"´s turn...")
    print("Player 1: ", points_p1, "v/s Player 2: ", points_p2)
   

points_p1 = 0
points_p2 = 0
turn = 1

while True:
    if turn == 1:
        coord1 = input("Player 1 enter your coordinates in format x,y: ").split(",")
        x1,y1 = int(coord1[0]),int(coord1[1])
        print("your chosed card is: ", hided_cards[x1,y1])
        c1 = hided_cards[x1,y1]
        showed_mat = mat_ast.copy()
        showed_mat[x1,y1] = c1
        print(showed_mat)
        coord2 = input().split(",")
        x2,y2 = int(coord2[0]),int(coord2[1])
        print("your second chosed card is: ", hided_cards[x2,y2])
        c2 = hided_cards[x2,y2]
        showed_mat[x2,y2] = c2
        print(showed_mat)
        sum_points(turn, c1, c2)
    elif turn == 2:
        coord3 = input("Player 2 enter your coordinates in format x,y: ").split(",")
        x3,y3 = int(coord3[0]),int(coord3[1])
        print("your chosed card is: ", hided_cards[x3,y3])
        c3 = hided_cards[x3,y3]
        showed_mat = mat_ast.copy()
        showed_mat[x3,y3] = c3
        print(showed_mat)
        coord4 = input("Player 2 Enter your coordinates in format x,y: ").split(",")
        x4,y4 = int(coord4[0]),int(coord4[1])
        print("your second chosed card is: ", hided_cards[x4,y4])
        c4 = hided_cards[x4,y4]
        showed_mat[x4,y4] = c4
        print(showed_mat)
        sum_points(turn, c3, c4)

    if end_game() == 0:
        break














