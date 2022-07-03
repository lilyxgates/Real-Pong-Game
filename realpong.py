import turtle
import os

# GLOBAL VARIABLES

# Speed
PADDLE_MOVEMENT = 40
BALL_MOVEMENT = 3.5

dir_path = os.path.dirname(os.path.realpath(__file__))
sound_path = os.path.join(dir_path, 'pong_bounce.wav')

wn = turtle.Screen()
wn.title("Pong by Lily Xi Gates")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# PADDLES
# Paddle A - Left
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B - Right
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Ball Movement
ball.dx = BALL_MOVEMENT
ball.dy = -BALL_MOVEMENT

# SCORING SYSTEM
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Score
score_a = 0
score_b = 0


# FUNCTION: MOVE PADDLES
# Move Paddle A (Left): Up/Down
def paddle_a_up():
    y = paddle_a.ycor()
    y += PADDLE_MOVEMENT
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= PADDLE_MOVEMENT
    paddle_a.sety(y)

# Move Paddle B (Right): Up/Down
def paddle_b_up():
    y = paddle_b.ycor()
    y += PADDLE_MOVEMENT
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= PADDLE_MOVEMENT
    paddle_b.sety(y)
    
# KEYBOARD BINDING
wn.listen()

# Paddle A (Left) - Keyboard Binding
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# Paddle B (Right) - Keyboard Binding
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# MAIN GAME LOOP
while True:
    wn.update()

    # MOVE THE BALL
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # BORDER CHECKING

    # Border Checking: Top/Bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system('afplay "{}"&'.format(sound_path))

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system('afplay "{}"&'.format(sound_path))


    # Border Checking: Sides
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        # Score for Player A
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        # Score for Player B
        score_b += 1
        pen.clear()        
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    

    # PADDLE & BALL COLLISION
    # Paddle B - Left
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor () > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system('afplay "{}"&'.format(sound_path))


    # Paddle A - Right
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor () > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system('afplay "{}"&'.format(sound_path))






        









