import pygame
from circleshape import CircleShape  # parent class

class Asteroid(CircleShape):

    containers = None

    def __init__(self, x, y, radius):

        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            (255, 255, 255),                    # white color
            (int(self.position.x), int(self.position.y)),  # position
            self.radius,                         # radius
            2                                    # width
        )

    def update(self, dt):
        # Move asteroid in a straight line
        self.position += self.velocity * dt