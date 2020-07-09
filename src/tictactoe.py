# attempt at tic tac toe game.

def drawBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[6] + '|' + board[7] + '|' + board[8])

def checkWin(board, char):
    if board[0] == char:
        if board[1] and board[2] == char:
            return True
        if board[3] and board[6] == char:
            return True
        if board[4] and board[8] == char:
            return True
    elif board[3] == char:
        if board[4] and board[5] == char:
            return True
    elif board[6] == char:
        if board[7] and board[8] == char:
            return True
    elif board[1] == char:
        if board[4] and board[7] == char:
            return True
    elif board[2] == char:
        if board[6] and board[8] == char:
            return True

    return False

print('Welcome to tic tac toe!')

play = True
board = [' ' for i in range(0,10)]

#while play == True:
 #   print('You are X, enter your location')
  #  choice = int(input())
   # board[choice] = 'X'
    #drawBoard(board)

print('testing checkWin... ')
print('empty board: ' + str(checkWin(board, 'X')))

board[0], board[1], board[2] = 'X', 'X', 'X'
print('top row win: ' + str(checkWin(board, 'X')))

board = [' ' for i in range(0,10)]
board[0], board[4], board[8] = 'X', 'X', 'X'
print('diagonal win: ' + str(checkWin(board, 'X')))

board = [' ' for i in range(0,10)]
board[3], board[4], board[5] = 'X', 'X', 'X'
print('mid row win: ' + str(checkWin(board, 'X')))

board = [' ' for i in range(0,10)]
board[3], board[4], board[5] = 'O', 'O', 'O'
print('mid row win for O, passing X: ' + str(checkWin(board, 'X')))
print('mid row win for O, passing O: ' + str(checkWin(board, 'O')))