import turtle

win = turtle.Screen()
win.title("Pong by @Kohta")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)  # sets the speed to the max possible speed
pad_a.shape("square")
pad_a.color("white")
pad_a.penup()
pad_a.goto(-350, 0)
pad_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)  # sets the speed to the max possible speed
pad_b.shape("square")
pad_b.color("white")
pad_b.penup()
pad_b.goto(350, 0)
pad_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball

# Game loop
while True:
    win.update()  # everytime the game loop runs, it updates the screen, hence updating
