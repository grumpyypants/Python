__author__ = 'James'
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)