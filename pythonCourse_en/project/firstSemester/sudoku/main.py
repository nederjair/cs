print('--------------------------------')
print('Welcome to Sudoku!')
print('--------------------------------')

def drawBoard(board):
    print('\n')
    print('---------------------')
    print('| ' + board[0] + '  | ' + board[1] + '  | ' + board[2] + '  | ' + board[3] + '  |' )
    print('---------------------')
    print('| ' + board[4] + '  | ' + board[5] + '  | ' + board[6] + '  | ' + board[7] + '  | ')
    print('---------------------')
    print('| ' + board[8] + '  | ' + board[9] + '  | ' + board[10] + '  | ' + board[11] + '  |')
    print('---------------------')
    print('| ' + board[12] + '  | ' + board[13] + '  | ' + board[14] + '  | ' + board[15] + '  |')
    print('---------------------')
    print('\n')

board = [' ', '2', '3', ' ',
         '1', ' ', ' ', '4',
         '2', ' ', ' ', '3',
         ' ', '1', '4', ' ']

drawBoard(board)
for k in range(0, 9, 1):
    index = int(input('enter the position : '))
    sign = input('enter the number: ')
    board[index - 1] = sign
    drawBoard(board)
