import tkinter
from customtkinter import*
import random


log=CTk()

log.geometry("480x460")

log.title("Game")

player = "X"
a=''
p1=0
p2=0
def game(s1,s2):
    log.destroy()
    while True:
        t=CTk()
        t.geometry("480x460")
        t.title("tic tac toe")
    
        

        player = "X"
        board = [
        ["","",""],
        ["","",""],
        ["","",""],
        ]

        def new_game():
            t.destroy()
    
        def stop_game():
            global a
            a="stop"
        fr1= CTkFrame(t, width=300, height=440, corner_radius=20)
        fr1.place(relx=0.5, rely=0.5,anchor=CENTER)
        msg=CTkLabel(fr1,text=f"{player} turn",font=("Arial Black",20))
        msg.place(x=120, y=10)
        reset=CTkButton(fr1,text="restart",fg_color='#06a603',hover_color="#037d01",command=new_game,font=("Arial Black",15),width=76)
        reset.place(x=110,y=45)
        fr2= CTkFrame(t, width=230,height=250,border_color="black",border_width=4)
        fr2.place(relx=0.5, rely=0.5,anchor=CENTER)
        stop=CTkButton(fr1,text="Quit",fg_color='#06a603',hover_color="#037d01",command=stop_game,font=("Arial Black",15),width=76)
        stop.place(x=110,y=350)       
        sc1=CTkLabel(fr1,text=f"{s1}  \n{s2}  ",font=("Arial Black",13))
        sc1.place(x=30, y=390)
        sc2=CTkLabel(fr1,text=f"( ' X ')  :   {p1}\n( ' O ')  :   {p2}",font=("Arial Black",14))
        sc2.place(x=140, y=390)
        if a=="stop":
            break 
        buttons = []
        for row in range(3):
            button_row = []
            for col in range(3): 
                button = CTkButton(
                fr2,
                text = f"{board[row][col]}",
                width = 76,height=76,
                fg_color='#06a603',
                hover_color="#037d01",
                command = lambda row=row, col=col: 
                    update_board(board, row, col) 
            ) 
                button.grid(
                row=row, column=col,
                padx=2,pady=3
            ) 
                button_row.append(button)
            buttons.append(button_row)
        def update_board(board,i,j):
    
            global player 
            if board[i][j] == '':
                board[i][j] = player 
                buttons[i][j].configure(text=player) 

                if check_winner(player) is True:
                    global p1,p2
                    if player=="X" or player=="x":
                        p1+=1
                    elif player=="O" or player=="o":
                        p2+=1
                    msg.configure(text = f"{player} won") 
                    return
            
        
                player = "O" if player == "X" else "X"
                msg.configure(text=f"{player} turn") 
            
                if empty_spaces() is False:
                    msg.configure(text=f" tie ") 

        def empty_spaces():

            spaces = 9

            for i in range(3):
                for j in range(3):
                    if board[i][j]!= "":
                        spaces -= 1

            if spaces == 0:
                return False
            else:
                return True     

        def check_winner(player):
            for row in range(3):
                if (
                    board[row][0] == board[row][1] == board[row][2] == player
                    and board[row][0] != ""
                ):
                    return True

            for col in range(3):
                if (
                    board[0][col] == board[1][col] == board[2][col] == player
                    and board[0][col] != ""
                ):
                    return True

            if (
                board[0][0] == board[1][1] == board[2][2] == player
                and board[0][0] != ""
            ): 
                return True

            if (
                board[0][2] == board[1][1] == board[2][0] == player
                and board[0][2] != ""
            ):
                return True
            else:
                return False 
        t.mainloop()
def start():
    s1=n1.get()
    s2=n2.get()
    if s1!="" and s2!="":
        game(s1,s2)
    else:
        l3=CTkLabel(f1, text='Give players Name',font=("Arial Black",13) ,fg_color='#161716',corner_radius=8)
        l3.place(x=65, y=280)


f1= CTkFrame(log, width=300, height=400, corner_radius=20)
f1.place(relx=0.5, rely=0.5,anchor=tkinter.CENTER)
 
 
l2=CTkLabel(f1, text='tic tac toe',font=("Arial Black",20) ,fg_color='transparent')
l2.place(x=95, y=10)


nl=CTkLabel(f1, text='Player1 : ',font=("Arial Black",13) ,fg_color='transparent')
nl.place(x=50,y=60)
n1=CTkEntry(f1,placeholder_text='Player1 Name : ',font=("Arial Black",11) ,width=200)
n1.place(x=50,y=90)


nl=CTkLabel(f1, text='Player2 : ',font=("Arial Black",13) ,fg_color='transparent')
nl.place(x=50,y=130)
n2=CTkEntry(f1,placeholder_text='Player2 Name : ',font=("Arial Black",11) ,width=200,)
n2.place(x=50,y=160)


lgbut=CTkButton(f1, text='start game',command=start,font=("Arial Black",13) ,fg_color='#06a603',hover_color="#045201",width=200)
lgbut.place(x=50,y=210)

log.mainloop()