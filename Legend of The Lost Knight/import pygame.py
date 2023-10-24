import pygame
import sys
pygame.init()
width = 1280
height = 720
blue = (0,0,255)
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load("background.png")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface((width, height))




run = True
speed = 30
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
    screen.blit(bg, (0,0))
    pygame.display.update()