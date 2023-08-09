import turtle
t1 = turtle.Turtle()
t1.speed(0)

def goto(turtle,x,y):
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()

def line(turtle,x,y,x1,y1):
    turtle.penup()
    position = turtle.pos()
    turtle.setpos(x,y)
    turtle.pendown()
    turtle.setpos(x1,y1)
    turtle.penup()
    turtle.setpos(position)

    
def drawGraph(turtle):
    size = 300
    goto(turtle,0,0)

    turtle.width(0.01)
    turtle.color("#999")
    for i in range(-500,500,10):
        line(turtle,i,-size,i,size)
        line(turtle,-size,i,size,i)

    turtle.width(2)
    turtle.color("#555")
    for i in range(-size,size+50,50):
        line(turtle,i,-size,i,size)
        line(turtle,-size,i,size,i)
        
    turtle.color("#000")
    turtle.width(4)
    line(turtle,-size,0,size,0)
    line(turtle,0,-size,0,size)

drawGraph(t1)
    
