import pygame
from constants import *
from player import Player
from asteroid import Asteroid



asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Asteroid.containers = (asteroids, updatable, drawable)

from asteroidfield import AsteroidField
AsteroidField.containers = (updatable,)
asteroid_field = AsteroidField()



 
def main():   
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Calculate dt for this frame
        dt = clock.tick(60) / 1000
        
        # Update game state
        updatable.update(dt)

        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
              print("Game over!")
              pygame.display.flip()  # update screen one last time
              pygame.time.delay(1000)  # wait 1 second so you can see the message
              pygame.quit()
              return
        
        # Render
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)            
        pygame.display.flip()

if __name__ == "__main__":
    main()