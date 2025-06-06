import pygame

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (250, 250, 250), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt