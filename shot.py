# shot.py
import pygame
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

        # Auto-add to groups if main set Shot.containers
        if hasattr(Shot, "containers"):
            self.add(*Shot.containers)

    def update(self, dt):
        # dt is seconds — position is Vector2
        self.position += self.velocity * dt

        # remove when off screen
        if (self.position.x < -self.radius or self.position.x > SCREEN_WIDTH + self.radius
            or self.position.y < -self.radius or self.position.y > SCREEN_HEIGHT + self.radius):
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen,
                           (255, 255, 0),
                           (int(self.position.x), int(self.position.y)),
                           int(self.radius))


