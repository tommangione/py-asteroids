import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.x = self.position.x
        self.y = self.position.y
