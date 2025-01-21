# # # # # # # # import turtle


# # # # # # # # def setup(x, y):
# # # # # # # #     turtle.setx(x)
# # # # # # # #     turtle.sety(y)
# # # # # # # #     print(x, y)


# # # # # # # # class Draw_Pikachu:

# # # # # # # #     def __init__(self):
# # # # # # # #         self.t = turtle.Turtle()
# # # # # # # #         t = self.t
# # # # # # # #         t.pensize(3)
# # # # # # # #         t.speed(9)
# # # # # # # #         t.ondrag(setup)

# # # # # # # #     def meme(self, x, y):
# # # # # # # #         self.t.penup()
# # # # # # # #         self.t.goto(x, y)
# # # # # # # #         self.t.pendown()

# # # # # # # #     def aankha1(self, x, y):
# # # # # # # #         self.meme(x, y)
# # # # # # # #         t = self.t
# # # # # # # #         t.seth(0)
# # # # # # # #         t.fillcolor('#333333')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.circle(22)
# # # # # # # #         t.end_fill()

# # # # # # # #         self.meme(x, y + 10)
# # # # # # # #         t.fillcolor('#000000')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.circle(10)
# # # # # # # #         t.end_fill()

# # # # # # # #         self.meme(x + 6, y + 22)
# # # # # # # #         t.fillcolor('#ffffff')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.circle(10)
# # # # # # # #         t.end_fill()

# # # # # # # #     def aankha2(self, x, y):
# # # # # # # #         self.meme(x, y)
# # # # # # # #         t = self.t
# # # # # # # #         t.seth(0)
# # # # # # # #         t.fillcolor('#333333')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.circle(22)
# # # # # # # #         t.end_fill()

# # # # # # # #         self.meme(x, y + 10)
# # # # # # # #         t.fillcolor('#000000')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.circle(10)
# # # # # # # #         t.end_fill()

# # # # # # # #         self.meme(x - 6, y + 22)
# # # # # # # #         t.fillcolor('#ffffff')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.circle(10)
# # # # # # # #         t.end_fill()

# # # # # # # #     def mukh(self, x, y):
# # # # # # # #         self.meme(x, y)
# # # # # # # #         t = self.t

# # # # # # # #         t.fillcolor('#88141D')
# # # # # # # #         t.begin_fill()
# # # # # # # #         #
# # # # # # # #         l1 = []
# # # # # # # #         l2 = []
# # # # # # # #         t.seth(190)
# # # # # # # #         a = 0.7
# # # # # # # #         for i in range(28):
# # # # # # # #             a += 0.1
# # # # # # # #             t.right(3)
# # # # # # # #             t.fd(a)
# # # # # # # #             l1.append(t.position())

# # # # # # # #         self.meme(x, y)

# # # # # # # #         t.seth(10)
# # # # # # # #         a = 0.7
# # # # # # # #         for i in range(28):
# # # # # # # #             a += 0.1
# # # # # # # #             t.left(3)
# # # # # # # #             t.fd(a)
# # # # # # # #             l2.append(t.position())

# # # # # # # #         #

# # # # # # # #         t.seth(10)
# # # # # # # #         t.circle(50, 15)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(-50, 15)

# # # # # # # #         t.circle(-50, 40)
# # # # # # # #         t.seth(233)
# # # # # # # #         t.circle(-50, 55)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(50, 12.1)
# # # # # # # #         t.end_fill()

# # # # # # # #         #
# # # # # # # #         self.meme(17, 54)
# # # # # # # #         t.fillcolor('#DD716F')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.seth(145)
# # # # # # # #         t.circle(40, 86)
# # # # # # # #         t.penup()
# # # # # # # #         for pos in reversed(l1[:20]):
# # # # # # # #             t.goto(pos[0], pos[1] + 1.5)
# # # # # # # #         for pos in l2[:20]:
# # # # # # # #             t.goto(pos[0], pos[1] + 1.5)
# # # # # # # #         t.pendown()
# # # # # # # #         t.end_fill()

