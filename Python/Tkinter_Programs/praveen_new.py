
# from customtkinter import *
# import random

# set_appearance_mode('dark') 
# set_default_color_theme('green')  

# app = CTk()
# app.title('Tic Tac Toe')
# app.geometry("480x460")

# # Initialize game state
# player = "X"
# board = [
#     ["","",""],
#     ["","",""],
#     ["","",""],
# ]

# # Create UI elements
# fr1= CTkFrame(app, width=300, height=400, corner_radius=20)
# fr1.place(relx=0.5, rely=0.5,anchor=CENTER)

# fr2= CTkFrame(fr1, width=230, height=230,border_color="black",border_width=4)
# fr2.place(relx=0.5, rely=0.5,anchor=CENTER)

# msg = CTkLabel(
#     fr1, 
#     text = f"{player} turn", 
#     font = ("Arial Black",20),
#     width = 100 
# ) 
# msg.place(x=100, y=10)

# buttons = []
# for row in range(3):
#     button_row = []
#     for col in range(3):
#         button = CTkButton(
#             fr2,
#             text = f"{board[row][col]}",
#             width = 76,height=76,
#             fg_color='#056301',
#             command = lambda row=row, col=col: 
#                 update_board(board, row, col) 
#         )
#         button.grid(
#             row=row, column=col,
#             padx=2,pady=3
#         ) 
#         button_row.append(button)
#     buttons.append(button_row)

# # Define game logic
# def update_board(board, i, j):
#     global player 

#     if board[i][j] == '':
#         board[i][j] = player 
#         buttons[i][j].configure(text=player) 

#         if check_win(player):
#             msg.configure(
#                 text = f"{player} won"
#             ) 
#             return
        
#         player = "O" if player == "X" else "X"
#         msg.configure(text=f"Player {player}") 

# def check_win(player): 
#     # ... your existing check_win code ...
#     pass
# def reset_game():
#     global player, board
#     player = "X"
#     board = [
#         ["","",""],
#         ["","",""],
#         ["","",""],
#     ]
#     for row in range(3):
#         for col in range(3):
#             buttons[row][col].configure(text=board[row][col])
#     msg.configure(text=f"{player} turn")

# # Create reset button
# reset_button = CTkButton(fr1, text="restart", fg_color='#056301', font=("Arial Black",15), command=reset_game)
# reset_button.place(x=90, y=40)

# app.mainloop()

from customtkinter import*
import random
a=''
while True:
    t=CTk()
    t.geometry("480x460")
    t.title("tic tac toe")
# players=['X','O']
# player=random.choice(players)

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

    fr1= CTkFrame(t, width=300, height=400, corner_radius=20)
    fr1.place(relx=0.5, rely=0.5,anchor=CENTER)

    msg=CTkLabel(fr1,text=f"{player} turn",font=("Arial Black",20))
    msg.place(x=120, y=10)

    reset=CTkButton(fr1,text="restart",command=new_game,font=("Arial Black",15))
    reset.place(x=90,y=40)

    fr2= CTkFrame(t, width=230, height=230,border_color="black",border_width=4)
    fr2.place(relx=0.5, rely=0.5,anchor=CENTER)

    stop=CTkButton(fr1,text="stop",command=stop_game,font=("Arial Black",15))
    stop.place(x=90,y=350)
   
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

            if check_winner(player):
                msg.configure(text = f"{player} won") 
                return
        
        
            player = "O" if player == "X" else "X"
            msg.configure(text=f"Player {player}") 
            

    def check_winner(player):
        for row in range(3):
            if (
                board[row][0] == board[row][1] == board[row][2] == player
                and board[row][0] != ""
            ):
                board[row][0].configure(bg="green")
                board[row][1].configure(bg="green")
                board[row][2].configure(bg="green")
            
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

        return False 







    t.mainloop()