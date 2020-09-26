import pygame
from pygame.draw import *

pygame.init()
pygame.font.init()

FPS = 30
screen = pygame.display.set_mode((927, 769))
SKIN = (233, 198, 175)
LIGHT_SKIN = (242, 230, 208)
BLACK = (0, 0, 0)
BLUE = (128, 179, 255)
BROWN = (120, 68, 33)
RED = (255, 42, 42)
ORANGE = (255, 102, 0)
VIOLET = (212, 42, 255)
GREEN = (127, 255, 42)

screen.fill((255, 255, 255))
ellipse(screen, ORANGE, (202, 571, 490, 400))  # Body
polygon(screen, SKIN,
        [(230, 549), (199, 568), (69, 126), (104, 124)])  # Left arm
polygon(screen, SKIN,
        [(703, 563), (671, 550), (817, 137), (854, 135)])  # Right arm
ellipse(screen, LIGHT_SKIN, (40, 40, 90, 95), 1)  # Left hand
ellipse(screen, SKIN, (40, 40, 90, 95))
ellipse(screen, LIGHT_SKIN, (790, 40, 90, 105), 1)  # Right hand
ellipse(screen, SKIN, (790, 40, 90, 105))
circle(screen, SKIN, (450, 400), 230)  # Face
ellipse(screen, BLACK, (328, 318, 96, 87), 1)  # Left eye
ellipse(screen, BLUE, (328, 318, 96, 87))
ellipse(screen, BLACK, (362, 356, 26, 22))
ellipse(screen, BLACK, (474, 319, 96, 86), 1)  # Right eye
ellipse(screen, BLUE, (474, 319, 96, 86))
ellipse(screen, BLACK, (511, 355, 26, 22))
polygon(screen, BLACK, [(431, 415), (469, 415), (450, 448)], 1)  # Nose
polygon(screen, BROWN, [(431, 415), (469, 415), (450, 448)])
polygon(screen, BLACK, [(326, 465), (568, 463), (452, 544)], 1)  # Mouth
polygon(screen, RED, [(326, 465), (568, 463), (452, 544)])
polygon(screen, BLACK,
        [(256, 531), (317, 600), (272, 688), (183, 675), (174, 578)],
        1)  # Left Shoulder
polygon(screen, ORANGE,
        [(256, 531), (317, 600), (272, 688), (183, 675), (174, 578)])
polygon(screen, BLACK,
        [(585, 607), (641, 531), (724, 568), (720, 667), (634, 691)],
        1)  # Right Shoulder
polygon(screen, ORANGE,
        [(585, 607), (641, 531), (724, 568), (720, 667), (634, 691)])
polygon(screen, BLACK, [(255, 283), (227, 225), (289, 230)], 1)
polygon(screen, VIOLET, [(255, 283), (227, 225), (289, 230)])
polygon(screen, BLACK, [(276, 246), (261, 182), (328, 203)], 1)
polygon(screen, VIOLET, [(276, 246), (261, 182), (328, 203)])
polygon(screen, BLACK, [(313, 216), (309, 150), (366, 180)], 1)
polygon(screen, VIOLET, [(313, 216), (309, 150), (366, 180)])
polygon(screen, BLACK, [(348, 196), (355, 131), (405, 171)], 1)
polygon(screen, VIOLET, [(348, 196), (355, 131), (405, 171)])
polygon(screen, BLACK, [(388, 180), (412, 119), (453, 169)], 1)
polygon(screen, VIOLET, [(388, 180), (412, 119), (453, 169)])
polygon(screen, BLACK, [(436, 176), (472, 123), (501, 181)], 1)
polygon(screen, VIOLET, [(436, 176), (472, 123), (501, 181)])
polygon(screen, BLACK, [(489, 185), (522, 129), (554, 185)], 1)
polygon(screen, VIOLET, [(489, 185), (522, 129), (554, 185)])
polygon(screen, BLACK, [(535, 186), (592, 157), (589, 222)], 1)
polygon(screen, VIOLET, [(535, 186), (592, 157), (589, 222)])
polygon(screen, BLACK, [(576, 203), (639, 188), (621, 250)], 1)
polygon(screen, VIOLET, [(576, 203), (639, 188), (621, 250)])
polygon(screen, BLACK, [(611, 231), (675, 228), (645, 285)], 1)
polygon(screen, VIOLET, [(611, 231), (675, 228), (645, 285)])
myfont = pygame.font.SysFont('Impact', 120)
textsurface = myfont.render('PYTHON is AMAZING', True, BLACK, GREEN)
screen.blit(textsurface, (0, -20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
