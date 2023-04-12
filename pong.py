import turtle
import time

window = turtle.Screen()
window.title("Pong by Saakk")
window.setup(width=800, height=600)
window.bgcolor("black")
window.tracer(0)

# Side A
side_a = turtle.Turtle()
side_a.speed(0)
side_a.shape("square")
side_a.color("white")
side_a.shapesize(stretch_wid=5, stretch_len=1)
side_a.penup()
side_a.goto(-350, 0)

# Side B
side_b = turtle.Turtle()
side_b.speed(0)
side_b.shape("square")
side_b.color("white")
side_b.shapesize(stretch_wid=5, stretch_len=1)
side_b.penup()
side_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2


# Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

# Functions to move paddles
def side_a_up():
    if side_a.ycor() <= 250:        
        y = side_a.ycor()
        y += 20
        side_a.sety(y)

def side_b_up():
    if side_b.ycor() <= 250:   
        y = side_b.ycor()
        y += 20
        side_b.sety(y)

def side_a_down():
    if side_a.ycor() >= -250:   
        y = side_a.ycor()
        y -= 20
        side_a.sety(y)

def side_b_down():
    if side_b.ycor() >= -250: 
        y = side_b.ycor()
        y -= 20
        side_b.sety(y)


# Keyboard Binding
window.listen()
window.onkeypress(side_a_up, "w")
window.onkeypress(side_a_down, "s")
window.onkeypress(side_b_up, "Up")
window.onkeypress(side_b_down, "Down")


# Main game loop
while True:
    window.update()

    # Border
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() >= 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
    
    if ball.xcor() <= -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball and paddle collissions
    if (ball.xcor() > 340 and ball.xcor() > 350 and (ball.ycor() < side_b.ycor() + 45 and ball.ycor() > side_b.ycor() - 45)):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -340 and (ball.ycor() < side_a.ycor() + 45 and ball.ycor() > side_a.ycor() - 45)):
        ball.setx(-340)
        ball.dx *= -1

    time.sleep(0.007)