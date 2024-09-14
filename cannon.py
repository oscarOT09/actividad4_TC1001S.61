from random import randrange, choice
import turtle as t
from freegames import vector

# Posición inicial y configuración de la bola y los objetivos
ball = vector(-200, -200)
speed = vector(0, 0)
COLORS = ['red', 'green', 'purple', 'yellow', 'orange']
targets = []fds
TARGET_COLOR = choice(COLORS)
BALL_COLOR = choice(COLORS)


def tap(x, y):
    """Responde al clic en la pantalla."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15


def inside(xy):
    """Devuelve True si el vector xy está dentro de los límites de la pantalla."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Dibuja la bola y los objetivos en la pantalla."""
    t.clear()

    # Dibuja los objetivos
    for target in targets:
        t.goto(target.x, target.y)
        t.dot(20, TARGET_COLOR)

    # Dibuja la bola
    if inside(ball):
        t.goto(ball.x, ball.y)
        t.begin_fill()
        t.color(BALL_COLOR)
        t.left(10)
        for _ in range(8):
            t.forward(20)
            t.left(135)
        t.end_fill()

    t.update()


def move():
    """Mueve la bola y los objetivos."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Mueve los objetivos
    for target in targets:
        target.x -= 1

    # Mueve la bola
    if inside(ball):
        speed.y -= 0.7
        ball.move(speed)

    # Elimina los objetivos que colisionan con la bola
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Repite el movimiento cada 30 ms
    t.ontimer(move, 30)


# Configuración inicial del entorno gráfico
t.setup(420, 420, 370, 0)
t.hideturtle()
t.up()
t.tracer(False)
t.onscreenclick(tap)
move()
t.done()
