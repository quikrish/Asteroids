import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
        
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    astrofield = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    astero = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while(True):
            log_state()
            dt = clock.tick(60) / 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     return
            updatable.update(dt)
            for asteroid in asteroids:
                 if asteroid.collides_with(player):
                      log_event("player_hit")
                      print("Game Over!")
                      sys.exit()

            #Add another collision check to the game loop. Loop over each asteroid
            for asteroid in asteroids:
                #for each asteroid, loop over each shot
                for shot in shots:
                     #If a shot and an asteroid collide
                     if asteroid.collides_with(shot):
                          log_event("asteroid_shot")
                          asteroid.split()
                          shot.kill()
                          break 

            # Fill screen with black color
            screen.fill((0,0,0))
            for thing in drawable:
                thing.draw(screen)
            pygame.display.flip()
            

if __name__ == "__main__":
    main()
