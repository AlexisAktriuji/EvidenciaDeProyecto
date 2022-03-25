from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
# Se obtiene un número random para poder cambiar el color cada que se corre el juego
randomSnake = randrange(1, 5)
randomFood = 0
listaColores = ['blue', 'magenta', 'cyan', 'orange', 'black']
if randomSnake < 5:
    randomFood = randomSnake - 1
else: 
    randomFood = randomSnake + 1


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, listaColores[randomSnake])

    square(food.x, food.y, 9, listaColores[randomFood])
    update()
    ontimer(move, 100)


# Creacion de Funcion para el movimiento de la comida un paso a la vez sin salisde la ventana
def moveFood():
    "Movimiento de la comida un paso a la vez sin que salga de la ventana"
    food.x=randrange(-15, 15) * 10
    food.y=randrange(-15, 15) * 10
    ontimer(moveFood, 5000)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
# Se asignan funciones a las teclas
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
moveFood()
done()