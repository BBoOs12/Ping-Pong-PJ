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
        if key_pressed[pygame.K_w] and self.rect.y > -5:
            self.rect.y -= self.speed 
        if key_pressed[pygame.K_s] and self.rect.y < 400:
            self.rect.y += self.speed 

class Racket_2(GameSprite):
    def movement(self):
        key_pressed = key.get_pressed()
        if key_pressed[pygame.K_UP] and self.rect.y > -5:
            self.rect.y -= self.speed 
        if key_pressed[pygame.K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed


racket_1 = Racket_1("source/Player.png", 50, 225, 25, 100)
racket_2 = Racket_2("source/Player.png", 615, 225, 25, 100)

# Game loop
FPS = 60
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == pygame.QUIT:
            game = False

    window.fill((80, 120, 120))  

    #player1
    racket_1.movement()
    racket_2.movement()

    #player2
    racket_1.draw(window)
    racket_2.draw(window)




    #for debug
    print(racket_1.rect.y)


    display.update()
    clock.tick(FPS)

pygame.quit()
