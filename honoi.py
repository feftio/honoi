import pygame
from src.game import Game

'''
class Rect():
    
    def __init__(self, x, y, width=50, height=50, color=color.BACKGROUND):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
'''

if __name__ == "__main__":
    Game(
        pygame=pygame,
        name="Honoi",
        size=(500, 500),
        fps=120
    ).run()