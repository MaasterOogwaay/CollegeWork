import numpy as np
import pygame

# CONSTANTS
TIME_DELAY = 0.0005


# Characteristics of a body in the sim
class Body:
    def __init__(self, pos_array, mass, color, radius=10):
        self.velocity = np.array([[0, 0, 0]])
        self.force = np.array([[0, 0, 0]])
        self.mass = mass
        self.pos = pos_array
        self.radius = radius
        self.thickness = self.radius * 2
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.pos[0][0], self.pos[0][1]), self.radius, self.thickness)

    def add_velocity(self, velocity_array):
        self.velocity = self.velocity + velocity_array

    def add_force(self, force_array):
        self.force = self.force + force_array

    def move(self):
        self.velocity = self.velocity + ((self.force/self.mass) * TIME_DELAY)
        self.pos = self.pos + self.velocity * TIME_DELAY

