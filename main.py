import pygame
from constants import *
from player import Player


 
def main():   
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
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
        player.update(dt)
        
        # Render
        screen.fill("black")
        player.draw(screen)            
        pygame.display.flip()

if __name__ == "__main__":
    main()