# # # # # # # #         #
# # # # # # # #         self.meme(-17, 94)
# # # # # # # #         t.seth(8)
# # # # # # # #         t.fd(4)
# # # # # # # #         t.back(8)

# # # # # # # #     #
# # # # # # # #     def gaala1(self, x, y):
# # # # # # # #         turtle.tracer(False)
# # # # # # # #         t = self.t
# # # # # # # #         self.meme(x, y)
# # # # # # # #         t.seth(300)
# # # # # # # #         t.fillcolor('#DD4D28')
# # # # # # # #         t.begin_fill()
# # # # # # # #         a = 2.3
# # # # # # # #         for i in range(120):
# # # # # # # #             if 0 <= i < 30 or 60 <= i < 90:
# # # # # # # #                 a -= 0.05
# # # # # # # #                 t.lt(3)
# # # # # # # #                 t.fd(a)
# # # # # # # #             else:
# # # # # # # #                 a += 0.05
# # # # # # # #                 t.lt(3)
# # # # # # # #                 t.fd(a)
# # # # # # # #         t.end_fill()
# # # # # # # #         turtle.tracer(True)

# # # # # # # #     def gaala2(self, x, y):
# # # # # # # #         t = self.t
# # # # # # # #         turtle.tracer(False)
# # # # # # # #         self.meme(x, y)
# # # # # # # #         t.seth(60)
# # # # # # # #         t.fillcolor('#DD4D28')
# # # # # # # #         t.begin_fill()
# # # # # # # #         a = 2.3
# # # # # # # #         for i in range(120):
# # # # # # # #             if 0 <= i < 30 or 60 <= i < 90:
# # # # # # # #                 a -= 0.05
# # # # # # # #                 t.lt(3)
# # # # # # # #                 t.fd(a)
# # # # # # # #             else:
# # # # # # # #                 a += 0.05
# # # # # # # #                 t.lt(3)
# # # # # # # #                 t.fd(a)
# # # # # # # #         t.end_fill()
# # # # # # # #         turtle.tracer(True)

# # # # # # # #     def kaan1(self, x, y):
# # # # # # # #         t = self.t
# # # # # # # #         self.meme(x, y)
# # # # # # # #         t.fillcolor('#000000')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.seth(330)
# # # # # # # #         t.circle(100, 35)
# # # # # # # #         t.seth(219)
# # # # # # # #         t.circle(-300, 19)
# # # # # # # #         t.seth(110)
# # # # # # # #         t.circle(-30, 50)
# # # # # # # #         t.circle(-300, 10)
# # # # # # # #         t.end_fill()

# # # # # # # #     def kaan2(self, x, y):
# # # # # # # #         t = self.t
# # # # # # # #         self.meme(x, y)
# # # # # # # #         t.fillcolor('#000000')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.seth(300)
# # # # # # # #         t.circle(-100, 30)
# # # # # # # #         t.seth(35)
# # # # # # # #         t.circle(300, 15)
# # # # # # # #         t.circle(30, 50)
# # # # # # # #         t.seth(190)
# # # # # # # #         t.circle(300, 17)
# # # # # # # #         t.end_fill()

# # # # # # # #     def jiu(self):
# # # # # # # #         t = self.t

# # # # # # # #         t.fillcolor('#F6D02F')
# # # # # # # #         t.begin_fill()
# # # # # # # #         #
# # # # # # # #         t.penup()
# # # # # # # #         t.circle(130, 40)
# # # # # # # #         t.pendown()
# # # # # # # #         t.circle(100, 105)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(-100, 5)

# # # # # # # #         #
# # # # # # # #         t.seth(20)
# # # # # # # #         t.circle(300, 30)
# # # # # # # #         t.circle(30, 50)
# # # # # # # #         t.seth(190)
# # # # # # # #         t.circle(300, 36)

# # # # # # # #         #
# # # # # # # #         t.seth(150)
# # # # # # # #         t.circle(150, 70)

