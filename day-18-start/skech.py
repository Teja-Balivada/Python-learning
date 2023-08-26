import turtle as t

tim = t.Turtle()
tim.shape("turtle")

def move_forward():
    tim.fd(10)

def move_backward():
    tim.bk(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()

screen = t.Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
# clear()
screen.exitonclick()