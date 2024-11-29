print('--------------------------------')
print('Welcome to tic-tac-toe!')
print('--------------------------------')

def drawBoard(board):
    print('\n')
    print(board[0] + '  | ' + board[1] + ' |' + board[2])
    print('---+---+---')
    print(board[3] + '  | ' + board[4] + ' |' + board[5])
    print('---+---+---')
    print(board[6] + '  | ' + board[7] + ' |' + board[8])
    print('\n')

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
drawBoard(board)
sign = 'X'
for k in range(0, 9, 1):
    index = int(input('enter the position : '))
    board[index - 1] = sign
    drawBoard(board)
    if sign == 'X':
        sign = '0'
    else:
        sign = 'X'

