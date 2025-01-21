'''import random
print("Let's Play a simple rock,paper,scissor game using python programming......")
def cwon():
    print("Computer Won!!!")
def pwon():
    print("Player Won!!!")
while True:
    game=["rock","paper","scissor"]
    choice =random.choice(game)
    player=None
    while player not in game:
        player=input("rock,paper,scissor :? ")
        if choice==player:
            print("Tie!!")
            print("Better luck next time....")
        elif player=="rock":
            if choice=="paper":
                print("Computer : ",choice)
                print("player : ",player)
                cwon()
            if choice=="scissor":
                print("Computer : ",choice)
                print("player : ",player)
                pwon()
        elif player=="scissor":
            if choice=="rock":
                print("Computer : ",choice)
                print("player : ",player)
                cwon()
            if choice=="paper":
                print("Computer : ",choice)
                print("player : ",player)
                pwon()
        elif player=="paper":
            if choice=="rock":
                print("Computer : ",choice)
                print("player : ",player)
                pwon()
            if choice=="scissor":
                print("Computer : ",choice)
                print("player : ",player)
                cwon()
    player1=input("Enter (yse/no) :? ")
    if player1 not in "yes":
        break
print("Bye !!!")'''

from customtkinter import *
import random

tab = CustomTk()
tab.title('GAME')
tab.geometry('700x700')
tab.resizable(0, 0)
tab.config(bg='#b3d5e6')

t1 = None
t2 = None
t3 = None
t4 = None
pw = 0
cw = 0
c = StringVar()
p = StringVar()


def st():
    Button(tab, width=5, text='Rock', font=('Copperplate Gothic Bold', 15), bg='pink', relief='raised',
           command=lambda: game("rock")).place(x=120, y=200)
    Button(tab, width=5, text='Paper', font=('Copperplate Gothic Bold', 15), bg='pink', relief='ridge',
           command=lambda: game("paper")).place(x=290, y=200)
    Button(tab, width=8, text='Scissor', font=('Copperplate Gothic Bold', 15), bg='pink', relief='groove',
           command=lambda: game("scissor")).place(x=450, y=200)


def ag1():
    global t1, t2
    t1.destroy()
    t2.destroy()
    t3.destroy()
    t4.destroy()
    m1.destroy()
    m2.destroy()


def ag2():
    tab.quit()


def tagain():
    global t2
    t2 = Label(tab, text='If you want to play again....', font=('poppins', 15, 'bold'), bg='#b3d5e6')
    t2.place(x=230, y=400)


def again():
    global t3, t4
    tagain()
    t3 = Button(tab, width=5, text='Yes', font=('Copperplate Gothic Bold', 15), bg='green', relief='sunken',
                command=ag1)
    t3.place(x=220, y=450)
    t4 = Button(tab, width=5, text='No', font=('Copperplate Gothic Bold', 15), bg='red', relief='sunken',
                command=ag2)
    t4.place(x=420, y=450)


def cwon():
    global t1, m1, m2
    m1 = Label(tab, text=f'Player choice      : {p}', font=('Algerian', 20), bg='#b3d5e6', fg='#627027')
    m1.place(x=180, y=260)
    m2 = Label(tab, text=f'Computer choice : {c}', font=('Algerian', 20), bg='#b3d5e6', fg='#627027')
    m2.place(x=180, y=300)
    t1 = Label(tab, text='Computer won the match', font=('Vineta BT', 15), bg='#b3d5e6', fg='brown')
    t1.place(x=180, y=350)
    again()


def pwon():
    global t1, m1, m2
    m1 = Label(tab, text=f'Player choice     : {p}', font=('Algerian', 20), bg='#b3d5e6', fg='#627027')
    m1.place(x=180, y=260)
    m2 = Label(tab, text=f'Computer choice : {c}', font=('Algerian', 20), bg='#b3d5e6', fg='#627027')
    m2.place(x=180, y=300)
    t1 = Label(tab, text='Player won the match', font=('Vineta BT', 15), bg='#b3d5e6', fg='brown')
    t1.place(x=180, y=350)
    again()


def game(player):
    gam = ["rock", "paper", "scissor"]
    choice = random.choice(gam)
    global c, p
    c = choice
    p = player
    if player not in choice:
        if choice in player:
            Label(tab, text='Tie').place(x=200, y=250)
            Label(tab, text='Butter luck next time....').place(x=200, y=290)
            again()
        elif player == "rock":
            if choice == "paper":
                cwon()
            if choice == "scissor":
                pwon()
        elif player == "scissor":
            if choice == "rock":
                cwon()
            if choice == "paper":
                pwon()
        elif player == "paper":
            if choice == "rock":
                pwon()
            if choice == "scissor":
                cwon()


Label(tab, text='Lets play a Rock,Paper and Scissor Game', font=('Copperplate Gothic Bold', 20), bg='#8db0ab').place(
    x=30, y=20)
Label(tab, text='click start button to begin the game', font=('BankGothic Md BT', 20)).place(x=30, y=100)
Button(tab, width=10, text='Start', font=('Copperplate Gothic Bold', 15), bg='#83f2a8', relief='sunken',
       command=st).place(x=250, y=150)

tab.mainloop()
