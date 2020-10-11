import pygame
from pygame.draw import *

pygame.init()
pygame.font.init()

FPS = 30
screen = pygame.display.set_mode((1600, 769))
SKIN = (233, 198, 175)
LIGHT_SKIN = (242, 230, 208)
BLACK = (0, 0, 0)
BLUE = (128, 179, 255)
BROWN = (120, 68, 33)
RED = (255, 42, 42)
ORANGE = (255, 102, 0)
VIOLET = (212, 42, 255)
GREEN = (127, 255, 42)
YELLOW = (255, 212, 42)
DARK_GREEN = (0, 128, 0)
LIGHT_GREEN = (190, 200, 183)


def fan_draw(x, y, hair_color, tshirt_color, eye_color):
    """
    Функция рисует мальчика на экране.
    x, y - координаты левого верхнего угла
    hair_color - цвет волос мальчика, заданный в формате, подходящем для pygame.Color
    tshirt_color - цвет футболки, заданный в формате, подходящем для pygame.Color
    """
    # Body
    ellipse(screen, tshirt_color, (x + 202, y + 571, 490, 400))
    # Left arm
    polygon(screen, SKIN, [(x + 230, y + 549), (x + 199, y + 568),
            (x + 69, y + 126), (x + 104, y + 124)])
    # Right arm
    polygon(screen, SKIN, [(x + 703, y + 563), (x + 671, y + 550),
            (x + 817, y + 137), (x + 854, y + 135)])
    # Left palm
    ellipse(screen, SKIN, (x + 40, y + 40, 90, 95))
    # Right palm
    ellipse(screen, SKIN, (x + 790, y + 40, 90, 105))
    # Face
    circle(screen, SKIN, (x + 450, y + 400), 230)
    # Left eye
    ellipse(screen, eye_color, (x + 328, y + 318, 96, 87))
    ellipse(screen, BLACK, (x + 362, y + 356, 26, 22))
    # Right eye
    ellipse(screen, eye_color, (x + 474, y + 319, 96, 86))
    ellipse(screen, BLACK, (x + 511, y + 355, 26, 22))
    # Nose
    polygon(screen, BROWN, [(x + 431, y + 415),
            (x + 469, y + 415), (x + 450, y + 448)])
    # Mouth
    polygon(screen, RED, [(x + 326, y + 465),
            (x + 568, y + 463), (x + 452, y + 544)])
    # Left Shoulder
    polygon(screen, tshirt_color, [(x + 256, y + 531), (x + 317, y + 600),
            (x + 272, y + 688), (x + 183, y + 675), (x + 174, y + 578)])
    # Right Shoulder
    polygon(screen, tshirt_color, [(x + 585, y + 607), (x + 641, y + 531),
            (x + 724, y + 568), (x + 720, y + 667), (x + 634, y + 691)])
    # Hair
    polygon(screen, hair_color,
            [(x + 255, y + 283), (x + 227, y + 225), (x + 289, y + 230)])
    polygon(screen, hair_color,
            [(x + 276, y + 246), (x + 261, y + 182), (x + 328, y + 203)])
    polygon(screen, hair_color,
            [(x + 313, y + 216), (x + 309, y + 150), (x + 366, y + 180)])
    polygon(screen, hair_color,
            [(x + 348, y + 196), (x + 355, y + 131), (x + 405, y + 171)])
    polygon(screen, hair_color,
            [(x + 388, y + 180), (x + 412, y + 119), (x + 453, y + 169)])
    polygon(screen, hair_color,
            [(x + 436, y + 176), (x + 472, y + 123), (x + 501, y + 181)])
    polygon(screen, hair_color,
            [(x + 489, y + 185), (x + 522, y + 129), (x + 554, y + 185)])
    polygon(screen, hair_color,
            [(x + 535, y + 186), (x + 592, y + 157), (x + 589, y + 222)])
    polygon(screen, hair_color,
            [(x + 576, y + 203), (x + 639, y + 188), (x + 621, y + 250)])
    polygon(screen, hair_color,
            [(x + 611, y + 231), (x + 675, y + 228), (x + 645, y + 285)])


screen.fill((255, 255, 255))
fan_draw(0, 0, VIOLET, ORANGE, BLUE)
fan_draw(750, 0, YELLOW, DARK_GREEN, LIGHT_GREEN)
myfont = pygame.font.SysFont('Leekawadee', 157)
textsurface = myfont.render('PYTHON is REALLY AMAZING', True, BLACK, GREEN)
screen.blit(textsurface, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