# # # # # # # #         #
# # # # # # # #         t.seth(200)
# # # # # # # #         t.circle(300, 40)
# # # # # # # #         t.circle(30, 50)
# # # # # # # #         t.seth(20)
# # # # # # # #         t.circle(300, 35)
# # # # # # # #         # print(t.pos())

# # # # # # # #         #
# # # # # # # #         t.seth(240)
# # # # # # # #         t.circle(105, 95)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(-105, 5)

# # # # # # # #         #
# # # # # # # #         t.seth(210)
# # # # # # # #         t.circle(500, 18)
# # # # # # # #         t.seth(200)
# # # # # # # #         t.fd(10)
# # # # # # # #         t.seth(280)
# # # # # # # #         t.fd(7)
# # # # # # # #         t.seth(210)
# # # # # # # #         t.fd(10)
# # # # # # # #         t.seth(300)
# # # # # # # #         t.circle(10, 80)
# # # # # # # #         t.seth(220)
# # # # # # # #         t.fd(10)
# # # # # # # #         t.seth(300)
# # # # # # # #         t.circle(10, 80)
# # # # # # # #         t.seth(240)
# # # # # # # #         t.fd(12)
# # # # # # # #         t.seth(0)
# # # # # # # #         t.fd(13)
# # # # # # # #         t.seth(240)
# # # # # # # #         t.circle(10, 70)
# # # # # # # #         t.seth(10)
# # # # # # # #         t.circle(10, 70)
# # # # # # # #         t.seth(10)
# # # # # # # #         t.circle(300, 18)

# # # # # # # #         t.seth(75)
# # # # # # # #         t.circle(500, 8)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(-500, 15)
# # # # # # # #         t.seth(250)
# # # # # # # #         t.circle(100, 65)

# # # # # # # #         #
# # # # # # # #         t.seth(320)
# # # # # # # #         t.circle(100, 5)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(-100, 5)
# # # # # # # #         t.seth(220)
# # # # # # # #         t.circle(200, 20)
# # # # # # # #         t.circle(20, 70)

# # # # # # # #         t.seth(60)
# # # # # # # #         t.circle(-100, 20)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(100, 20)
# # # # # # # #         t.seth(300)
# # # # # # # #         t.circle(10, 70)

# # # # # # # #         t.seth(60)
# # # # # # # #         t.circle(-100, 20)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(100, 20)
# # # # # # # #         t.seth(10)
# # # # # # # #         t.circle(100, 60)

# # # # # # # #         #
# # # # # # # #         t.seth(180)
# # # # # # # #         t.circle(-100, 10)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(100, 10)
# # # # # # # #         t.seth(5)
# # # # # # # #         t.circle(100, 10)
# # # # # # # #         t.circle(-100, 40)
# # # # # # # #         t.circle(100, 35)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(-100, 10)

# # # # # # # #         #
# # # # # # # #         t.seth(290)
# # # # # # # #         t.circle(100, 55)
# # # # # # # #         t.circle(10, 50)

# # # # # # # #         t.seth(120)
# # # # # # # #         t.circle(100, 20)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(-100, 20)

# # # # # # # #         t.seth(0)
# # # # # # # #         t.circle(10, 50)

# # # # # # # #         t.seth(110)
# # # # # # # #         t.circle(100, 20)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(-100, 20)

# # # # # # # #         t.seth(30)
# # # # # # # #         t.circle(20, 50)

# # # # # # # #         t.seth(100)
# # # # # # # #         t.circle(100, 40)

# # # # # # # #         #
# # # # # # # #         t.seth(200)
# # # # # # # #         t.circle(-100, 5)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(100, 5)
# # # # # # # #         t.left(30)
# # # # # # # #         t.circle(100, 75)
# # # # # # # #         t.right(15)
# # # # # # # #         t.circle(-300, 21)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(300, 3)

# # # # # # # #         #
# # # # # # # #         t.seth(43)
# # # # # # # #         t.circle(200, 60)

# # # # # # # #         t.right(10)
# # # # # # # #         t.fd(10)

