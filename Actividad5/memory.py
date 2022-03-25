"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

Propuesta: Que en lugar de números que se utilicen emojis o imagenes para que sea mucho más sencillo memorizarlo
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
# Variable para almacenar el número de taps 
taps = {'taps': 0}
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
writer = Turtle(visible=False)
# Inicializar el contador de pares para poder indicar cuando el jugador gane
pares = {'pares': 0}


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    taps['taps'] += 1
    print("Taps: ", taps['taps'])
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        pares['pares'] += 1
        print("Pares: ", pares['pares'])
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
    
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 27, y) # Se ajusta el número 27 para que el valor se centre correctamente
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center') # Con el parámetro align se centra el texto en el cuadrante
        # Se muestra en pantalla el número de taps que ha realizado el jugador
        goto(0, 220)
        color('black')
        write("Taps: {0}".format(taps['taps'], font=('Arial', 100, 'bold')))
    # Si el número de pares es igual a 32 significa que le jugador ha ganado y se han destapado todos los cuadros
    if pares['pares'] == 32:
        goto(-200, -220)
        color('green')
        write("Ganaste :)", font=('Arial', 50, 'bold'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(500, 500, 370, 0)
addshape(car) 
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()