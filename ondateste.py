import pygame
from modulo import construir_grid
from random import choice

def reflexo():
        x = choice(range(1200))
        y = choice(range(1000))
        pygame.draw.rect(pygame.display.get_surface(),(255,255,255),(x,y,5,5,))
        pygame.display.flip()

pygame.init()
tela=pygame.display.set_mode((1200,1000))#definição de tela
relogio = pygame.time.Clock()
jogador1 = []
jogador2 = []
tela.fill((0,0,255))
construir_grid(tela,1200)#função que desenha e e faz a tupla dos quadrados
pygame.display.flip()
relogio = pygame.time.Clock()
refletir = pygame.USEREVENT+1
limpar = pygame.USEREVENT+2
explosao = pygame.USEREVENT +3
pygame.time.set_timer(refletir, 12)
pygame.time.set_timer(limpar,200)
while True:
    posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
    relogio.tick(60)
    for event in pygame.event.get():
            if event.type == refletir:
                print("mar")
                reflexo()
            if event.type == limpar:
                tela.fill((0,0,255))
                construir_grid(tela,1200)
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.time.set_timer(explosao, 10)
                a= 5

            
            if event.type == explosao:
                 a+=5
                 pygame.draw.circle(pygame.display.get_surface(),(255,255,255),(posicao[0],posicao[1]),(100),(5))