import pygame
from asteroidfield import *
from player import *
from asteroid import *
from logger import log_state
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
def main():
    pygame.init()


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    

    Player.containers= (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)



    clock = pygame.time.Clock() 
    dt = 0.0

    AsteroidField()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player1 = Player(x, y)


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000
        screen.fill("black")

        for object in updatable:
            object.update(dt)

        for object in asteroids:
            object.update(dt)

        for object in drawable:
            object.draw(screen)


        pygame.display.flip()


if __name__ == "__main__":
    main()
