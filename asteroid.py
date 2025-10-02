import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),  # white
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2
        )

    def update(self, dt):
        # Move asteroid in a straight line
        self.position += self.velocity * dt

    def split(self):
        # Kill the current asteroid (always destroyed)
        self.kill()

        # If too small, just disappear
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Pick a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors (rotated left & right)
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # New radius (shrinks by ASTEROID_MIN_RADIUS each split)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two new asteroids at the same position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = velocity1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = velocity2
