import turtle
import os
import time

HEIGHT = 800
WIDTH = 800

a_score = 0
b_score = 0

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=WIDTH, height=HEIGHT)
window.tracer(n=0)


def Draw_shape(pos, wid=5, _len=1, ball=False):
	paddle = turtle.Turtle()
	paddle.speed(0)
	paddle.shapesize(stretch_wid=wid, stretch_len=_len)
	paddle.shape("square")
	paddle.penup()
	paddle.color("white")
	paddle.goto(pos)
	if ball:
		paddle.dx = 0.3
		paddle.dy = 0.3

	return paddle

paddel_a = Draw_shape((-370, 0))
paddel_b = Draw_shape((370, 0))
ball =  Draw_shape((0, 0), wid=1, ball=True)
####################Pen############################
pen = turtle.Turtle()
pen.speed()
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0, 350)
pen.write(f"{a_score}		{b_score}", align="center", font=("Courier", 23, "bold"))
##################Movment###########################
def move_up_a():
	y = paddel_a.ycor()
	y += 15
	paddel_a.sety(y)

def move_down_a():
	y = paddel_a.ycor()
	y -= 15
	paddel_a.sety(y)

def move_up_b():
	y = paddel_b.ycor()
	y += 15
	paddel_b.sety(y)

def move_down_b():
	y = paddel_b.ycor()
	y -= 15
	paddel_b.sety(y)


window.listen()
window.onkeypress(move_up_a, "w")
window.onkeypress(move_down_a, "x")
window.onkeypress(move_up_b, "Up")
window.onkeypress(move_down_b, "Down")


while True:
	window.update()
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	if paddel_b.ycor() - 40 <= -380 :
		paddel_b.sety(-350)

	if paddel_a.ycor() - 40 <= -380 :
		paddel_a.sety(-350)

	if paddel_b.ycor() + 40 >= 380 :
		paddel_b.sety(350)

	if paddel_a.ycor() + 40 >= 380 :
		paddel_a.sety(350)

	if  ball.ycor() > 390 :
		os.system("aplay bounce.wav&")
		ball.dy *= -1 


	if ball.ycor() < -390:
		os.system("aplay bounce.wav&")
		ball.dy *= -1 

	if ball.xcor() > 390:
		ball.dx *= -1 
		a_score += 1
		os.system("aplay bounce.wav&")
		pen.clear()
		pen.write(f"{a_score}		{b_score}", align="center", font=("Courier", 23, "bold"))
		ball.goto(0, 0)
		time.sleep(0.6)

	if ball.xcor() < -390:
		ball.dx *= -1 
		b_score += 1
		os.system("aplay bounce.wav&")
		pen.clear()
		pen.write(f"{a_score}		{b_score}", align="center", font=("Courier", 23, "bold"))
		ball.goto(0, 0)
		time.sleep(0.6)

	if (ball.xcor() > 360 and ball.xcor() < 380) and (ball.ycor() < paddel_b.ycor() + 50 and ball.ycor() > paddel_b.ycor() - 50):
		ball.setx(350)
		os.system("aplay bounce.wav&")
		ball.dx *= -1

	if (ball.xcor() < -360 and ball.xcor() > -380) and (ball.ycor() < paddel_a.ycor() + 50 and ball.ycor() > paddel_a.ycor() - 50):
		ball.setx(-350)
		os.system("aplay bounce.wav&")
		ball.dx *= -1
