import pygame
import sys
pygame.init()
width = 1280
height = 720
blue = (0,0,255)
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load("background.png")
#Sprite Class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(blue)
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
#Draw Function
def draw(self, screen):
    screen.blit(self.image, self.rect)
#Move Function
def move(self, x, y):
    self.rect.move_ip(x,y)
key = pygame.key.get_pressed()

all_sprites_list = pygame.sprite.Group() 
player = Sprite(blue, 200, 200)
all_sprites_list.add(player)

if key[pygame.K_d]:
    player.x += 20


#While Loop
run = True
speed = 30
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
    screen.blit(bg, (0,0))
    all_sprites_list.draw(screen)
    pygame.display.flip()