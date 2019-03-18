import turtle

my_turtle = turtle.Turtle()  # create a turtle object
my_screen = turtle.Screen()  # create a screen object

my_turtle.width(4)
my_turtle.speed(0) # 0 means as fast as it will
my_turtle.shape("turtle") # makes the pen that draws it look like a turtle

def march_mathness(x, y, height, depth):
    # top of the C bracket

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(90)
    my_turtle.forward(height)
    my_turtle.right(90)
    my_turtle.forward(100)
    pos1 = my_turtle.pos()

    # bottom of the C bracket
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(270)
    my_turtle.forward(height)
    my_turtle.left(90)
    my_turtle.forward(100)
    pos2 = my_turtle.pos()

    if depth > 0:
        march_mathness(pos1[0], pos1[1], height / 2, depth - 1)
        march_mathness(pos2[0], pos2[1], height / 2, depth - 1)


#recursive_rect(1, 20, 50, 40)
march_mathness(-250, 0, 180, 5)

my_screen.exitonclick()