# # # # # # # #         t.circle(5, 160)
# # # # # # # #         t.seth(90)
# # # # # # # #         t.circle(5, 160)
# # # # # # # #         t.seth(90)

# # # # # # # #         t.fd(10)
# # # # # # # #         t.seth(90)
# # # # # # # #         t.circle(5, 180)
# # # # # # # #         t.fd(10)

# # # # # # # #         t.left(180)
# # # # # # # #         t.left(20)
# # # # # # # #         t.fd(10)
# # # # # # # #         t.circle(5, 170)
# # # # # # # #         t.fd(10)
# # # # # # # #         t.seth(240)
# # # # # # # #         t.circle(50, 30)

# # # # # # # #         t.end_fill()
# # # # # # # #         self.meme(130, 125)
# # # # # # # #         t.seth(-20)
# # # # # # # #         t.fd(5)
# # # # # # # #         t.circle(-5, 160)
# # # # # # # #         t.fd(5)

# # # # # # # #         #
# # # # # # # #         self.meme(166, 130)
# # # # # # # #         t.seth(-90)
# # # # # # # #         t.fd(3)
# # # # # # # #         t.circle(-4, 180)
# # # # # # # #         t.fd(3)
# # # # # # # #         t.seth(-90)
# # # # # # # #         t.fd(3)
# # # # # # # #         t.circle(-4, 180)
# # # # # # # #         t.fd(3)

# # # # # # # #         #
# # # # # # # #         self.meme(168, 134)
# # # # # # # #         t.fillcolor('#F6D02F')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.seth(40)
# # # # # # # #         t.fd(200)
# # # # # # # #         t.seth(-80)
# # # # # # # #         t.fd(150)
# # # # # # # #         t.seth(210)
# # # # # # # #         t.fd(150)
# # # # # # # #         t.left(90)
# # # # # # # #         t.fd(100)
# # # # # # # #         t.right(95)
# # # # # # # #         t.fd(100)
# # # # # # # #         t.left(110)
# # # # # # # #         t.fd(70)
# # # # # # # #         t.right(110)
# # # # # # # #         t.fd(80)
# # # # # # # #         t.left(110)
# # # # # # # #         t.fd(30)
# # # # # # # #         t.right(110)
# # # # # # # #         t.fd(32)

# # # # # # # #         t.right(106)
# # # # # # # #         t.circle(100, 25)
# # # # # # # #         t.right(15)
# # # # # # # #         t.circle(-300, 2)
# # # # # # # #         ##############
# # # # # # # #         # print(t.pos())
# # # # # # # #         t.seth(30)
# # # # # # # #         t.fd(40)
# # # # # # # #         t.left(100)
# # # # # # # #         t.fd(70)
# # # # # # # #         t.right(100)
# # # # # # # #         t.fd(80)
# # # # # # # #         t.left(100)
# # # # # # # #         t.fd(46)
# # # # # # # #         t.seth(66)
# # # # # # # #         t.circle(200, 38)
# # # # # # # #         t.right(10)
# # # # # # # #         t.fd(10)
# # # # # # # #         t.end_fill()

# # # # # # # #         #
# # # # # # # #         t.fillcolor('#923E24')
# # # # # # # #         self.meme(126.82, -156.84)
# # # # # # # #         t.begin_fill()

# # # # # # # #         t.seth(30)
# # # # # # # #         t.fd(40)
# # # # # # # #         t.left(100)
# # # # # # # #         t.fd(40)
# # # # # # # #         t.pencolor('#923e24')
# # # # # # # #         t.seth(-30)
# # # # # # # #         t.fd(30)
# # # # # # # #         t.left(140)
# # # # # # # #         t.fd(20)
# # # # # # # #         t.right(150)
# # # # # # # #         t.fd(20)
# # # # # # # #         t.left(150)
# # # # # # # #         t.fd(20)
# # # # # # # #         t.right(150)
# # # # # # # #         t.fd(20)
# # # # # # # #         t.left(130)
# # # # # # # #         t.fd(18)
# # # # # # # #         t.pencolor('#000000')
# # # # # # # #         t.seth(-45)
# # # # # # # #         t.fd(67)
# # # # # # # #         t.right(110)
# # # # # # # #         t.fd(80)
# # # # # # # #         t.left(110)
# # # # # # # #         t.fd(30)
# # # # # # # #         t.right(110)
# # # # # # # #         t.fd(32)
# # # # # # # #         t.right(106)
# # # # # # # #         t.circle(100, 25)
# # # # # # # #         t.right(15)
# # # # # # # #         t.circle(-300, 2)
# # # # # # # #         t.end_fill()

