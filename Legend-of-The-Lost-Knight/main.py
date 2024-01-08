import pygame
import sys
'''
Variables
'''
title = pygame.display.set_caption("Legend of The Lost Knight")
width,height = 1000, 450
white = (255,255,255)
gravity = 1
jump_height = 20
y_velocity = jump_height
jumping = False

'''
Objects
'''
#Sprite Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("idle/idleanim.png")
        self.jump_image = pygame.image.load("idle/idleanim.png")
        self.idle_cycle = [pygame.image.load(f"idle/idleanim{i:0>2}.png") for i in range(1,15)]
        self.walk_cycle = [pygame.image.load(f"walk/walkanim{i:0>2}.png") for i in range(1,9)]
        self.run_cycle = [pygame.image.load(f"run/runanim{i:0>2}.png") for i in range(3,28)]
        self.punch_cycle = [pygame.image.load(f"punch/punchanim{i:0>2}.png") for i in range(7,16)]
        self.idle_animation_index = 0
        self.walk_animation_index = 0
        self.run_animation_index = 0
        self.punch_anim_index = 0
        self.rect = self.image.get_rect()
        self.rect.center = (0,40)
        self.facing_left = False
        self.health = 100
#Move Function
    def move(self, x, y):
        self.rect.move_ip([x,y])
#Draw Function
    def draw(self):
        screen.blit(self.image, self.rect)
#Window Redraw Function
    def redrawWindow(self):
        screen.blit(bg, (bgX, 0))
        screen.blit(bg, (bgX2, 0))
    def redrawWindowLeft(self):
        screen.blit(bg, (-bgX, 0))
        screen.blit(bg, (-bgX2, 0))
#Idle Animation Function
    def idle_animation(self):
        self.image = self.idle_cycle[self.idle_animation_index]
        if self.idle_animation_index < len(self.idle_cycle)-1:
            self.idle_animation_index += 1
        else:
            self.idle_animation_index = 0
#Walk Animation Function
    def walk_animation(self):
        self.image = self.walk_cycle[self.walk_animation_index]
        if self.walk_animation_index < len(self.walk_cycle)-1:
            self.walk_animation_index += 1
        else:
            self.walk_animation_index = 0
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)
        
#Jump Animation Function
    def jump_animation(self):
        pass
#Run Animation Function
    def run_animation(self):
        self.image = self.run_cycle[self.run_animation_index]
        if self.run_animation_index < len(self.run_cycle)-1:
            self.run_animation_index += 1
        else:
            self.run_animation_index = 0
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)
#Punch Animation Function
    def punch_animation(self):
        self.image = self.punch_cycle[self.punch_anim_index]
        if self.punch_anim_index < len(self.punch_cycle)-1:
            self.punch_anim_index += 1
        else:
            self.punch_anim_index = 0
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy/enemy.png")
        self.rect = self.image.get_rect()  
        self.hitcount = 0 
        self.rect.center = (800,40)
'''
Setup
'''
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load("background.png")
bgX = 0
bgX2 = bg.get_width()
run = True
player = Player()
enemy = Enemy()
player.rect.x = 0
player.rect.y = 40
enemy.rect.x = 800
enemy.rect.y = 40
player_list = pygame.sprite.Group()
player_list.add(player)
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)

'''
Main Loop
'''
#While Loop
while run:
    pygame.event.pump()
    enemy.rect.x -= 5
    if enemy.rect.x < 0:
        enemy.rect.x = 300
    clock.tick(30)
    key = pygame.key.get_pressed()
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()
    #Controls
    if key[pygame.K_w]:
        jumping = True
    if jumping:
        player.rect.y -= y_velocity
        y_velocity -= gravity
        if y_velocity < -jump_height:
            jumping = False
            y_velocity = jump_height    
    if key[pygame.K_a]:
        bgX -= 3
        bgX2 -= 3
        player.rect.x -= 5
        player.idle_animation_index = -1
        player.walk_animation()
        player.facing_left = True
    elif key[pygame.K_d]:
        bgX -= 3
        bgX2 -= 3
        player.rect.x += 5
        player.idle_animation_index = -1
        player.walk_animation()
        player.facing_left = False
    else:
        player.idle_animation()
    if key[pygame.K_a] and key[pygame.K_LSHIFT]:
        bgX -= 6
        bgX2 -= 6
        player.rect.x -= 10
        player.walk_animation_index = -1
        player.run_animation()
        player.facing_left = True
    if key[pygame.K_d] and key[pygame.K_LSHIFT]:
        bgX -= 6
        bgX2 -= 6
        player.rect.x += 10
        player.walk_animation_index = -1
        player.run_animation()
        player.facing_left = False  
    if key[pygame.K_e]:
        player.idle_animation_index = -1
        player.punch_animation()
        #Borders
    if player.rect.x > 400:
        player.rect.x = 400
    if player.rect.x < 0:
        player.rect.x = 0
        #Scroll of the Screen
    if player.rect.x > 220 and key[pygame.K_d]:
        player.redrawWindow()
    elif player.rect.x < 100 and key[pygame.K_a]:
        player.redrawWindowLeft()
    else:
        screen.blit(bg,(0,0))
    collision = pygame.sprite.groupcollide(player_list, enemy_list, False, False)
    if collision:
        player.health -= 1/4
    if player.health == 0:
        player.kill()
    if collision and key[pygame.K_e]:
        enemy.hitcount += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
    font = pygame.font.Font("foul-fiend/Foul Fiend.ttf", 16)
    text = font.render("Health:"+str(player.health), True, white)
    textrect = text.get_rect()
    textrect.center = (100,100)
    hitfont = pygame.font.Font("foul-fiend/Foul Fiend.ttf", 16)
    hittext = font.render("Hits:"+str(enemy.hitcount), True, white)
    hitrect = hittext.get_rect()
    hitrect.center = (300,100)
    screen.blit(text, textrect)
    screen.blit(hittext, hitrect)
    player_list.draw(screen)
    enemy_list.draw(screen)
    pygame.display.update()
