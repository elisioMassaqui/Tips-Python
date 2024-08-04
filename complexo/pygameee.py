import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Joint:
    def __init__(self, x, y, length, angle):
        self.x = x
        self.y = y
        self.length = length
        self.angle = angle
        self.end_x = x + length * math.cos(angle)
        self.end_y = y + length * math.sin(angle)

    def update(self, angle):
        self.angle = angle
        self.end_x = self.x + self.length * math.cos(angle)
        self.end_y = self.y + self.length * math.sin(angle)

    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.end_x, self.end_y), 5)

joint1 = Joint(400, 300, 100, math.pi/4)
joint2 = Joint(joint1.end_x, joint1.end_y, 100, math.pi/4)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        joint1.update(joint1.angle - 0.09)
    if keys[pygame.K_RIGHT]:
        joint1.update(joint1.angle + 0.09)

    joint2.x, joint2.y = joint1.end_x, joint1.end_y
    joint2.update(joint2.angle)

    screen.fill((0, 0, 0))
    joint1.draw(screen)
    joint2.draw(screen)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
