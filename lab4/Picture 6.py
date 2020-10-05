import numpy
import pygame
import random

from random import randint

from LIB import *
from pygame.draw import *

pygame.init()

FPS = 30
FRUIT_COLORS = [RED, GREEN, YELLOW, ORANGE]

screen = pygame.display.set_mode((800, 600))


def setup_background(surface, color):
    """
    функция устанавливает цвет фона
    :param surface: объект pygame.Surface
    :param color: цвет фона pygame.Color
    """

    rect(surface, color, (0, 0, 800, 600))


def back_leg(surface, x, y, size):
    """
    рисуем заднюю лапку
    """

    for i in range(110):
        circle(surface, BLACK, (x + int((260 - i // 7) * size), y + int((130 + i) * size)), int(size * 30))

    ellipse(surface, BLACK, (x + int(size * 205), y + int(size * 220), int(size * 80), int(size * 60)))


def front_legs(surface, x, y, size, touch):
    """
    рисуем передние лапки
    """

    # левая нога
    for i in range(70):
        circle(surface, BLACK, (x + int((40 - i // 2) * size), y + int((148 + i*(not touch)) * size)), int(25 * size))
    if not touch:
        ellipse(surface, BLACK, (x - int(26 * size), y + int(size * 207), int(size * 60), int(size * 40)))

    # правая нога
    for i in range(70):
        circle(surface, BLACK, (x + int((125 - i // 2) * size), y + int((175 + i) * size)), int(25 * size))

    ellipse(surface, BLACK, (x + int(size * 54), y + int(size * 228), int(size * 70), int(size * 50)))


def head(surface, x, y, size, touch):
    """
    рисуем голову
    """
    if touch:
        y -= 50 * size / 0.5
        y = int(y)

    ellipse(surface, WHITE, (x, y, int(135 * size), int(200 * size)))

    circle(surface, BLACK, (x + int(90 * size), y + int(130 * size)), int(size * 25))

    ellipse(surface, BLACK, (x, y + int(size * 100), int(size * 44), int(size * 60)))

    ellipse(surface, BLACK, (x + int(size * 33), y + int(size * 163), int(size * 64), int(size * 40)))

    ellipse(surface, BLACK, (x - int(size * 25), y - int(10 * size), int(80 * size), int(50 * size)))

    ellipse(surface, BLACK, (x + int(size * 70), y, int(size * 80), int(size * 50)))


def body(surface, x, y, size, stand):
    """
    рисуем тельце
    """
    body_pos = (x + int(20 * size), y + int(size * 30), int(size * 300), int(size * 150))
    ellipse(surface, WHITE, body_pos)

    line(surface, (0, 0, 0), (x + int(size * 140), y + int(size * 20)), (x + int(size * 133), y + int(size * 195)),
         int(size * 20))


def panda(surface, x, y, size, touch, stand):
    """
    ункция рисует панду
    :param x:
    :param surface: объект pygame.Syrface
    :param x, y: координаты левого верхнего угла туловища
    :param size: размер панды (коэффициент ее увеличение)
    """

    body(screen, x, y, size, stand)

    #front_legs(surface, x, y, size, touch)

    #back_leg(surface, x, y, size)

    #head(surface, x, y, size, touch)


def left_branches(surface, x, y, size, color):
    """
    рисует левые плоды
    """

    # верхние плоды
    ellipse(surface, color[randint(0, len(color)-1)], (x - int(200 * size), y - int(353 * size), int(size * 20),
            int(size * 60)))
    ellipse(surface, color[randint(0, len(color)-1)], (x - int(170 * size), y - int(355 * size), int(size * 20),
            int(size * 60)))
    ellipse(surface, color[randint(0, len(color)-1)], (x - int(140 * size), y - int(345 * size), int(size * 20),
            int(size * 60)))
    ellipse(surface, color[randint(0, len(color)-1)], (x - int(110 * size), y - int(342 * size), int(size * 20),
            int(size * 60)))
    ellipse(surface, color[randint(0, len(color)-1)], (x - int(70 * size), y - int(323 * size), int(size * 20),
            int(size * 60)))

    # нижние плоды
    ellipse(surface, color[randint(0, len(color)-1)], (x - int(size * 80), y - int(size * 210), int(size * 20),
            int(size * 60)))
    ellipse(surface, color[randint(0, len(color)-1)], (x - int(size * 140), y - int(size * 245), int(size * 20),
            int(size * 60)))
    ellipse(surface, color[randint(0, len(color)-1)], (x - int(size * 200), y - int(size * 253), int(size * 20),
            int(size * 60)))


def right_branches(surface, x, y, size, color):
    """ 
    рисует правые плоды
    """

    # верхние плоды
    ellipse(surface, color[randint(0, len(color)-1)], (x + int(size * 80), y - int(size * 360), int(size * 20),
            int(size * 60)))
    ellipse(surface, color[randint(0, len(color)-1)], (x + int(size * 120), y - int(size * 375), int(size * 20),
            int(size * 60)))
    ellipse(surface, color[randint(0, len(color)-1)], (x + int(size * 160), y - int(size * 395), int(size * 20),
            int(size * 60)))
    ellipse(surface, color[randint(0, len(color)-1)], (x + int(size * 200), y - int(size * 410), int(size * 20),
            int(size * 60)))
    ellipse(surface, color[randint(0, len(color)-1)], (x + int(size * 240), y - int(size * 420), int(size * 20),
            int(size * 60)))

    # нижние плоды
    ellipse(surface, color[randint(0, len(color)-1)], (x + int(size * 35), y - int(size * 195), int(size * 20),
            int(size * 60)))
    ellipse(surface, color[randint(0, len(color)-1)], (x + int(size * 80), y - int(size * 230), int(size * 20),
            int(size * 60)))
    ellipse(surface, color[randint(0, len(color)-1)], (x + int(size * 125), y - int(size * 265), int(size * 20),
            int(size * 60)))


def tree(surface, x, y, size, color):
    """
    рисует ствол пальмы
    """

    line(surface, color, (x, y), (x, y - int(100 * size)), int(30 * size))
    line(surface, color, (x + int(25 * size), y - int(335 * size)), (x + int(75 * size), y - int(440 * size)),
         int(size * 14))
    line(surface, color, (x - int(5 * size), y - int(240 * size)), (x + int(25 * size), y - int(320 * size)),
         int(size * 27))
    line(surface, color, (x, y - int(120 * size)), (x, y - int(220 * size)), int(size * 30))

    arc(surface, color, (x - int(390 * size), y - int(360 * size), int(size * 400), int(size * 250)), 0.5, 1.7, 3)
    arc(surface, color, (x - int(310 * size), y - int(260 * size), int(size * 300), int(size * 400)), 0.5, 2, 3)

    arc(surface, color, (x + int(10 * size), y - int(440 * size), int(size * 700), int(size * 400)), 1.8, 2.6, 3)
    arc(surface, color, (x + int(20 * size), y - int(300 * size), int(size * 700), int(size * 300)), 2.2, 3, 3)


def palm(surface, x, y, size, tree_color, fruit_color):
    """
    функция рисует пальму
    :param fruit_color: массив цветов плодов
    :param tree_color: цыет ствола и веток
    :param surface: площадка на которой рисуется пальма, объект pygame.Surface
    :param x: координата х основания ствола пальмы
    :param y: координата у основания ствола пальмы
    :param size: коэффициент растяжения(увеличеия) пальмы
    """

    tree(surface, x, y, size, tree_color)

    left_branches(surface, x, y, size, fruit_color)
    right_branches(surface, x, y, size, fruit_color)


def draw():
    """
    здесь мы рисуем всё
    """
    setup_background(screen, GREY_RED)

    palm(screen, 130, 350, 0.52, GREEN, FRUIT_COLORS)
    palm(screen, 330, 350, 0.52, GREEN, FRUIT_COLORS)
    palm(screen, 480, 350, 0.75, GREEN, FRUIT_COLORS)
    palm(screen, 640, 350, 0.56, GREEN, FRUIT_COLORS)

    #panda(screen, 500, 400, 0.8, False, False)

    #panda(screen, 150, 300, 0.25, False, False)
    #panda(screen, 160, 270, 0.15, True, False)

    panda(screen, 300, 500, 0.3, False, True)


draw()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
