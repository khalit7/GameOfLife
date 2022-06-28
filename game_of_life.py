import os
import time
import random

def printmatrix(matrix):
    m,n = len(matrix),len(matrix[0])
    print("")
    print("")
    print("")
    for i in range(m):
        for j in range(n):
            val = "X" if matrix[i][j] == 1 else "."
            print(val, end = "")
        print("")

def gameOfLife(board) -> None:
    m,n = len(board),len(board[0])
    change = [ [False]*n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            neighbors = get_neighbors(board,i,j)
            num_of_ones = neighbors.count(1)
            #
            #print("index is {},{} and the neigbours are {}".format(i,j,neighbors))
            if board[i][j] == 1: # live cell
                if num_of_ones < 2 or  num_of_ones > 3:
                    change[i][j] = True
            else: # dead cell
                if num_of_ones == 3:
                    change[i][j] = True

    for i in range(m):
        for j in range(n):
            if change[i][j]:
                board[i][j] = 1 if board[i][j] == 0 else 0

    return board
                    
        
def get_neighbors(board,i,j):
    m,n = len(board),len(board[0])
    arr = [0]*8
    for i,index in  enumerate([(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]):
        if not 0<=index[0]<m or not 0<=index[1]<n:
            arr[i] = 0
        else:
            arr[i] = board[index[0]][index[1]]
        
    return arr

print("INPUT THE NUMBER OF ROWS AND COLUMNS OF THE WORLD (MAKE SURE YOUR SCREEN FITS, IF IN DOUBT, CHOOSE 35 ROWS AND 150 COLUMNS and use the terminal in full screen)")
m = int(input("numer of rows : "))
n = int(input("number of columns: "))
mat = [ [0]*n for _ in range(m) ]
arr = [0]*87 + [1]*13
for i in range(m):
    for j in range(n):
        mat[i][j] = random.choice(arr)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    printmatrix(mat)
    gameOfLife(mat)
    time.sleep(0.1)
