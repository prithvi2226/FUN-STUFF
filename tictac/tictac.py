import turtle

#getting a screen to work on
ws = turtle.Screen()

#defining turtle instance
t = turtle.Turtle()

#Setting up turtle to color green
t.color("Green")

#width-2
t.width("2")

#speed-2
t.speed(2)

#loop for making outside square of length 300
for i in range(4):
    t.forward(300)
    t.left(90)

#inner lines of the square
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(100, 0)
    t.pendown()
    t.left(90)
    t.forward(300)
    t.penup()
    t.goto(200, 0)
    t.pendown()
    t.forward(300)



