from turtle import Turtle, Screen

# Creating Turtle and Screen objects
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_counter_clockwise():
    tim.left(10)


def turn_clockwise():
    tim.right(10)


def screen_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# Listen method allows the screen to expect input
screen.listen()

counter_clockwise = "a"
clockwise = "d"
forwards = "w"
backwards = "s"
clear = "c"

# Providing parameters for the onkey function
screen.onkey(move_forwards, forwards)
screen.onkey(move_backwards, backwards)
screen.onkey(turn_counter_clockwise, counter_clockwise)
screen.onkey(turn_clockwise, clockwise)
screen.onkey(screen_clear, clear)

screen.exitonclick()
