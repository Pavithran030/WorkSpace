from tkinter import*
import random
tab=Tk()
tab.title('GAME')
tab.geometry('700x700')
tab.resizable(0,0)
tab.config(bg='#b3d5e6')
t1=None
t2=None
t3=None
t4=None
pw=0
cw=0
da=0
score1=IntVar()
score2=IntVar()
score3=IntVar()
def score():
    Label(tab,width=15,text='Computer won',font=('poppins',10),bg='#b3d5e6').place(x=190,y=590)
    Label(tab,width=10,textvariable=score1,font=('poppins',10)).place(x=350,y=590)
    Label(tab,width=10,text='Player won',font=('poppins',10),bg='#b3d5e6').place(x=200,y=620)
    Label(tab,width=10,textvariable=score2,font=('poppins',10)).place(x=350,y=620)
    Label(tab,width=10,text='Tie',font=('poppins',10),bg='#b3d5e6').place(x=200,y=650)
    Label(tab,width=10,textvariable=score3,font=('poppins',10)).place(x=350,y=650)
c=StringVar()
p=StringVar()
def st():
    Button(tab,width=8,text='Rock',font=('Copperplate Gothic Bold',15),bg='pink',relief='ridge',command=lambda:game("rock")).place(x=120,y=200)
    Button(tab,width=8,text='Paper',font=('Copperplate Gothic Bold',15),bg='pink',relief='ridge',command=lambda:game("paper")).place(x=290,y=200)
    Button(tab,width=8,text='Scissor',font=('Copperplate Gothic Bold',15),bg='pink',relief='ridge',command=lambda:game("scissor")).place(x=450,y=200)
    Button(tab,width=10,text='Score',font=('Copperplate Gothic Bold',15),bg='#83f2a8',relief='sunken',command=score).place(x=280,y=530)
def ag1():
    global t1,t2
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
    t2=Label(tab,text='If you want to play again....',font=('poppins',15,'bold'),bg='#b3d5e6')
    t2.place(x=230,y=400)
def again():
    global t3,t4
    tagain()
    t3=Button(tab,width=5,text='Yes',font=('Copperplate Gothic Bold',15),bg='green',relief='sunken',command=ag1)
    t3.place(x=220,y=450)
    t4=Button(tab,width=5,text='No',font=('Copperplate Gothic Bold',15),bg='red',relief='sunken',command=ag2)
    t4.place(x=420,y=450)
def cwon():
    global t1,m1,m2,cw
    m1=Label(tab,text=f'Player choice      : {p}',font=('Algerian',20),bg='#b3d5e6',fg='#8657bd')
    m1.place(x=180,y=260)
    m2=Label(tab,text=f'Computer choice : {c}',font=('Algerian',20),bg='#b3d5e6',fg='#8657bd')
    m2.place(x=180,y=300)
    t1=Label(tab,text='Computer won the Match',font=('FZShuTi',25),bg='#b3d5e6',fg='brown')
    t1.place(x=180,y=350)
    cw+=1
    score1.set(cw)
    again()
def pwon():
    global t1,m1,m2,pw
    m1=Label(tab,text=f'Player choice     : {p}',font=('Algerian',20),bg='#b3d5e6',fg='#8657bd')
    m1.place(x=180,y=260)
    m2=Label(tab,text=f'Computer choice : {c}',font=('Algerian',20),bg='#b3d5e6',fg='#8657bd')
    m2.place(x=180,y=300)
    t1=Label(tab,text='Player won the Match',font=('FZShuTi',25),bg='#b3d5e6',fg='brown')
    t1.place(x=180,y=350)
    pw+=1
    score2.set(pw)
    again()
def game(player):
    gam=["rock","paper","scissor"]
    choice=random.choice(gam)
    global c,p
    c=choice
    p=player
    if player not in choice:
        if choice in player:
            da+=1
            score3.set(da)
            Label(tab,text='Tie').place(x=200,y=250)
            Label(tab,text='Butter luck next time....').place(x=200,y=290)
            again()
        elif player=="rock":
            if choice=="paper":
                cwon()              
            if choice=="scissor":
                pwon()      
        elif player=="scissor":
            if choice=="rock":
                cwon()     
            if choice=="paper":
                pwon()  
        elif player=="paper":
            if choice=="rock":
                pwon()    
            if choice=="scissor":
                cwon()    
Label(tab,text='Lets play a Rock,Paper and Scissor Game',font=('Copperplate Gothic Bold',20),bg='#8db0ab').place(x=30,y=20)
Label(tab,text='click start button to begin the game',font=('BankGothic Md BT',20)).place(x=30,y=100)
Button(tab,width=10,text='Start',font=('Copperplate Gothic Bold',15),bg='#83f2a8',relief='sunken',command=st).place(x=275,y=150)
tab.mainloop()