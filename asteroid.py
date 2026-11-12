import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import *
from logger import log_state, log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)



    def draw(self, screen):

        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)



    def update(self, dt: float) -> None:

        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            new1_asteroid = self.velocity.rotate(new_angle)
            new2_asteroid = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new1_asteroid * 1.2
            asteroid2.velocity - new2_asteroid * 1.2

        