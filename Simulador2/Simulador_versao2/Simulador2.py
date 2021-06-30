import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 720
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Simulador de Maquina termica 2")
fps = pygame.time.Clock()

maquinaSprites = pygame.image.load("Maquina.png")
botaoSprites = pygame.image.load("botão.png")


class MaquinaTermica(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Maquina Desligada
        self.maquinaDesligada = maquinaSprites.subsurface((0, 0), (64, 64))
        self.image = self.maquinaDesligada
        self.image = pygame.transform.scale(self.image, (660, 480))
        self.rect = self.image.get_rect()

        # Esquentando a Agua
        self.esquentandoAgua = []
        self.index1 = 0
        for i in range(1, 3):
            img = maquinaSprites.subsurface((i * 64, 0), (64, 64))
            img = pygame.transform.scale(img, (660, 480))
            self.esquentandoAgua.append(img)

        self.image = self.esquentandoAgua[self.index1]
        self.rect = self.image.get_rect()
        self.iniciar = False
        self.comecou_esquentar = False
        self.time_esquentar = 0

        # Agua fervendo
        self.fervendoAgua = []
        self.index2 = 0
        for i in range(2):
            img = maquinaSprites.subsurface((i * 64, 64), (64, 64))
            img = pygame.transform.scale(img, (660, 480))
            self.fervendoAgua.append(img)

        self.image = self.fervendoAgua[self.index2]
        self.rect = self.image.get_rect()
        self.comecou_ferver = False
        self.time_ferver = 0

        # Vapor Inicial
        self.vapor_inicio = []
        self.index3 = 0
        self.vapor1 = maquinaSprites.subsurface((2 * 64, 64), (64, 64))
        self.vapor2 = maquinaSprites.subsurface((0, 2 * 64), (64, 64))
        self.vapor1 = pygame.transform.scale(self.vapor1, (660, 480))
        self.vapor2 = pygame.transform.scale(self.vapor2, (660, 480))
        self.vapor_inicio.append(self.vapor1)
        self.vapor_inicio.append(self.vapor2)
        self.image = self.vapor_inicio[self.index3]
        self.rect = self.image.get_rect()
        self.comecou_vaporInicial = False
        self.time_vaporInicial = 0


        self.vapor_preechendo = maquinaSprites.subsurface((64, 64 * 2), (64, 64))
        self.image = self.vapor_preechendo
        self.image = self.image = pygame.transform.scale(self.image, (660, 480))
        self.vapor_subindo = False

        # Roda Rodando
        self.roda_rodando = []
        self.index4 = 0
        self.pistao1 = maquinaSprites.subsurface((64 * 2, 64 * 2), (64, 64))
        self.pistao1 = pygame.transform.scale(self.pistao1, (660, 480))
        self.pistao2 = maquinaSprites.subsurface((0, 64 * 3), (64, 64))
        self.pistao2 = pygame.transform.scale(self.pistao2, (660, 480))
        self.roda_rodando.append(self.pistao1)
        self.roda_rodando.append(self.pistao2)

        self.image = self.roda_rodando[self.index4]
        self.rect = self.image.get_rect()
        self.comecou_rodar = False



    def desligar_maquina(self):
        self.iniciar = False


    def iniciar_maquina(self):
        self.iniciar = True

    def update(self):
        if self.iniciar:
            self.index1 += 0.1
            self.comecou_esquentar = True
            print(self.time_esquentar)

            if self.index1 >= len(self.esquentandoAgua):
                self.index1 = 0
                self.time_esquentar += 1

            if self.time_esquentar == 20:
                self.index1 = 0
                self.comecou_esquentar = False
                self.index2 += 0.1
                self.comecou_ferver = True

                if self.index2 >= len(self.fervendoAgua):
                    self.index2 = 0
                    self.time_ferver += 1

                if self.time_ferver == 20:
                    self.index2 = 0
                    self.comecou_ferver = False
                    self.index3 += 0.1
                    self.comecou_vaporInicial = True

                    if self.index3 >= len(self.vapor_inicio):
                        self.index3 = 0
                        self.time_vaporInicial += 1

                    if self.time_vaporInicial == 20:
                        self.index3 = 0
                        self.comecou_vaporInicial = False
                        self.vapor_subindo = True
                        self.vapor_subindo = False
                        self.index4 += 0.1
                        self.comecou_rodar = True

                        if self.index4 >= len(self.roda_rodando):
                            self.index4 = 0
        else:
            self.image = self.maquinaDesligada
            self.image = pygame.transform.scale(self.image, (720, 480))

        if self.comecou_esquentar:
            self.image = self.esquentandoAgua[int(self.index1)]
            self.image = pygame.transform.scale(self.image, (720, 480))
        elif self.comecou_ferver:
            self.image = self.fervendoAgua[int(self.index2)]
            self.image = pygame.transform.scale(self.image, (720, 480))
        elif self.comecou_vaporInicial:
            self.image = self.vapor_inicio[int(self.index3)]
            self.image = pygame.transform.scale(self.image, (720, 480))
        elif self.vapor_subindo:
            self.image = self.vapor_preechendo
            self.image = pygame.transform.scale(self.image, (720, 480))
        elif self.comecou_rodar:
            self.image = self.roda_rodando[int(self.index4)]
            self.image = pygame.transform.scale(self.image, (720, 480))




class Botao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.botaoSprites = []
        self.index = 0

        for i in range(2):
            img = botaoSprites.subsurface((0, i * 32), (32, 32))
            img = pygame.transform.scale(img, (300, 300))
            self.botaoSprites.append(img)

        self.image = self.botaoSprites[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (270, 425)
        self.cor_verde = False

    def voltarCorVermelha(self):
        self.cor_verde = False

    def mudar_cor(self):
        self.cor_verde = True

    def update(self):
        if self.cor_verde:
            self.index = 1
        elif not self.cor_verde:
            self.index = 0

        self.image = self.image = self.botaoSprites[self.index]
        self.image = pygame.transform.scale(self.image, (100, 100))


maquina_sprites_group = pygame.sprite.Group()
maquina_sprites = MaquinaTermica()
maquina_sprites_group.add(maquina_sprites)

botao_sprites_group = pygame.sprite.Group()
botao_sprites = Botao()
botao_sprites_group.add(botao_sprites)


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            print(mouse_position)
            mouse_positionX = mouse_position[0]
            mouse_positionY = mouse_position[1]

            if mouse_positionX in range(161, 176) and mouse_positionY in range(313, 331):
                botao_sprites.mudar_cor()
                maquina_sprites.iniciar_maquina()

        if event.type == KEYDOWN:
            botao_sprites.voltarCorVermelha()
            maquina_sprites.desligar_maquina()


    maquina_sprites_group.draw(tela)
    maquina_sprites_group.update()
    botao_sprites_group.draw(tela)
    botao_sprites_group.update()
    pygame.display.update()