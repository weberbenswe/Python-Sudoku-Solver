#this creates a sample test board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
'''this actually solves the board recursively'''
def solve(bo):
    '''uses fun find_empty to find next empty space'''
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find  
    '''looks at all pos 1-9 and checks if they are valid'''  
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            '''recursion for resetting last pos to 0'''
            if solve(bo):
                return True
            bo[row][col] = 0
    
    return False

'''function checks if board is valid'''
def valid(bo, num, pos):
    '''checks length for no repeat nums'''
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    '''checks width for no repeat nums'''
    for i in range(len(bo)):
        if bo[pos[1]] == num and pos[0] != i:
            return False
    '''checks box for no repeat nums'''
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

#this creates a print statement for the board with formatting
def print_board(bo):
    '''looks for vertical length'''
    for i in range(len(bo)):
        '''every 3 vertical positions prints separators'''
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')
        '''looks for horiszontal length'''
        for j in range(len(bo[0])):
            '''every 3 horizontal positions prints separators'''
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            '''checks if alg is at the last position to create next line'''
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end='')
print_board(board)

'''this function looks for an empty position'''
def find_empty(bo):
    '''look at each pos in order to find next 0'''
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None

print('\n')
print_board(board)
print('\n')
solve(board)
print_board(board)
print('\n')