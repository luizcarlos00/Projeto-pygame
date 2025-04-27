import pygame
from modulo import construir_grid



def marcar(x,y,tam,vertical,jogador,ciclo):
    if vertical:
        construir_grid(pygame.display.get_surface(),1000,ciclo,jogador)
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(x*100,y*100,100,tam*100),(2))
        pygame.display.flip()
    else:
        construir_grid(pygame.display.get_surface(),1000,ciclo,jogador)
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(x*100,y*100,tam*100,100),(2))
        pygame.display.flip()

def colisaoX(marcados, posicao,tamanho):
    espacos = [x for x in range(posicao[0],posicao[0]+tamanho)]
    for x in espacos:
        if (x,posicao[1]) in marcados:
            return True
    return False

def colisaoY(marcados, posicao,tamanho):
    espacos = [y for y in range(posicao[1],posicao[1]+tamanho)]
    for y in espacos:
        if (posicao[0],y) in marcados:
            return True
    return False

def colocarX(posX,posY,tam):
    selecionados = []
    for x in range(posX,posX+tam):
        selecionados.append((x,posY))
    return selecionados

def colocarY(posX,posY,tam):
    selecionados = []
    for y in range(posY,posY+tam):
        selecionados.append((posX,y)) 
    return selecionados
    
def posicionar( jogador=[]):

    timer = pygame.USEREVENT
    pygame.time.set_timer(timer, 100)
    ciclo = 0

    marcados = []
    tamanho = 4
    vertical = False
    while len(jogador) < 10:
        for barco in jogador:
            for coord in barco:
                if coord not in marcados:
                    marcados.append(coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == timer:
                ciclo += 1

            if event.type == pygame.KEYDOWN :               
                if event.key == pygame.K_x:
                    vertical = not vertical

            posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
            
            if vertical: 
                
                if not colisaoY(marcados,posicao,tamanho) and posicao[1]+tamanho <= 10 :
                    marcar(posicao[0],posicao[1],tamanho,vertical,jogador,ciclo)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        jogador.append(colocarY(posicao[0],posicao[1],tamanho))
                        if len(jogador) in [1,3,6]:
                            tamanho -= 1
                        
                            
                elif posicao[1] in range(11-tamanho,11) and not colisaoY(marcados,(posicao[0],10-tamanho),tamanho) :
                    marcar(posicao[0],10-tamanho,tamanho,vertical,jogador,ciclo)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        jogador.append(colocarY(posicao[0],10-tamanho,tamanho))
                        if len(jogador) in [1,3,6]:
                            tamanho -= 1

                elif colisaoY(marcados,posicao,tamanho):
                    construir_grid(pygame.display.get_surface(),1000,ciclo,jogador)
                    pygame.display.flip()

            else:
                
                if not colisaoX(marcados,posicao,tamanho) and posicao[0] in range(11-tamanho) :
                        marcar(posicao[0],posicao[1],tamanho,vertical,jogador,ciclo)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            jogador.append(colocarX(posicao[0],posicao[1],tamanho))
                            if len(jogador) in [1,3,6]:
                                tamanho -= 1
                            
                elif posicao[0] in range(11-tamanho,11) and not colisaoX(marcados,(10-tamanho,posicao[1]),tamanho):
                    marcar(10-tamanho,posicao[1],tamanho,vertical,jogador,ciclo)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        jogador.append(colocarX(10-tamanho,posicao[1],tamanho))
                        if len(jogador) in [1,3,6]:
                            tamanho -=1

                elif colisaoX(marcados,posicao,tamanho):
                    construir_grid(pygame.display.get_surface(),1000,ciclo,jogador)
                    pygame.display.flip()

    return jogador
    
if __name__ == "__main__":
    pygame.init()
    tela=pygame.display.set_mode((1000,1000))
    construir_grid(tela,1000,0)
    pygame.display.flip()
    while True:
        for event in pygame.event.get(): 
            if event.type ==  pygame.QUIT:
                pygame.quit()
                exit()
            print(posicionar())

