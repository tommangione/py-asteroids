import pygame
from constants import *
from player import *
from circleshape import *
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.x = self.position.x
        self.y = self.position.y
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            theta = random.uniform(20, 50)
            v1 = self.velocity.rotate(theta)
            v2 = self.velocity.rotate(-theta)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child1 = Asteroid(self.x, self.y, new_radius)
            child1.velocity = v1 * 1.2
            child2 = Asteroid(self.x, self.y, new_radius)
            child2.velocity = v2 * 1.2
            self.kill()
