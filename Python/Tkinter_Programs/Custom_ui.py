# import tkinter as tk

# root = tk.Tk()
# entry = tk.Entry(root)
# entry.pack()

# # Create a variable to hold the current number
# current_number = None

# def reduce_number():
#     global current_number
#     try:
#         # Get the number from the entry if it's the first time
#         if current_number is None:
#             current_number = int(entry.get())
#         else:
#             # Reduce the number
#             current_number -= 1
#         # Update the entry with the current number
#         entry.delete(0, 'end')
#         entry.insert(0, str(current_number))
#         if current_number==0:
#             root.quit()
#     except ValueError:
#         print("Please enter a valid integer.")

# button = tk.Button(root, text="Reduce", command=reduce_number)
# button.pack()

# root.mainloop()

# import tkinter as tk
# import random

# def play_game(player_choice):
#     computer_choice = random.choice(['rock', 'paper', 'scissors'])
#     result_text.set("Computer chooses: " + computer_choice)

#     if player_choice == computer_choice:
#         result_text.set("It's a tie!")
#     elif (player_choice == 'rock' and computer_choice == 'scissors') or \
#          (player_choice == 'paper' and computer_choice == 'rock') or \
#          (player_choice == 'scissors' and computer_choice == 'paper'):
#         result_text.set("You win!")
#     else:
#         result_text.set("Computer wins!")

# # Create main window
# root = tk.Tk()
# root.title("Rock, Paper, Scissors")

# # Create buttons
# rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_game('rock'))
# rock_button.pack(pady=5)
# paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_game('paper'))
# paper_button.pack(pady=5)
# scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_game('scissors'))
# scissors_button.pack(pady=5)

# # Create result label
# result_text = tk.StringVar()
# result_label = tk.Label(root, textvariable=result_text)
# result_label.pack(pady=10)

# # Run the main event loop
# root.mainloop()






import tkinter as tk
import random

def play_round(player_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(player_choice, computer_choice)
    display_result(player_choice, computer_choice, result)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(player_choice, computer_choice, result):
    round_results.append((player_choice, computer_choice, result))
    round_label.config(text=f"Player: {player_choice}\nComputer: {computer_choice}\nResult: {result}")

def show_winner():
    player_score = sum(1 for result in round_results if result[2] == "You win!")
    computer_score = sum(1 for result in round_results if result[2] == "Computer wins!")

    if player_score > computer_score:
        winner_label.config(text="You win the game!")
    elif player_score < computer_score:
        winner_label.config(text="Computer wins the game!")
    else:
        winner_label.config(text="It's a tie!")

def start_game():
    global round_results
    round_results = []
    num_rounds = int(num_rounds_entry.get())
    for _ in range(num_rounds):
        play_round(random.choice(["Rock", "Paper", "Scissors"]))
    show_winner()

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create frames
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

output_frame = tk.Frame(root)
output_frame.pack(pady=10)

# Create widgets
num_rounds_label = tk.Label(input_frame, text="Enter number of rounds:")
num_rounds_label.grid(row=0, column=0)

num_rounds_entry = tk.Entry(input_frame)
num_rounds_entry.grid(row=0, column=1)

start_button = tk.Button(input_frame, text="Start Game", command=start_game)
start_button.grid(row=1, columnspan=2)

round_label = tk.Label(output_frame, text="")
round_label.pack()

winner_label = tk.Label(output_frame, text="")
winner_label.pack()

# Run the main event loop
root.mainloop()

