import numpy as np
# sudoku = []
# print('Please use 0 in the place of blank')

# for i in range(9):
#     row = list(input('Enter the elements of row {} without spaces and comma'.format(i+1)))
#     row = [int(i) for i in row]
#     sudoku.append(np.array(row))
# print(np.matrix(sudoku))
sudoku = np.array([[5,3, 0, 0 ,7 ,0 ,0 ,0 ,0],
 [6 ,0 ,0 ,1 ,9 ,5 ,0, 0 ,0],
 [0, 9, 8, 0 ,0 ,0 ,0 ,6 ,0],
 [8 ,0 ,0 ,0 ,6 ,0 ,0, 0, 3],
 [4 ,0 ,0 ,8 ,0 ,3 ,0 ,0 ,1],
 [7 ,0, 0, 0 ,2 ,0 ,0 ,0 ,6],
 [0 ,6, 0, 0 ,0 ,0 ,2 ,8, 0],
 [0 ,0, 0 ,4 ,1 ,9 ,0 ,0, 5],
 [0 ,0, 0, 0 ,8 ,0, 0, 7 ,9]
 ])
print(sudoku)
def possible(y, x, n):
    global sudoku
    for i in range(9):
        if sudoku[y][i] == n:
            return False
    for i in range(9):
        if sudoku[i][x] == n:
            return False
    box_y = (y//3)*3
    box_x = (x//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[box_y+i][box_x+j] == n:
                return False 
    return True                

def solve():
    for y in range(0,9):
        for x in range(0,9):
            if sudoku[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        sudoku[y][x] = n
                        solve()
                        sudoku[y][x] = 0
                return sudoku 

    print(sudoku)
    input('More Solutions')
sorted = solve()
print(sorted)