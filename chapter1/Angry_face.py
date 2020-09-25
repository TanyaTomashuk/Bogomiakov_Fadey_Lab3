import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 200),100)
circle(screen, (0, 0, 0), (200, 200),100, 1)
circle(screen, (255, 0, 0), (150, 175), 20)
circle(screen, (0, 0, 0), (150, 175), 20, 1)
circle(screen, (0, 0, 0), (150, 175), 8)
circle(screen, (255, 0, 0), (250, 175), 15)
circle(screen, (0, 0, 0), (250, 175), 15, 1)
circle(screen, (0, 0, 0), (250, 175), 8)
rect(screen, (0, 0, 0), (150, 250, 100, 20))
polygon(screen, (0, 0, 0), [(103, 117), (181, 166), (177, 173), (99, 124)])
polygon(screen, (0, 0, 0), [(220, 166), (297, 137), (300, 144), (223, 173)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
