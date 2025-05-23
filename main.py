import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    asteroid =  pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    astroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill('black')

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroid:
            if obj.col(player):
                print("Game over!")
                return

            for s in shots:
                if s.col(obj):
                    obj.split()
                    s.kill()

        pygame.display.flip()

        #Limit FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
