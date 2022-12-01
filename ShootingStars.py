import random
import settings
import pygame
class ShootingStars:
    def __init__(self, px, py):
        self.bright = 8
        self.waxing = True
        self.x = px + random.randint(-settings.width / 2 - 300, settings.width / 2 + 300)
        self.y = py + random.randint(-settings.height / 2 - 300, settings.height / 2 + 300)
        self.dx = float(random.randint(-10, 10)) 
        self.dy = float(random.randint(-10, 10))
        self.color = (random.randint(160, 255),random.randint(160, 255),random.randint(160, 255))
        self.trail = []
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.trail.append([self.x, self.y, self.bright])
        for elem in self.trail:
            if elem[2] > 0:
                elem[2] -= 1
        if self.waxing:
            self.bright += 1
        else:
            self.bright -= 1
        if self.bright > 16:
            self.waxing = False

    def draw_shooting_stars(self, xOff, yOff, screen):
        pygame.draw.ellipse(screen, self.color, (self.drawX - self.bright / 2, self.drawY  - self.bright / 2, self.bright, self.bright), 100)
        for t in self.trail:
            drawX = -(t[0] - xOff) + settings.width
            drawY = -(t[1] - yOff) + settings.height
            if t[2] > 1:
                pygame.draw.ellipse(screen, self.color, (drawX - self.bright / 2, drawY  - self.bright / 2, t[2], t[2]), 100)
