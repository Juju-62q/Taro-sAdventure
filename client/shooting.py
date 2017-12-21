from random import randint
import pygame
from pygame.locals import QUIT,Rect,KEYDOWN,K_SPACE

pygame.init()
pygame.key.set_repeat(5,5)
SURFACE = pygame.display.set_mode((800,600))
FPSCLOCK = pygame.time.Clock()


def isGameOver(effect, ship_x, ship_y):
    return (ship_x + 10 <= effect.left and ship_x + 75 >= effect.left and ship_y + 10 <= effect.top and ship_y + 50 >= effect.top) or ship_y <= 90 or ship_y >= 450

def main():
    """main loutine"""
    ship_y = 250
    ship_x = 0
    score = 0
    sysfont = pygame.font.SysFont(None,36)
    ship_image = pygame.image.load("ship.png")
    bang_image = pygame.image.load("bang.png")
    wall = Rect(0,100,800,400)
    effects = []

    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        if not game_over:
            score += 10
            pressed_key = pygame.key.get_pressed()

            if pressed_key[pygame.K_UP]:
                ship_y -= 20
            elif pressed_key[pygame.K_DOWN]:
                ship_y += 20
            if pressed_key[pygame.K_RIGHT]:
                ship_x += 20 if ship_x < 700 else 0
            elif pressed_key[pygame.K_LEFT]:
                ship_x -= 20 if ship_x > 0 else 0

            edge = Rect(790,randint(100,490),10,10) if randint(0, 5) == 3 else Rect(0,0,0,0)
            effects.append(edge)
            if len(effects) >= 80:
                del effects[0]
            effects = [x.move(-10,0) for x in effects]

            for effect in effects:
                if isGameOver(effect,ship_x,ship_y):
                    game_over = True
                    break

        SURFACE.fill((103,65,49))


        pygame.draw.rect(SURFACE,(0,0,0),wall)
        for effect in effects:
            pygame.draw.rect(SURFACE, (255, 255, 0), effect)
        SURFACE.blit(ship_image, (ship_x, ship_y))
        score_image = sysfont.render("score is {}".format(score),True,(0,0,225))
        SURFACE.blit(score_image,(600,20))

        if game_over:
            SURFACE.blit(bang_image,(ship_x,ship_y - 40))

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()
