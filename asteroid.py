import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            rad = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, rad)
            a2 = Asteroid(self.position.x, self.position.y, rad)
            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2
