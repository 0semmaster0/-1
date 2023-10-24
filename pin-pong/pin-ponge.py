
from pygame import *
from random import *
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__ (self,p_image,px,py,sx,sy,speed):
        super().__init__()
        self.sx =sx
        self.sy =sy
        self.image = transform.scale(image.load(p_image),(sx,sy))
        self.speed = speed    
        self.rect = self.image.get_rect()
        self.rect.x=px
        self.rect.y=py 
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
        
class Player(GameSprite):
    def update1(self):
        keys_p = key.get_pressed()
        if keys_p[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_p[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

    def update2(self):
        keys_p = key.get_pressed()
        if keys_p[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_p[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

window = display.set_mode((700,500))
display.set_caption('pin-pongs')
back = transform.scale(image.load('fon.png'),(700,500))

clock=time.Clock()
game = True
finish = False

bolll=GameSprite('boll.png',320,220,50,50,4)
hero1= Player('roket.png',5,10,50,150,4)
hero2= Player('roket.png',640,340,50,150,4)

font.init()
font1 = font.SysFont('Arial',70)
win1 = font1.render('WIN PLAYER 1!',1,(60,144,250))
win2 = font1.render('WIN PLAYER 2!',1,(60,144,250))

vx=4
vy=4
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish == False:
        window.blit(back,(0,0))
        
        hero1.update2()
        hero2.update1()
        bolll.rect.x += vx
        bolll.rect.y -= vy

        if sprite.collide_rect(bolll,hero1) or sprite.collide_rect(bolll,hero2):
            vx=vx * (-1)

        if bolll.rect.y < 5:
            vy *=(-1)
        if bolll.rect.y > 445:
            vy *=(-1)
        if bolll.rect.x < 1:
            finish=True
            window.blit(win2,(130,200))
        if bolll.rect.x > 645:
            finish=True
            window.blit(win1,(130,200))
        hero1.reset()
        hero2.reset()
        bolll.reset()

    display.update()
    clock.tick(65)       