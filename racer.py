import pygame, sys
from pygame.locals import *
import random, time
pygame.init()
clock= pygame.time.Clock()

W=400
H=600

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
FPS=60
SPEED=5
SCORE=0
SCORE_COIN = 0

font = pygame.font.Font("C:\\Users\\kadyr\\Downloads\\BebasNeue-Regular.ttf", 60)
font_small = pygame.font.Font("C:\\Users\\kadyr\\Downloads\\BebasNeue-Regular.ttf", 20)
font_coin = pygame.font.Font("C:\\Users\\kadyr\\Downloads\\BebasNeue-Regular.ttf", 20)
game_over=font.render("GAME OVER", True, BLACK)

background = pygame.image.load("C:\\Users\\kadyr\\OneDrive\\Изображения\\Снимки экрана\\Снимок экрана 2024-03-31 154934.png")
background= pygame.transform.scale(background, (400,600))
sc=pygame.display.set_mode((W,H))
pygame.display.set_caption("RACER")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\kadyr\\Downloads\\Снимок экрана 2024-03-31 161854-fotor-bg-remover-20240331162020.png")
        self.image=pygame.transform.scale(self.image, (70,150))
        self.rect= self.image.get_rect()
        self.rect.center= (random.randint(40,W-40),0)
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if(self.rect.bottom>600):
            SCORE += 1
            self.rect.top=0
            self.rect.center = (random.randint(40,W-40),0)
    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\kadyr\\OneDrive\\Рабочий стол\\pp2\\lab7\\carr.png")
        self.image=pygame.transform.scale(self.image, (70,150))
        self.rect= self.image.get_rect()
        self.rect.center=(160,520)
    def move(self):
        pressed_keys=pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < W:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\kadyr\\OneDrive\\Рабочий стол\\pp2\\lab7\\coin.png")
        self.image=pygame.transform.scale(self.image, (70,70))
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,W-40), 0)
    def move(self):
        global SCORE_COIN
        self.rect.move_ip(0,2)
        if(self.rect.bottom > 600):
            self.rect.top=0
            self.rect.center = (random.randint(40,W-40),0)
    

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies=pygame.sprite.Group()
enemies.add(E1)

coins=pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

increase=pygame.USEREVENT + 1
pygame.time.set_timer( increase, 1000)

while True:
    for event in pygame.event.get():
        if event.type == increase:
            SPEED+=0.2
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    sc.blit(background, (0,0))
    scores=font_small.render(str(SCORE), True, BLACK)
    sc.blit(scores, (10,10))
    coin_score=font_coin.render(str(SCORE_COIN),True, BLACK)
    sc.blit(coin_score, (382,10))

    

    for entity in all_sprites:
        sc.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(P1,enemies):
        sc.fill(RED)
        sc.blit(game_over, (90,250))
        pygame.display.update() 
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    if pygame.sprite.spritecollideany(P1,coins):
        SCORE_COIN += 1
        C1.rect.center = (random.randint(40, W - 40), 0)
        
    
    pygame.display.update()
    clock.tick(FPS)
