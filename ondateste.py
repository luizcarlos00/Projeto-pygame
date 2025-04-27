import pygame
from modulo import construir_grid
from random import choice
mar = [pygame.transform.scale(pygame.image.load("imagens/aguaspt01.png"),(1000,1000)),
       pygame.transform.scale(pygame.image.load("imagens/aguaspt02.png"),(1000,1000)),
       pygame.transform.scale(pygame.image.load("imagens/aguaspt03.png"),(1000,1000)),
       pygame.transform.scale(pygame.image.load("imagens/aguaspt04.png"),(1000,1000))]
nuvem = [pygame.transform.scale(pygame.image.load("imagens/nuvem01.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem02.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem03.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem04.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem05.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem06.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem07.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem08.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem09.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem10.png"),(1000,1000)),]
def reflexo(contador):
        x = choice(range(1000))
        y = choice(range(1000))
        #pygame.draw.rect(pygame.display.get_surface(),(255,255,255),(x,y,5,5,))
        #pygame.display.flip()
        if contador % 12 == 0:
            for a in range(x-50,x+60):
                  pygame.draw.rect(pygame.display.get_surface(),(255,255,255),(a,y,5,5,))
            pygame.display.flip()
                  
                  
pygame.init()
tela=pygame.display.set_mode((1000,1000))#definição de tela
relogio = pygame.time.Clock()
jogador1 = []
jogador2 = []
contador = 0
tela.blit(mar[0],(0,0))
construir_grid(tela,1000,0)#função que desenha e e faz a tupla dos quadrados
pygame.display.flip()
relogio = pygame.time.Clock()
refletir = pygame.USEREVENT
limpar = pygame.USEREVENT+2
explosao = pygame.USEREVENT +3
pygame.time.set_timer(refletir, 100)
#pygame.time.set_timer(limpar,200)
for i in range(10):
                     
                    tela.blit(nuvem[i],(i*100,0))
while True:

   
   for event in pygame.event.get():
                
                 
            if event.type == refletir:
                
                contador+= 1
                pygame.display.flip()
            if event.type == limpar:
                tela.fill((0,0,255))
                construir_grid(tela,1000,0)
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
                pygame.time.set_timer(explosao, 15,25)
                centro = ((pygame.mouse.get_pos()[0]//100)*100+50,(pygame.mouse.get_pos()[1]//100)*100+50)
                a= 0

            
            if event.type == explosao:
                 a+=2
                 pygame.draw.circle(pygame.display.get_surface(),(255,255,255),(centro[0],centro[1]),(a),(5))
                 