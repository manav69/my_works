

def insertLetter(letter, pos):
    board[pos]=letter

def spaceIsFree(pos):
    return board[pos]==' '

def printBoard(board):
    print(' | | ')
    print(''+board[1]+'|'+board[2]+'|'+board[3])
    print(' | | ')
    print('-----------')
    print(' | | ')
    print('' + board[4] + '|' + board[5] + '|' + board[6])
    print(' | | ')
    print('-----------')
    print(' | | ')
    print('' + board[7] + '|' + board[8] + '|' + board[9])
    print(' | | ')

def isWinner(bo,le):
    return (bo[7]==le and bo[8]==le and bo[9]==le) or\
    (bo[4]==le and bo[5]==le and bo[6]==le) or\
    (bo[1]==le and bo[2]==le and bo[3]==le) or\
    (bo[1] == le and bo[4] == le and bo[7] == le)or\
    (bo [2]==le and bo[5]==le and bo[8]==le)or\
    (bo[3]==le and bo[6]==le and bo[9]==le)

def playerMove():
    run= True
    while run:
        move=input('Please select position to place an X between 1-9')
        try:
            move=int(move)
            if move >0 and move < 10:
                if spaceIsFree(move):
                    run= False
                    insertLetter('X',move)
                else:
                    print(' Sorry, this space is occupied')
            else:
                print('PLease enter a valid number between 1-9')
        except:
            print('Please type a number!')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter==' ' and x!=0]#enumerate gives indices and values at same time
    move = 0

    for let in['O','X']:
        for i in possibleMoves:#here we check whether we can will or player will win
            boardCopy=board[:]
            boardCopy[i]=let
            if isWinner(boardCopy,let):
                move=i
                return move
    cornerOpen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerOpen.append(i)
    if len(cornerOpen)>0:
        move=selectRadom(cornerOpen)
        return move
    if 5 in possibleMoves:
        move=5
        return move
    edgesOpen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRadom(edgesOpen)
        return move
    return move

def selectRadom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def main():
    print(' WELCOME TO TIC-TAC-TOE')
    printBoard(board)
    while not(isBoardFull(board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O won this time')
            break
        if not(isWinner(board,'X')):
            move=compMove()
            if move == 0:
                print('Tie Game')
            else:
                insertLetter('O',move)
                print('Computer placed an O in position',move,':')
                printBoard(board)
        else:
            print('X won this time, GOOD_JOB!')
            break
        if isBoardFull(board):
            print('Tie Game')

while True:
  board = [' ' for x in range(10)]
  input("Reset Game")
  main()
