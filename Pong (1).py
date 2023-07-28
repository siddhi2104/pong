import turtle
import winsound

wn = turtle.Screen()
wn.title(" Pong ")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # Helps to run the window faster by updating it manually

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)   
paddle_a.shape("square")    
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # 20px wide and 100px long
paddle_a.penup() # No drawing line
paddle_a.goto(-350, 0) # Starting position of the paddle

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)   
paddle_b.shape("square")    
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # 20px wide and 100px long
paddle_b.penup() # No drawing line
paddle_b.goto(350, 0) # Starting position of the paddle

# Ball
ball = turtle.Turtle()
ball.speed(0)   
ball.shape("circle")    
ball.color("white")
ball.penup() # No drawing line
ball.goto(0, 0) # Starting position of the paddle
ball.dx = 0.4 # Everytime the ball moves, it moves by 0.3px
ball.dy = 0.4 # Everytime the ball moves, it moves by 0.3px

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() # No drawing line
pen.hideturtle() # Hide the turtle
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function  
def paddle_a_up():
    y = paddle_a.ycor() # Returns the y coordinate
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() 
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 40
    paddle_b.sety(y)

# Keyboard binding
wn.listen() # Listen for keyboard input
wn.onkeypress(paddle_a_up, "w") # When user presses w, call paddle_a_up function
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) # Set the x coordinate to the current x coordinate + the value of dx
    ball.sety(ball.ycor() + ball.dy) # Set the y coordinate to the current y coordinate + the value of dy

    # Border checking
    if ball.ycor() > 290: # Top border
        ball.sety(290)
        ball.dy *= -1 # Reverse the direction of the ball

    if ball.ycor() < -290: # Bottom border
        ball.sety(-290)
        ball.dy *= -1 # Reverse the direction of the ball
        
    if ball.xcor() > 390: # Right border
        ball.goto(0, 0) # Reset the ball to the center
        ball.dx *= -1 # Reverse the direction of the ball
        score_a +=1;
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390: # Left border
        ball.goto(0, 0) 
        ball.dx *= -1
        score_b +=1;
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)