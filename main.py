from pygame import *

window = display.set_mode((700,500))
window.fill((80, 120, 120))


FPS = 60
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)   
    display.update()