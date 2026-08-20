from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return #this was a small asteroid

        log_event("asteroid_split")

        # generate a random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

        #Compute the new radius of the smaller asteroids using the formula old_radius - ASTEROID_MIN_RADIUS
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #Call the .rotate method on the asteroid's velocity vector to create a new vector representing the first new asteroids movement
        velocity_1 = self.velocity.rotate(angle)
        #Call the .rotate again for the second new asteroid, but this time rotate it in the opposite direction (negative angle).
        velocity_2 = self.velocity.rotate(-angle)
        
        #Create two new Asteroid objects at the current asteroid position with the new radius
        asteriod_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteriod_2 = Asteroid(self.position.x, self.position.y, new_radius)

        #Set the first's .velocity to the first new vector, but make it move faster by scaling it up (multiplying) by 1.2.
        asteriod_1.velocity = velocity_1 * 1.2
        # for the second asteroid
        asteriod_2.velocity = velocity_2 * 1.2