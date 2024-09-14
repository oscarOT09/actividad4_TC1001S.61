from random import randrange, choice
from turtle import *
from freegames import vector

# Inicialización de la bola y su velocidad.
ball = vector(-200, -200)
speed = vector(0, 0)

# Colores posibles para la bola y los objetivos.
colors = ['red', 'green', 'purple', 'yellow', 'orange']
targets = []

# Selecciona un color aleatorio para los objetivos y la bola.
target_color = choice(colors)
ball_color = choice(colors)

def tap(x, y):
    """
    Responde a un toque en la pantalla. Si la bola está fuera de los 
    límites, la reposiciona y ajusta su velocidad basada en la posición del clic.
    """
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15

def inside(xy):
    """
    Verifica si una coordenada está dentro de la pantalla.
    Devuelve True si las coordenadas xy están dentro de los límites.
    """
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """
    Dibuja la bola y los objetivos en la pantalla.
    """
    clear()

    # Dibuja todos los objetivos en la pantalla.
    for target in targets:
        goto(target.x, target.y)
        dot(20, target_color)

    # Dibuja la bola si está dentro de los límites de la pantalla.
    if inside(ball):
        goto(ball.x, ball.y)
        begin_fill()
        color(choice(colors))  # Elige un color aleatorio para la bola.
        left(10)
        # Dibuja la forma de la bola con 8 lados.
        for _ in range(8):
            forward(20)
            left(135)
        end_fill()

    update()  # Actualiza la pantalla.

def move():
    """
    Mueve la bola y los objetivos en la pantalla.
    Crea nuevos objetivos y reposiciona los que salen de los límites.
    """
    # Crea un nuevo objetivo aleatoriamente.
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Mueve los objetivos existentes.
    for target in targets:
        target.x -= 1

        # Reposiciona el objetivo si sale de los límites de la pantalla.
        if not inside(target):
            target.x = 200
            target.y = randrange(-150, 150)

    # Mueve la bola si está dentro de los límites.
    if inside(ball):
        speed.y -= 0.7  # La gravedad afecta la velocidad vertical de la bola.
        ball.move(speed)

    # Reposiciona la bola si sale de los límites de la pantalla.
    if not inside(ball):
        if ball.x < -200:
            ball.x = 200
        elif ball.x > 200:
            ball.x = -200
        if ball.y < -200:
            ball.y = 200
        elif ball.y > 200:
            ball.y = -200

    # Duplica la lista de objetivos y limpia la original.
    dupe = targets.copy()
    targets.clear()

    # Mantén solo los objetivos que no colisionen con la bola.
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()  # Redibuja la pantalla.
    ontimer(move, 30)  # Llama a la función move cada 30 milisegundos.

# Configuración del entorno gráfico.
setup(420, 420, 370, 0)  # Establece el tamaño y la posición de la ventana.
hideturtle()  # Oculta el cursor de la tortuga.
up()  # Levanta el lápiz para que no dibuje líneas mientras se mueve.
tracer(False)  # Desactiva el trazado automático para evitar retrasos.
onscreenclick(tap)  # Vincula la función tap al clic en pantalla.
move()  # Inicia el movimiento de los objetos.
done()  # Finaliza el programa cuando se cierra la ventana.