# # # # # # # #         self.topi(-134.07, 147.81)
# # # # # # # #         self.mukh(-5, 25)
# # # # # # # #         self.gaala1(-126, 32)
# # # # # # # #         self.gaala2(107, 63)
# # # # # # # #         self.kaan1(-250, 100)
# # # # # # # #         self.kaan2(140, 270)
# # # # # # # #         self.aankha1(-85, 90)
# # # # # # # #         self.aankha2(50, 110)
# # # # # # # #         t.hideturtle()

# # # # # # # #     def topi(self, x, y):
# # # # # # # #         self.meme(x, y)
# # # # # # # #         t = self.t
# # # # # # # #         t.fillcolor('#CD0000')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.seth(200)
# # # # # # # #         t.circle(400, 7)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(-400, 30)
# # # # # # # #         t.circle(30, 60)
# # # # # # # #         t.fd(50)
# # # # # # # #         t.circle(30, 45)
# # # # # # # #         t.fd(60)
# # # # # # # #         t.left(5)
# # # # # # # #         t.circle(30, 70)
# # # # # # # #         t.right(20)
# # # # # # # #         t.circle(200, 70)
# # # # # # # #         t.circle(30, 60)
# # # # # # # #         t.fd(70)
# # # # # # # #         # print(t.pos())
# # # # # # # #         t.right(35)
# # # # # # # #         t.fd(50)
# # # # # # # #         t.circle(8, 100)
# # # # # # # #         t.end_fill()
# # # # # # # #         self.meme(-168.47, 185.52)
# # # # # # # #         t.seth(36)
# # # # # # # #         t.circle(-270, 54)
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(270, 27)
# # # # # # # #         t.circle(-80, 98)

# # # # # # # #         t.fillcolor('#444444')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.left(180)
# # # # # # # #         t.circle(80, 197)
# # # # # # # #         t.left(58)
# # # # # # # #         t.circle(200, 45)
# # # # # # # #         t.end_fill()

# # # # # # # #         self.meme(-58, 270)
# # # # # # # #         t.pencolor('#228B22')
# # # # # # # #         t.dot(35)

# # # # # # # #         self.meme(-30, 280)
# # # # # # # #         t.fillcolor('#228B22')
# # # # # # # #         t.begin_fill()
# # # # # # # #         t.seth(100)
# # # # # # # #         t.circle(30, 180)
# # # # # # # #         t.seth(190)
# # # # # # # #         t.fd(15)
# # # # # # # #         t.seth(100)
# # # # # # # #         t.circle(-45, 180)
# # # # # # # #         t.right(90)
# # # # # # # #         t.fd(15)
# # # # # # # #         t.end_fill()
# # # # # # # #         t.pencolor('#000000')

# # # # # # # #     def start(self):
# # # # # # # #         self.jiu()


# # # # # # # # def main():
# # # # # # # #     print('Painting the Cartoon... ')
# # # # # # # #     turtle.screensize(800, 600)
# # # # # # # #     turtle.title('Cartoon')
# # # # # # # #     drawing = Draw_Pikachu()
# # # # # # # #     drawing.start()
# # # # # # # #     turtle.mainloop()


# # # # # # # # if __name__ == '__main__':
# # # # # # # #     main()

# # # # # # # import turtle

# # # # # # # # Set up the screen
# # # # # # # screen = turtle.Screen()
# # # # # # # t = turtle.Turtle()
# # # # # # # t.speed(0)  # Fastest drawing speed

