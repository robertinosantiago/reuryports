import os
import pygame
from placar import Placar
from desafio import Desafio


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.desafio = Desafio(screen)
        self.placar = Placar(screen)

        self.chao = pygame.image.load(os.path.join("imagens", "chao.png")).convert_alpha()
        self.caixa = pygame.image.load(os.path.join("imagens", "caixa.png")).convert_alpha()

        self.font = pygame.font.Font(None, 36)

        self.iniciou = False

    def desenha_texto(self, mensagem, y, cor=(255, 255, 255)):
        texto = self.font.render(mensagem, True, cor)
        x = (self.screen.get_width() - texto.get_width()) // 2
        self.screen.blit(texto, (x, y))

    def desenha_cenario(self):
        total_blocos = self.screen.get_width() // self.chao.get_width() + 1
        altura_chao = self.screen.get_height() - self.chao.get_height()

        for i in range(total_blocos):
            self.screen.blit(self.chao, (i * self.chao.get_width(), altura_chao))

        y_caixa = self.screen.get_height() - self.caixa.get_height() - self.chao.get_height()
        self.screen.blit(self.caixa, (10, y_caixa))
        self.screen.blit(self.caixa, (self.screen.get_width() - self.caixa.get_width() - 10, y_caixa))

    def desenha_tela_instrucoes(self):
        self.desenha_texto("Use as teclas 0 ou 1 para responder", self.screen.get_height() // 2 - 40)
        self.desenha_texto("Pressione ENTER para iniciar", self.screen.get_height() // 2 + 10)

    def desenha_tela_game_over(self):
        self.desenha_texto("Game Over", self.screen.get_height() // 2)

    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000.0
            self.trata_eventos()

            self.screen.fill((0, 0, 0))

            if not self.iniciou:
                self.desenha_tela_instrucoes()
            elif self.placar.vidas <= 0:
                self.desenha_tela_game_over()
            else:
                self.desafio.update(dt)
                self.desafio.draw()

                if self.desafio.fora_tela():
                    self.placar.errou_resposta()
                    self.desafio = Desafio(self.screen)

            self.placar.draw()
            self.desenha_cenario()

            pygame.display.flip()

    def trata_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN:
                if not self.iniciou and event.key == pygame.K_RETURN:
                    self.iniciou = True
                elif event.key == pygame.K_ESCAPE and self.placar.vidas <= 0:
                    self.iniciou = False
                    self.placar.reset()
                    self.desafio = Desafio(self.screen)
                else:
                    if self.iniciou and self.placar.vidas > 0:
                        self.trata_resposta(event.key)

    def trata_resposta(self, key):
        resposta = None
        if key in (pygame.K_0, pygame.K_KP0):
            resposta = 0
        elif key in (pygame.K_1, pygame.K_KP1):
            resposta = 1

        if resposta is not None:
            if self.desafio.expressao.verificar_resposta(resposta):
                self.placar.acertou_resposta()
            else:
                self.placar.errou_resposta()
            self.desafio = Desafio(self.screen)
