import pygame
from modulo import construir_grid
# adicionar imagem para quadrados não selecionados e selecionados
def turno(jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2):
    j1OK = False
    j2OK= False
    vez = True
    transicao = pygame.USEREVENT
    cont_transicoes = 0
    barco1=pygame.image.load("imagens/barco1.png")
    barco2_v=pygame.image.load("imagens/barco2_v.png")
    barco2_h=pygame.image.load("imagens/barco2_h.png")
    barco3_v=pygame.image.load("imagens/barco3_v.png")
    barco3_h=pygame.image.load("imagens/barco3_h.png")
    barco4_h=pygame.image.load("imagens/barco4_h.png")
    barco4_v=pygame.image.load("imagens/barco4_v.png")
    
    while True:
        for event in pygame.event.get():#sair 
            if event.type== pygame.QUIT:
                pygame.quit()
                exit()
            if vez and j1OK == False :
                
                posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)

                if posicao not in marcadosJ1 and posicao[0] >= 2:
                    construir_grid(pygame.display.get_surface(),1198)
                    pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(posicao[0]*100,posicao[1]*100,100,100),(2))

                    if len(condicaoJ1) > 0:
                        for barco in condicaoJ1:
                            if len(barco) == 4:
                                if barco[0][0] - barco[1][0] == 0:
                                    imagem = barco4_v
                                else:
                                    imagem = barco4_h
                            elif len(barco) == 3:
                                if barco[0][0] - barco[1][0] == 0:
                                    imagem = barco3_v
                                else:
                                    imagem = barco3_h
                            elif len(barco) == 2:
                                if barco[0][0] - barco[1][0] == 0:
                                    imagem = barco2_v
                                else:
                                    imagem = barco2_h
                            else:
                                imagem = barco1
                            
                            pygame.display.get_surface().blit(imagem,(barco[0][0]*100,barco[0][1]*100))
                    pygame.display.flip()

                    if event.type==pygame.MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                        pygame.display.get_surface().blit(pygame.image.load("imagens/J2_vez.png"),(0,0))
                        transicao = pygame.USEREVENT + cont_transicoes
                        pygame.time.set_timer(transicao,3000,1)
                        pygame.display.flip()
                        cont_transicoes +=1
                        for barco in jogador2:
                            if posicao in barco:
                                condicaoJ1.append(barco)
                                for coord in barco:
                                    marcadosJ1.append(coord)
                                break
                            
                        if posicao not in marcadosJ1:
                            marcadosJ1.append(posicao)
                                                               
                        j1OK = True
            if event.type == transicao and j1OK:
                vez = not vez
                pygame.display.get_surface().fill((0,0,255))
                construir_grid(pygame.display.get_surface(),1200)
                pygame.display.flip()
            if not vez and not j2OK:
                posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
                if posicao not in marcadosJ2 and posicao[0] >= 2:
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(posicao[0]*100,posicao[1]*100,100,100),(2))
                    
                    if len(condicaoJ2) > 0:
                        for barco in condicaoJ2:
                            if len(barco) == 4:
                                if barco[0][0] - barco[1][0] == 0:
                                    imagem = barco4_v
                                else:
                                    imagem = barco4_h
                            elif len(barco) == 3:
                                if barco[0][0] - barco[1][0] == 0:
                                    imagem = barco3_v
                                else:
                                    imagem = barco3_h
                            elif len(barco) == 2:
                                if barco[0][0] - barco[1][0] == 0:
                                    imagem = barco2_v
                                else:
                                    imagem = barco2_h
                            else:
                                imagem = barco1
                        pygame.display.get_surface().blit(imagem,(barco[0][0]*100,barco[0][1]*100))
                    pygame.display.flip()

                    if event.type==pygame.MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                        pygame.display.get_surface().blit(pygame.image.load("imagens/J1_vez.png"),(0,0))
                        transicao = pygame.USEREVENT + cont_transicoes
                        pygame.time.set_timer(transicao,3000,1)
                        pygame.display.flip()
                        cont_transicoes +=1
                        vez = not vez
                        j2OK = True
                        for barco in jogador1:
                            if posicao in barco:
                                condicaoJ2.append(barco)
                                for coord in barco:
                                    marcadosJ2.append(coord)
                                break

                        if posicao not in marcadosJ2:
                            marcadosJ2.append(posicao)
            if event.type == transicao and j1OK and j2OK:
                pygame.display.get_surface().fill((0,0,255))
                pygame.display.flip()
                return jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2
                     

            
            