import pygame
from modulo import construir_grid,mar,nuvem

pygame.mixer.init()
bomba_agua=pygame.mixer.Sound("audio/acerto_agua.mp3")
bomba_barco=pygame.mixer.Sound("audio/acerto_barco.mp3")
    
def mapa(estado,marcados,repeticao):
    coordenadas = []
    for barco in estado:
        for lugar in barco:
            if lugar not in coordenadas:
                coordenadas.append(lugar)

    construir_grid(pygame.display.get_surface(),1000,repeticao,estado)
    for x in range(10):
        for y in range(10):
            if (x,y) not in coordenadas:
                pygame.display.get_surface().blit(nuvem[0],(x*100,y*100))
                pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(x*100,y*100,100,100),(2))
    for lugar in marcados:
        if lugar not in coordenadas:
            pygame.display.get_surface().blit(mar[repeticao%4],(lugar[0]*100,lugar[1]*100))
            pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(x*100,y*100,100,100),(2))
    pygame.display.flip()
        
def ataque(posicao,condicao,marcados):
    timer = pygame.USEREVENT
    pygame.time.set_timer(timer, 100)
    ciclo = 1
    for barco in condicao:
        if posicao in barco:
            pygame.mixer.Sound.play(bomba_barco)
            while ciclo < 15:
                for event in pygame.event.get():
                
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    
                    if event.type == timer:
                        for coord in barco:
                            pygame.display.get_surface().blit(mar[0],(coord[0]*100,coord[1]*100))
                            pygame.display.get_surface().blit(nuvem[int(ciclo//1.5)],(coord[0]*100,coord[1]*100))
                            pygame.display.flip()
                            
                        ciclo += 1
            mapa(condicao,marcados,0)
            while ciclo < 31:
                for event in pygame.event.get():
                    if event.type == timer:
                        ciclo += 1
            return None
    pygame.mixer.Sound.play(bomba_agua)
    while ciclo < 15:
        for event in pygame.event.get():
                
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    
                    if event.type == timer:
                        
                        pygame.display.get_surface().blit(mar[0],(posicao[0]*100,posicao[1]*100))
                        pygame.display.get_surface().blit(nuvem[int(ciclo//1.5)],(posicao[0]*100,posicao[1]*100))
                        pygame.display.flip()
                        ciclo += 1
    while ciclo < 31:
        for event in pygame.event.get():
            if event.type == timer:
                ciclo += 1
    return None
        
def turno(jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2):
    j1OK = False
    j2OK= False
    vez = True
    executar = True
    transicao = pygame.USEREVENT
    cont_transicoes = 0
    timer = pygame.USEREVENT+1
    pygame.time.set_timer(timer, 100)
    ciclo = 0

    mapa(condicaoJ1,marcadosJ1,ciclo)    
    
    while executar:
        for event in pygame.event.get(): 
            if event.type== pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == timer:
                ciclo += 1
            if vez and not j1OK:
                
                posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)

                if posicao not in marcadosJ1:
                    mapa(condicaoJ1,marcadosJ1,ciclo)
                    pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(posicao[0]*100,posicao[1]*100,100,100),(2))
                    pygame.display.flip()

                    if event.type==pygame.MOUSEBUTTONDOWN:
                        for barco in jogador2:
                            if posicao in barco:
                                condicaoJ1.append(barco)
                                for coord in barco:
                                    marcadosJ1.append(coord)
                                break
                            
                        if posicao not in marcadosJ1:
                            marcadosJ1.append(posicao)

                        ataque(posicao,condicaoJ1,marcadosJ1)

                        if len(condicaoJ1) == 10:
                            return jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2
                        
                        pygame.display.get_surface().blit(pygame.transform.scale(pygame.image.load("imagens/J2_vez.png"),(1000,1000)),(0,0))
                        transicao = pygame.USEREVENT + cont_transicoes
                        pygame.time.set_timer(transicao,1500,1)
                        pygame.display.flip()
                        cont_transicoes += 1                              
                        j1OK = True
            
            if event.type == transicao and j1OK and not j2OK:
                vez = not vez
                mapa(condicaoJ2,marcadosJ2,ciclo)
                pygame.display.flip()

            if not vez and not j2OK:
                posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
                if posicao not in marcadosJ2:
                    mapa(condicaoJ2,marcadosJ2,ciclo)
                    pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(posicao[0]*100,posicao[1]*100,100,100),(2))
                    pygame.display.flip()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for barco in jogador1:
                            if posicao in barco:
                                condicaoJ2.append(barco)
                                for coord in barco:
                                    marcadosJ2.append(coord)
                                break

                        if posicao not in marcadosJ2:
                            marcadosJ2.append(posicao)
                        ataque(posicao,condicaoJ2,marcadosJ2)
                        if len(condicaoJ2) == 10:
                            return jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2
                        
                        pygame.display.get_surface().blit(pygame.transform.scale(pygame.image.load("imagens/J1_vez.png"),(1000,1000)),(0,0))
                        transicao = pygame.USEREVENT + cont_transicoes
                        pygame.time.set_timer(transicao,1500,1)
                        pygame.display.flip()
                        cont_transicoes +=1
                        vez = not vez
                        j2OK = True

                        
            if event.type == transicao and j1OK and j2OK:
                return jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2
            
            if event.type == pygame.KEYDOWN :               
                    if event.key == pygame.K_f:
                        return jogador1,jogador2,marcadosJ1,marcadosJ2,[1,1,1,1,1,1,1,1,1,1],condicaoJ2
            
                     

            
            