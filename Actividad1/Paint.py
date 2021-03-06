"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
import math

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
    # Dibujar los 4 lados del cuadrado
    for count in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()


def circles(start, end):
    """Draw circle from start to end."""
    # Cálculo del radio por medio de la fórmula de distancia entre dos puntos
    r = math.sqrt((end.x - start.x)**2 + (end.y - end.x)**2) / 2
    up()
    goto(start.x, start.y)
    down()
    begin_fill() 
    circle(r)
    end_fill()    


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    # Dibujar el recángulo y dependiendo de los lados, la distancia entre los puntos es el doble de la distancia o solo la distancia
    for count in range(4):
        if(count == 1 or count == 3):
            forward(end.x - start.x)
            left(90)
        else:
            forward(2 * (end.x - start.x))
            left(90)

    end_fill()


def triangle(start, end):
    #Esta es la funcion del Triangulo y funciona con "t" , selceccion de color abajo.
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
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


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
# Asignación de colores dependiendo de la letra que sea tecleada
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('magenta'), 'M') 
onkey(lambda: color('yellow'), 'Y')
# Asignación de funciones de dibujo dependiendo de la letra que sea tecleada
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circles), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()