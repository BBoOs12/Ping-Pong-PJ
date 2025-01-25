import pygame
from pygame import sprite, image, transform, event, key, display, time

pygame.init()

window = display.set_mode((700,500))
window.fill((80, 120, 120))

class GameSprite(sprite.Sprite):
    def __init__(self, image_path, x, y, width, height, speed=10, speed2=2):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.speed2 = speed2
        self.direction = 1

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

class Racket_1(GameSprite):
    def movement(self):
        key_pressed = key.get_pressed()
        if key_pressed[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed 
        if key_pressed[pygame.K_s] and self.rect.y < 400:
            self.rect.y += self.speed 

class Racket_2(GameSprite):
    def movement(self):
        key_pressed = key.get_pressed()
        if key_pressed[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed 
        if key_pressed[pygame.K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed


racket_1 = Racket_1("source/Player.png", 20, 225, 25, 100)
racket_2 = Racket_2("source/Player.png", 650, 225, 25, 100)
ball = GameSprite('source/ball.png', 450, 225, 40, 40)

#Value 
FPS = 60
speed_x = 3
speed_y = 3
white = (255, 255, 255)

#Texts
font = pygame.font.SysFont("Arial", 36)
lose1 = font.render("P1 : Game Over", True, white)
lose2 = font.render("P2 : Game Over", True, white)




# Game loop
clock = time.Clock()
finish =False
game = True
while game:
    for e in event.get():
        if e.type == pygame.QUIT:
            game = False

    window.fill((80, 120, 120))  
    if finish != True:
        #player1
        racket_1.movement()
        racket_1.draw(window)
        
        #player2
        racket_2.draw(window)
        racket_2.movement()

        ball.draw(window)
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide_rect(racket_1, ball) or sprite.collide_rect(racket_2, ball):
        speed_x = speed_x *(-1)

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y = speed_y * (-1)

    if ball.rect.x > 700:
        finish = True
        window.blit(lose1,(200, 200))

    if ball.rect.x < 0:
        finish = True
        window.blit(lose2,(200, 200))
    #for debug
    #print(racket_1.rect.y)


    display.update()
    clock.tick(FPS)

pygame.quit()