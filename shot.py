import pygame

from circleshape import CircleShape

from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (250, 250, 250), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt