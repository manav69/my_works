from tkinter import *
import random
window = Tk()
def reset():
    def insertLetter(letter, pos):
        board[pos] = letter

    def spaceIsFree(pos):
        return board[pos] == ' '

    def isWinner(bo, le):
        return (bo[7] == le and bo[8] == le and bo[9] == le) or \
               (bo[4] == le and bo[5] == le and bo[6] == le) or \
               (bo[1] == le and bo[2] == le and bo[3] == le) or \
               (bo[1] == le and bo[4] == le and bo[7] == le) or \
               (bo[2] == le and bo[5] == le and bo[8] == le) or \
               (bo[3] == le and bo[6] == le and bo[9] == le) or \
               (bo[1] == le and bo[5] == le and bo[9] == le) or \
               (bo[3] == le and bo[5] == le and bo[7] == le)

    def playerMove(move):

        if spaceIsFree(move):
            insertLetter('X', move)
            move = compMove()
            if move > 0: insertLetter('O', move)
            if move == 1:
                b11()
            elif move == 2:
                b22()
            elif move == 3:
                b33()
            elif move == 4:
                b44()
            elif move == 5:
                b55()
            elif move == 6:
                b66()
            elif move == 7:
                b77()
            elif move == 8:
                b88()
            elif move == 9:
                b99()
        if isWinner(board, 'X'):
            label1.destroy()
            Label(window, text="HURRAY!!! YOU WON.", width=40, height=3, bg=color, fg='black', font=100).grid(row=2,
                                                                                                             column=0)
        elif isWinner(board, 'O'):
            label1.destroy()
            Label(window, text="SORRY!!! YOU LOST.", width=40, height=3, bg=color, fg='black', font=100).grid(row=2,
                                                                                                             column=0)

        elif isBoardFull(board):
            label1.destroy()
            Label(window, text="IT\'S A TIE!!!", width=40, height=3, bg=color, fg='black', font=100).grid(row=2,
                                                                                                         column=0)

    def compMove():
        possibleMoves = [x for x, letter in enumerate(board) if
                         letter == ' ' and x != 0]  # enumerate gives indices and values at same time
        move = 0

        for let in ['O', 'X']:
            for i in possibleMoves:  # here we check whether we can will or player will win
                boardCopy = board[:]
                boardCopy[i] = let
                if isWinner(boardCopy, let):
                    move = i
                    return move
        cornerOpen = []
        for i in possibleMoves:
            if i in [1, 3, 7, 9]:
                cornerOpen.append(i)
        if len(cornerOpen) > 0:
            move = selectRadom(cornerOpen)
            return move
        if 5 in possibleMoves:
            move = 5
            return move
        edgesOpen = []
        for i in possibleMoves:
            if i in [2, 4, 6, 8]:
                edgesOpen.append(i)
        if len(edgesOpen) > 0:
            move = selectRadom(edgesOpen)
            return move
        return move

    def selectRadom(li):
        import random
        ln = len(li)
        r = random.randrange(0, ln)
        return li[r]

    def isBoardFull(board):
        if board.count(' ') > 1:
            return False
        else:
            return True

    def b1():
        button1.destroy()
        Button(frame1, text="X", fg='white', bg='black', width=15, height=6).grid(row=0, column=0)
        playerMove(1)

    def b2():
        button2.destroy()
        Button(frame1, text="X", fg='white', bg='black', width=15, height=6).grid(row=0, column=1)
        playerMove(2)

    def b3():
        button3.destroy()
        Button(frame1, text="X", fg='white', bg='black', width=15, height=6).grid(row=0, column=2)
        playerMove(3)

    def b4():
        button4.destroy()
        Button(frame1, text="X", fg='white', bg='black', width=15, height=6).grid(row=1, column=0)
        playerMove(4)

    def b5():
        button5.destroy()
        Button(frame1, text="X", fg='white', bg='black', width=15, height=6).grid(row=1, column=1)
        playerMove(5)

    def b6():
        button6.destroy()
        Button(frame1, text="X", fg='white', bg='black', width=15, height=6).grid(row=1, column=2)
        playerMove(6)

    def b7():
        button7.destroy()
        Button(frame1, text="X", fg='white', bg='black', width=15, height=6).grid(row=2, column=0)
        playerMove(7)

    def b8():
        button8.destroy()
        Button(frame1, text="X", fg='white', bg='black', width=15, height=6).grid(row=2, column=1)
        playerMove(8)

    def b9():
        button9.destroy()
        Button(frame1, text="X", fg='white', bg='black', width=15, height=6).grid(row=2, column=2)
        playerMove(9)

    def b11():
        button1.destroy()
        Button(frame1, text="O", fg='white', bg='black', width=15, height=6).grid(row=0, column=0)

    def b22():
        button2.destroy()
        Button(frame1, text="O", fg='white', bg='black', width=15, height=6).grid(row=0, column=1)

    def b33():
        button3.destroy()
        Button(frame1, text="O", fg='white', bg='black', width=15, height=6).grid(row=0, column=2)

    def b44():
        button4.destroy()
        Button(frame1, text="O", fg='white', bg='black', width=15, height=6).grid(row=1, column=0)

    def b55():
        button5.destroy()
        Button(frame1, text="O", fg='white', bg='black', width=15, height=6).grid(row=1, column=1)

    def b66():
        button6.destroy()
        Button(frame1, text="O", fg='white', bg='black', width=15, height=6).grid(row=1, column=2)

    def b77():
        button7.destroy()
        Button(frame1, text="O", fg='white', bg='black', width=15, height=6).grid(row=2, column=0)

    def b88():
        button8.destroy()
        Button(frame1, text="O", fg='white', bg='black', width=15, height=6).grid(row=2, column=1)

    def b99():
        button9.destroy()
        Button(frame1, text="O", fg='white', bg='black', width=15, height=6).grid(row=2, column=2)

    window.title("TIC_TAC_TOE")
    window.geometry("400x400")
    frame1 = Frame(window)
    quit_button = Button(window, text="Exit", command=window.quit, width=25, height=2, bg='Red')
    button1 = Button(frame1, text='1', command=b1, width=15, height=6)
    button2 = Button(frame1, text='2', command=b2, width=15, height=6)
    button3 = Button(frame1, text='3', command=b3, width=15, height=6)
    button4 = Button(frame1, text='4', command=b4, width=15, height=6)
    button5 = Button(frame1, text='5', command=b5, width=15, height=6)
    button6 = Button(frame1, text='6', command=b6, width=15, height=6)
    button7 = Button(frame1, text='7', command=b7, width=15, height=6)
    button8 = Button(frame1, text='8', command=b8, width=15, height=6)
    button9 = Button(frame1, text='9', command=b9, width=15, height=6)
    frame1.grid(row=0, column=0, sticky=W)
    button1.grid(row=0, column=0, sticky=W)
    button2.grid(row=0, column=1, sticky=W)
    button3.grid(row=0, column=2, sticky=W)
    button4.grid(row=1, column=0, sticky=W)
    button5.grid(row=1, column=1, sticky=W)
    button6.grid(row=1, column=2, sticky=W)
    button7.grid(row=2, column=0, sticky=W)
    button8.grid(row=2, column=1, sticky=W)
    button9.grid(row=2, column=2, sticky=W)
    quit_button.grid(row=3, column=0, sticky=E)
    color = random.choice(['violet', 'yellow', 'green', 'orange', 'pink','purple'])
    label1 = Label(window, text="WELCOME TO TIC-TAC-TOE!!!", width=40, height=3, bg=color, fg='black', font=100)
    label1.grid(row=2, column=0)
    board = [' ' for x in range(10)]
    Button(window, text='RESET', command=reset,bg=color,width=25,height=2).grid(row=3, column=0,sticky=W)

reset()
window.mainloop()
