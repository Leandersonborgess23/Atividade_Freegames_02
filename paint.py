"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


#alteração
def circle(start, end, width=1):
    up()
    goto(start.x, start.y)
    down()

    #Calculo do raio
    radius = abs(end.x - start.x) / 2

    #Desenhar o circulo
    turtle = Turtle()
    turtle.circle(radius)  
    

#alteração
def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    #Cálculo do comprimento e altura do retangulo
    width = abs(end.x - start.x)
    height = abs(end.y - start.y)
    
    #Desenhar o retangulo
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
        
    end_fill()


#alteração
def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    #Desenhar o triangulo
    for _ in range(3):
        forward(end.x - start.x)
        left(120)
        
    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value

def change_width():
    """Prompt to change width value."""
    width = numinput("Change Width", "Enter the width value:", default=1, minval=1)
    state['width'] = width

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y') #alteração nova cor
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(change_width, 'w') #alteração parametro
done()
