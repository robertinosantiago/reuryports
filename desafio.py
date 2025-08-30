import os
import random
import pygame
from expressao import Expressao

class Desafio:
    def __init__(self, screen):
        self.expressao = Expressao()
        self.screen = screen
        self.x = self.screen.get_width() // 2
        self.y = 0

    def update(self, dt):
        self.y += 100 * dt

    def draw(self):
        font = pygame.font.Font(os.path.join("fonts", "ka1.ttf"), 60)
        text = font.render(self.expressao.get_expressao().upper(), True, (255, 255, 255))
        self.screen.blit(text, (self.x - text.get_width() // 2, self.y))

    def fora_tela(self):
        return self.y > self.screen.get_height() - 96