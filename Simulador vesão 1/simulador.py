import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()

diretorio_principal = os.path.dirname(__file__)

largura = 680
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Simulador Maquina Termica")
fps = pygame.time.Clock()

spritesheet = pygame.image.load('Maquina7.png')
botao = pygame.image.load('New Piskel (5).png')


class MaquinaTermica(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.maquinaDesligada = spritesheet.subsurface((0, 0), (32, 32))
        self.image = self.maquinaDesligada
        self.rect = self.image.get_rect()
        self.rect.center = (450, 300)


        self.esquentandoAgua = []
        self.index = 0
        for i in range(1, 3):
            img = spritesheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (500, 500))
            self.esquentandoAgua.append(img)

        ''''self.vapor = spritesheet.subsurface((0, 32), (32, 32))
        self.esquentandoAgua.append(self.vapor)'''

        self.image = self.esquentandoAgua[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (450, 300)


        self.rodando_a_roda = []
        self.index2 = 0

        self.vaporzinho = spritesheet.subsurface((0, 32), (32, 32))
        self.vaporzao = spritesheet.subsurface((64, 32), (32, 32))

        self.vaporzinho = pygame.transform.scale(self.vaporzinho, (450, 450))
        self.vaporzao = pygame.transform.scale(self.vaporzao, (450, 450))

        self.rodando_a_roda.append(self.vaporzinho)
        self.rodando_a_roda.append(self.vaporzao)

        '''for i in range(3):
            img = spritesheet.subsurface((i * 32, 32), (32, 32))
            img = pygame.transform.scale(img, (450, 450))
            self.rodando_a_roda.append(img)'''

        self.image = self.rodando_a_roda[self.index2]
        self.rect = self.image.get_rect()
        self.rect.center = (450, 300)


        self.iniciar = False
        self.terminou1 = False
        self.terminou2 = False
        self.continuar = True
        self.contador = 0

    def iniciarMaquina(self):
        self.iniciar = True

    def update(self):
        if self.iniciar:
            if self.continuar:
                self.index += 0.1
                self.terminou1 = True

            if self.index >= len(self.esquentandoAgua):
                self.index = 0
                self.contador += 1
                print(self.contador)

            if self.contador == 10:
                self.continuar = False
                self.terminou1 = False
                self.terminou2 = True
                self.index2 += 0.2


                if self.index2 >= len(self.rodando_a_roda):
                    self.index2 = 0
        else:
            self.image = self.maquinaDesligada
            self.image = pygame.transform.scale(self.image, (450, 450))

        if self.terminou1:
            self.image = self.esquentandoAgua[int(self.index)]
            self.image = pygame.transform.scale(self.image, (450, 450))
        elif self.terminou2:
            self.image = self.rodando_a_roda[int(self.index2)]
            self.image = pygame.transform.scale(self.image, (450, 450))


class Botao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.botao = []
        self.index = 0

        for i in range(2):
            img = botao.subsurface((0, i * 32), (32, 32))
            img = pygame.transform.scale(img, (500, 500))
            self.botao.append(img)

        self.image = self.botao[self.index]
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)
        self.cor_verde = False


    def mudarCor(self):
        self.cor_verde = True

    def update(self):
        if self.cor_verde:
            self.index = 1

        self.image = self.botao[self.index]
        self.image = pygame.transform.scale(self.image, (500, 500))


spritesMaquina = pygame.sprite.Group()
maquina_termica = MaquinaTermica()
spritesMaquina.add(maquina_termica)

spritesButton = pygame.sprite.Group()
BotaoIniciar = Botao()
spritesButton.add(BotaoIniciar)

while True:
    tela.fill((255, 255, 255))
    fps.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            mouse_positionX = mouse_position[0]
            mouse_positionY = mouse_position[1]

            if mouse_positionX in range(54, 131) and mouse_positionY in range(238, 330):
                BotaoIniciar.mudarCor()
                maquina_termica.iniciarMaquina()

    spritesButton.draw(tela)
    spritesButton.update()
    spritesMaquina.draw(tela)
    spritesMaquina.update()
    pygame.display.flip()

