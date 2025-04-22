import pygame
from modulo import construir_grid

def posicionar( jogador=[]):
    marcados = []
    tamanho = 4
    vertical = False
    #fazer se pressionar botão, troca modo
    while len(jogador) < 10:

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN :               
                if event.key == pygame.K_x:
                    vertical = not vertical
                    print(vertical)
            posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)

            if vertical:
                if posicao[0] >= 2 and posicao[1]+tamanho-1 < 10 and (posicao[0],posicao[1]+tamanho-1) not in marcados and posicao not in marcados and posicao[1]+tamanho <= 10 :
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(posicao[0]*100,posicao[1]*100,100,tamanho*100),(2))
                    pygame.display.flip()
                    if event.type==1025:#pegar a posição do mouse na tela
                        print(posicao)
                        posicionou = [(posicao[0],y) for y in range(posicao[1],posicao[1]+tamanho)]
                        for y in range(posicao[1],posicao[1]+tamanho):
                            marcados.append((posicao[0],y)) 
                        jogador.append(posicionou)
                        pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(posicao[0]*100,posicao[1]*100,100,100*tamanho))
                        pygame.display.flip()
                        if len(jogador) in [1,3,6]:
                            tamanho -=1
                            
                elif posicao[1] in range(10-tamanho,10) and (posicao[0],10-tamanho)not in marcados and posicao not in marcados :
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(posicao[0]*100,(10-tamanho)*100,100,tamanho*100),(2))
                    pygame.display.flip()
                    if event.type==1025:#pegar a posição do mouse na tela
                        posicionou = [(posicao[0],y) for y in range(10-tamanho,10)]
                        for y in range(10-tamanho,10):
                            marcados.append((posicao[0],y)) 
                        jogador.append(posicionou)
                        pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(posicao[0]*100,(10-tamanho)*100,100,100*tamanho))
                        pygame.display.flip()
                        if len(jogador) in [1,3,6]:
                            tamanho -=1
                elif posicao in marcados or (posicao[0],posicao[1]+tamanho-1) in marcados:
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.display.flip()

            else:
                if posicao[0] >= 2 and posicao[0]+tamanho < 12 and (posicao[0]+tamanho-1,posicao[1]) not in marcados and posicao not in marcados and posicao[0]+tamanho <= 12 :
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(posicao[0]*100,posicao[1]*100,tamanho*100,100),(2))
                    pygame.display.flip()
                    if event.type==1025:#pegar a posição do mouse na tela
                        posicionou = [(x,posicao[1]) for x in range(posicao[0],posicao[0]+tamanho)]
                        for x in range(posicao[0],posicao[0]+tamanho):
                            marcados.append((x,posicao[1])) 
                        jogador.append(posicionou)
                        pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(posicao[0]*100,posicao[1]*100,100*tamanho,100))
                        pygame.display.flip()
                        if len(jogador) in [1,3,6]:
                            tamanho -=1
                            
                elif posicao[0] in range(12-tamanho,12) and (12-tamanho,posicao[1])not in marcados and posicao not in marcados :
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.draw.rect(pygame.display.get_surface(),(255,0,0),((12-tamanho)*100,posicao[1]*100,tamanho*100,100),(2))
                    pygame.display.flip()
                    if event.type==1025:#pegar a posição do mouse na tela
                        posicionou = [(x,posicao[1]) for x in range(12-tamanho,12)]
                        for x in range(12-tamanho,12):
                            marcados.append((x,posicao[1])) 
                        jogador.append(posicionou)
                        pygame.draw.rect(pygame.display.get_surface(),(0,0,0),((12-tamanho)*100,posicao[1]*100,100*tamanho,100))
                        pygame.display.flip()
                        if len(jogador) in [1,3,6]:
                            tamanho -=1
                elif posicao in marcados or (posicao[0]+tamanho-1,posicao[1]) in marcados:
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.display.flip()

    return jogador
    
if __name__ == "__main__":
    pygame.init()
    tela=pygame.display.set_mode((1200,1000))#definição de tela
    construir_grid(tela,1200)
    tela.blit(pygame.image.load("tela_fundo.jpg"),(0,0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():#sair 
            if event.type== pygame.QUIT:
                pygame.quit()
                exit()
            print(posicionar())

