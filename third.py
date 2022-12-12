from tkinter import *
from random import *
from tkinter import messagebox as msgb

def game(): 
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'light slate blue'
            field[row][col]['command'] = lambda row=row, col=col: click(row,col)
    global begin
    begin = True
    global moveCount
    moveCount = 0

def click(row, col):
    if begin and field[row][col]['text'] == ' ':
        field[row][col]['text'] = '+'
        global moveCount
        moveCount += 1
        checkViktory('+')
        if begin and moveCount < 5:
            botMove()
            checkViktory('O')
        else:
            gameOver = Tk()
            gameOver.title('Игра окончена!')
            massage = Label(gameOver, text='Ничья!', 
                            font=('Segoe Script', 15, 'bold'))
            gameOver.geometry('+700+350')
            massage.config(bd=20, bg='cyan4')
            massage.pack()
            gameOver.mainloop() 

def checkViktory(char_):
    for i in range(3):
        check_line(field[i][0], field[i][1], field[i][2], char_)
        check_line(field[0][i], field[1][i], field[2][i], char_)
    check_line(field[0][0], field[1][1], field[2][2], char_)
    check_line(field[2][0], field[1][1], field[0][2], char_)

def check_line(field1, field2, field3, char_):
    if (field1['text'] == char_) and (field2['text'] == char_) and (field3['text'] == char_):
        field1['background'] = 'cyan4'
        field2['background'] = 'cyan4'
        field3['background'] = 'cyan4'
        global begin
        begin = False 
        winGame = Tk()
        winGame.title('Победа!')
        if char_ == '+':
            winMassage = Label(winGame, text='Поздравляю! Вы победили!!!', 
                            font=('Segoe Script', 15, 'bold'))
            winGame.geometry('+600+300')
        else:
            winMassage = Label(winGame, text='Победил бот!', 
                            font=('Segoe Script', 15, 'bold'))
            winGame.geometry('+670+330')
        winMassage.config(bd=20, bg='cyan4')
        winMassage.pack()
        winGame.mainloop() 
        

def victoryCon(field1, field2, field3,char_):
    res = False
    if field1['text'] == char_ and field2['text'] == char_ and field3['text'] == ' ':
        field3['text'] = 'O'
        res = True
    if field1['text'] == char_ and field2['text'] == ' ' and field3['text'] == char_:
        field2['text'] = 'O'
        res = True
    if field1['text'] == ' ' and field2['text'] == char_ and field3['text'] == char_:
        field1['text'] = 'O'
        res = True
    return res

def botMove():
    for i in range(3):
        if victoryCon(field[i][0], field[i][1], field[i][2], 'O'):
            return
        if victoryCon(field[0][i], field[1][i], field[2][i], 'O'):
            return
    if victoryCon(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if victoryCon(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for i in range(3):
        if victoryCon(field[i][0], field[i][1], field[i][2], '+'):
            return
        if victoryCon(field[0][i], field[1][i], field[2][i], '+'):
            return
    if victoryCon(field[0][0], field[1][1], field[2][2], '+'):
        return
    if victoryCon(field[2][0], field[1][1], field[0][2], '+'):
        return
    help_ = True
    while help_ == True:
        row = randint(0, 2)
        col = randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            help_ = False

window = Tk()
window.title('Игра "Крестики-нолики"')
window.geometry('+600+200')
begin = True
field = []
crossCount = 0

for row in range(3):
    line = []
    for col in range(3):
        buttonsField = Button(window, text=' ', width=6, height=3, 
                        font=('Arial', 20, 'bold'),
                        background='lime green')
        buttonsField.grid(row=row, column=col)
        line.append(buttonsField)
    field.append(line)
    
newGameButton = Button(window, text='Новая игра', width=18, height=2, 
                    font=('Segoe Script', 15, 'bold'), background='dodgerblue4', command=game)
newGameButton.grid(row=3, column=0, columnspan = 3, sticky=NSEW)
game()
window.mainloop()