# # # # # # # # Draw the orange rectangle
# # # # # # # t.penup()
# # # # # # # t.goto(-400, 250)
# # # # # # # t.pendown()
# # # # # # # t.color("orange")
# # # # # # # t.begin_fill()
# # # # # # # for _ in range(2):
# # # # # # #     t.forward(800)
# # # # # # #     t.right(90)
# # # # # # #     t.forward(167)
# # # # # # #     t.right(90)
# # # # # # # t.end_fill()

# # # # # # # # Draw the white rectangle
# # # # # # # t.left(90)
# # # # # # # t.forward(167)

# # # # # # # # Draw the green rectangle
# # # # # # # t.color("green")
# # # # # # # t.begin_fill()
# # # # # # # for _ in range(2):
# # # # # # #     t.forward(167)
# # # # # # #     t.left(90)
# # # # # # #     t.forward(800)
# # # # # # #     t.left(90)
# # # # # # # t.end_fill()

# # # # # # # # Draw the big blue circle
# # # # # # # t.penup()
# # # # # # # t.goto(70, 0)
# # # # # # # t.pendown()
# # # # # # # t.color("navy")
# # # # # # # t.begin_fill()
# # # # # # # t.circle(70)
# # # # # # # t.end_fill()

# # # # # # # # Draw the big white circle
# # # # # # # t.penup()
# # # # # # # t.goto(60, 0)
# # # # # # # t.pendown()
# # # # # # # t.color("white")
# # # # # # # t.begin_fill()
# # # # # # # t.circle(60)
# # # # # # # t.end_fill()

# # # # # # # # Draw the mini blue circles
# # # # # # # t.penup()
# # # # # # # t.goto(-57, -8)
# # # # # # # t.pendown()

# # # # # # # # The Indian flag is ready!
# # # # # # # turtle.done()


# # # # # # import turtle
# # # # # # screen = turtle.Screen()
# # # # # # t = turtle.Turtle()
# # # # # # t.speed(10)
# # # # # # colors = ["red", "green", "blue", "yellow", "purple"]
# # # # # # t.pensize(5)
# # # # # # for i in range(5):
# # # # # #     t.pencolor(colors[i])
# # # # # #     t.forward(200)
# # # # # #     t.right(144)
# # # # # # t.hideturtle()
# # # # # # turtle.done()


# # # # # import turtle

# # # # # # Set up the screen
# # # # # screen = turtle.Screen()
# # # # # screen.bgcolor("white")

# # # # # # Create a turtle
# # # # # t = turtle.Turtle()
# # # # # t.speed("fastest")  # Set the drawing speed

# # # # # # Custom colors for the petals
# # # # # colors = ["orange", "blue"]

# # # # # # Draw the petals
# # # # # for _ in range(6):
# # # # #     t.color(colors[_ % 2])  # Alternate between orange and blue
# # # # #     t.circle(100)
# # # # #     t.right(60)

# # # # # # Hide the turtle cursor
# # # # # t.hideturtle()

# # # # # # Keep the window open until manually closed
# # # # # turtle.done()


# # # # import turtle as t
# # # # s=t.getscreen()
# # # # a=t.Turtle()
# # # # a.fillcolor("blue")
# # # # a.begin_fill()
# # # # a.fd(100)
# # # # a.left(-90)
# # # # a.fd(100)
# # # # a.right(90)
# # # # a.fd(100)
# # # # a.right(90)
# # # # a.fd(100)
# # # # a.fd(100)
# # # # a.left(90)
# # # # a.fd(100)
# # # # a.left(90)
# # # # a.fd(100)
# # # # a.left(90)
# # # # a.fd(100)
# # # # a.end_fill()
# # # # t.mainloop()

