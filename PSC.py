import turtle as tu

t = tu.Turtle()  # Turtle object
wn = tu.Screen()  # Screen Object
wn.bgcolor("Tan")  # Screen Bg color
wn.title("Fractal Tree Pattern")
t.left(90)  # moving the turtle 90 degrees towards left
t.speed(200)  # setting the speed of the turtle


def draw(l):  # recursive function taking length 'l' as argument
    if (l < 10):
        return
    else:

        t.pensize(2)  # Setting Pensize
        t.pencolor("MistyRose")  # Setting Pencolor as MistyRose   
        t.forward(l)  # moving turtle forward by 'l'
        t.left(30)  # moving the turtle 30 degrees towards left
        draw(3 * l / 4)  # drawing a fractal on the left of the turtle object 't' with 3/4th of its length
        t.right(60)  # moving the turtle 60 degrees towards right
        draw(3 * l / 4)  # drawing a fractal on the right of the turtle object 't' with 3/4th of its length
        t.left(30)  # moving the turtle 30 degrees towards left
        t.pensize(2)
        t.backward(l)  # returning the turtle back to its original position


draw(10)  # drawing 10 times

t.right(90)
t.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(2)
        t.pencolor("Light Cyan") 
        t.forward(l)
        t.left(30)
        draw(3 * l / 4)
        t.right(60)
        draw(3 * l / 4)
        t.left(30)
        t.pensize(2)
        t.backward(l)


draw(10)

t.left(270)
t.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(2)
        t.pencolor("Light Grey") 
        t.forward(l)
        t.left(30)
        draw(3 * l / 4)
        t.right(60)
        draw(3 * l / 4)
        t.left(30)
        t.pensize(2)
        t.backward(l)


draw(10)

t.right(90)
t.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(2)
        t.pencolor("Light Yellow")
        t.forward(l)
        t.left(30)
        draw(3 * l / 4)
        t.right(60)
        draw(3 * l / 4)
        t.left(30)
        t.pensize(2)
        t.backward(l)


draw(10)


########################################################

def draw(l):
    if (l < 10):
        return
    else:

        t.pensize(3)
        t.pencolor("MistyRose") 
        t.forward(l)
        t.left(30)
        draw(4 * l / 5)
        t.right(60)
        draw(4 * l / 5)
        t.left(30)
        t.pensize(2)
        t.backward(l)


draw(20)

t.right(90)
t.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(3)
        t.pencolor("Light Cyan") 
        t.forward(l)
        t.left(30)
        draw(4 * l / 5)
        t.right(60)
        draw(4 * l / 5)
        t.left(30)
        t.pensize(2)
        t.backward(l)


draw(20)

t.left(270)
t.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(3)
        t.pencolor("Light Grey") 
        t.forward(l)
        t.left(30)
        draw(4 * l / 5)
        t.right(60)
        draw(4 * l / 5)
        t.left(30)
        t.pensize(2)
        t.backward(l)


draw(20)

t.right(90)
t.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(3)
        t.pencolor("Light Yellow") 
        t.forward(l)
        t.left(30)
        draw(4 * l / 5)
        t.right(60)
        draw(4 * l / 5)
        t.left(30)
        t.pensize(2)
        t.backward(l)


draw(20)


########################################################
def draw(l):
    if (l < 10):
        return
    else:

        t.pensize(2)
        t.pencolor("MistyRose")       
        t.forward(l)
        t.left(30)
        draw(6 * l / 7)
        t.right(60)
        draw(6 * l / 7)
        t.left(30)
        t.pensize(2)
        t.backward(l)


draw(30)

t.right(90)
t.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(2)
        t.pencolor("Light Cyan") 
        t.forward(l)
        t.left(30)
        draw(6 * l / 7)
        t.right(60)
        draw(6 * l / 7)
        t.left(30)
        t.pensize(2)
        t.backward(l)


draw(30)

t.left(270)
t.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(2)
        t.pencolor("Light Grey")
        t.forward(l)
        t.left(30)
        draw(6 * l / 7)
        t.right(60)
        draw(6 * l / 7)
        t.left(30)
        t.pensize(2)
        t.backward(l)


draw(30)

t.right(90)
t.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        t.pensize(2)
        t.pencolor("Light Yellow")  
        t.forward(l)
        t.left(30)
        draw(6 * l / 7)
        t.right(60)
        draw(6 * l / 7)
        t.left(30)
        t.pensize(2)
        t.backward(l)


draw(30)
wn.exitonclick()
