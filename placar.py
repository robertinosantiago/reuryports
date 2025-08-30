import os
import pygame

class Placar:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.coracao = pygame.image.load(os.path.join("imagens", "coracao.png")).convert_alpha()
        self.acertou = pygame.mixer.Sound(os.path.join("sons", "acertou.wav"))
        self.errou = pygame.mixer.Sound(os.path.join("sons", "errou.wav"))
        self.reset()

    def reset(self):
        self.pontos = 0
        self.vidas = 5

    def draw(self):
        self.exibe_pontos()
        self.exibe_vidas()

    def exibe_pontos(self):
        texto_placar = self.font.render(f"Pontos: {self.pontos}", True, (255, 255, 255))
        self.screen.blit(texto_placar, (10, 10))

    def exibe_vidas(self):
        espacamento = 5
        total = self.vidas * self.coracao.get_width() + (self.vidas - 1) * espacamento
        inicio = self.screen.get_width() - total - 10
        for i in range(self.vidas):
            x = inicio + i * (self.coracao.get_width() + espacamento)
            self.screen.blit(self.coracao, (x, 10))

    def acertou_resposta(self):
        self.acertou.play()
        self.pontos += 10

    def errou_resposta(self):
        self.errou.play()
        self.vidas -= 1
