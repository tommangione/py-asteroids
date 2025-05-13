from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    myfield = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while (0<1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black", rect=None, special_flags=0)
        for member in updatable:
            member.update(dt)
        for rock in asteroids:
            if rock.collide(player) == True:
                print ("Game over!")
                return 0
            for member in shots:
                if member.collide(rock) == True:
                    member.kill()
                    rock.split()
        for member in drawable:
            member.draw(screen)
        #for member in shots:
        #    member.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
