from random import randrange , choice
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
colors = ['red', 'green', 'purple', 'yellow', 'orange']
targets = []
target_Color = choice(colors)
ball_Color = choice(colors)

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, target_Color)  

    if inside(ball):
        goto(ball.x, ball.y)
        begin_fill()
        color(choice(colors))
        left(10)
        for _ in range(8):
            forward(20)  # Lado del triángulo
            left(135)  # Ángulo para un triángulo equilátero
        end_fill()

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1

    if inside(ball):
        speed.y -= 0.7
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 30)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