# # # # import tkinter as tk
# # # # from tkinter import messagebox
# # # # def check_credentials():
# # # #     if username_entry.get() == "admin" and password_entry.get() == "password123":
# # # #         messagebox.showinfo("Login Status", "Login successful")
# # # #     else:
# # # #         messagebox.showerror("Login Status", "Login failed")
# # # # root = tk.Tk()
# # # # root.title("Login Form")
# # # # root.geometry('600x600')
# # # # username_label = tk.Label(root, text="Username:")
# # # # username_label.pack()
# # # # username_entry = tk.Entry(root)
# # # # username_entry.pack()
# # # # password_label = tk.Label(root, text="Password:")
# # # # password_label.pack()
# # # # password_entry = tk.Entry(root, show="*")
# # # # password_entry.pack()
# # # # login_button = tk.Button(root, text="Login", command=check_credentials)
# # # # login_button.pack()
# # # # root.mainloop()


# # # import tkinter as tk

# # # def say_hello():
# # #     label.config(text="Hello, Tkinter!")

# # # root = tk.Tk()
# # # root.title("Menu")

# # # menubar = tk.Menu(root)
# # # root.config(menu=menubar)
# # # root.geometry('400x400')

# # # file_menu = tk.Menu(menubar, tearoff=0)
# # # menubar.add_cascade(label="File", menu=file_menu)
# # # file_menu.add_command(label="Say Hello", command=say_hello)
# # # file_menu.add_separator()
# # # file_menu.add_command(label="Exit", command=root.quit)

# # # label = tk.Label(root, text="")
# # # label.pack()

# # # root.mainloop()

# # import turtle

# # # Defining colors
# # colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

# # # Setup turtle pen
# # t = turtle.Pen()

# # # Change the speed of the turtle
# # t.speed(10)

# # # Change the background color
# # turtle.bgcolor("black")

# # # Make spiral web
# # for x in range(200):
# #     t.pencolor(colors[x % 6])  # Setting color
# #     t.width(x / 100 + 1)       # Setting width
# #     t.forward(x)               # Moving forward
# #     t.left(59)                 # Moving left

# # # End the turtle graphics
# # turtle.done()

# import tkinter as tk
# from tkinter import messagebox
# def add_task():
#     task = task_entry.get()
#     if task:
#         listbox.insert(tk.END, task)
#         task_entry.delete(0, tk.END)
#         status_label.config(text="Task added successfully!", fg="green")
#         root.after(2000, lambda: status_label.config(text=""))
#     else:
#         messagebox.showwarning("Warning", "Please enter a task.")
# def delete_task():
#     try:
#         selected_line_index = listbox.curselection()
#         listbox.delete(selected_line_index)
#     except:
#         messagebox.showerror("Error", "Please select a task to delete.")
# root = tk.Tk()
# root.title("Task Manager")
# root.geometry("400x300")
# task_entry = tk.Entry(root, width=40)
# task_entry.pack(pady=10, fill='both', expand=True)
# add_button = tk.Button(root, text="Add Task", bg='light green', fg='gray', command=add_task)
# add_button.pack(pady=5)
# delete_button = tk.Button(root, text="Delete Task", bg='light blue', fg='dark red', command=delete_task)
# delete_button.pack(pady=5)
# listbox = tk.Listbox(root, width=40, height=10)
# listbox.pack(pady=10, fill='both', expand=True)
# status_label = tk.Label(root, text="", fg="green")
# status_label.pack()
# root.mainloop()


import turtle
sm=turtle.Screen().bgcolor("white")
sm=title("house drawing")
h=turtle.Turtle()
h.speed()
def square(colour,side):
    h.fillcolor(colour)
    h.begin_fill()
    for i in range(4):
        f.fd(side)
        h.left(90)
    h.end_fill()
def triangle(colour,side):
    h.fillcolor(colour)
    h.begin_fill()
    for i in range(3):
        h.fd(side)
        h.left(120)
    h.end_fill()
def rectangle(colour,w,h):
    h.fillcolor(colour)
    h.begin_fill()
    for i in range(2):
        h.fd(w)
        h.left(90)
        h.fd(h)
        h.left(90)
    h.end_fill()
h.penup()
h.goto(-50.-50)
h.pendown()
triangle("red",100)
h.penup()
h.goto(-20,-50)
h.pendown()
rectangle("brown",40,60)
h.hideturtle()
turtle.done()