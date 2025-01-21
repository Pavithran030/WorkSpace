from customtkinter import *

# Stylize the appearance [Optional] ~ Aesthetics
set_appearance_mode('dark') # By default, it's white
set_default_color_theme('green') # By default, it's blue

# Creating an App Object
app = CTk()
app.title('Tic Tac Toe') # Optional
app.geometry('400x400')

# Initialize the variables
player = "X"
board = [
    ["","",""],
    ["","",""],
    ["","",""],
]

# Initialize the buttons, for configuration later on
buttons = []
for row in range(3): # for each row
    button_row = []
    for col in range(3): # for each column
        button = CTkButton(
            app,
            text = f"{board[row][col]}",
            width = 125,
            height=100,
            command = lambda row=row, col=col: 
                update_board(board, row, col) # Handling the button clicks
        ) # Creates a button object
        button.grid(
            row=row, column=col,
            padx=4,pady=3
        ) # Design and Position the button
        button_row.append(button)
    buttons.append(button_row)

# Function to update board
def update_board(board, i, j):
    global player # Globalize the player variable

    # Checks if a player already exists on the board
    if board[i][j] == '':
        board[i][j] = player # Sets the board
        buttons[i][j].configure(text=player) # Sets the button

        if check_win(player):
            msg.configure(
                text = f"{player} won"
            ) # Change the label at the end
            return
        
        # Change the player
        player = "O" if player == "X" else "X"
        msg.configure(text=f"Player {player}") # Change player name each turn
        
# Function to check for a win
def check_win(player): 
    for row in range(3): # For every row (3)
        if (
            board[row][0] == board[row][1] == board[row][2] == player
            and board[row][0] != ""
        ):
            return True

    for col in range(3): # For every column (3)
        if (
            board[0][col] == board[1][col] == board[2][col] == player
            and board[0][col] != ""
        ):
            return True

    if (
        board[0][0] == board[1][1] == board[2][2] == player
        and board[0][0] != ""
    ): # For leading diagonal
        return True

    if (
        board[0][2] == board[1][1] == board[2][0] == player
        and board[0][2] != ""
    ): # For trailing diagonal
        return True

    return False # Returns a failed check

# Create a footer label
msg = CTkLabel(
    app, # Window to place the label
    text = f"Player {player}", # Text to be shown
    font = ("Poppins", 30), # Custom font [Optional]
    width = 100 # Style [Optional] ~ Aesthetics
) 
# Positioning below buttons
msg.grid(row=3,column=0,columnspan=3)

# Keep the below statement at the end [Recommended]
app.mainloop()