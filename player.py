from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN
from shot import Shot
import pygame
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2 )

    def rotate(self, dt):
        self.rotation += (dt * PLAYER_TURN_SPEED)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE] and self.shot_timer <= 0:
            self.shot_timer = PLAYER_SHOT_COOLDOWN
            self.shot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shot(self):
        vel = pygame.Vector2(0,1)
        vel = vel.rotate(self.rotation)
        vel *= PLAYER_SHOT_SPEED
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, vel)
