import pygame
from modulo import construir_grid

def marcar(x,y,tam,vertical):
    if vertical:
        construir_grid(pygame.display.get_surface(),1200)
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(x*100,y*100,100,tam*100),(2))
        pygame.display.flip()
    else:
        construir_grid(pygame.display.get_surface(),1200)
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

def colocarX(posX,posY,tam,img):
    selecionados = []
    for x in range(posX,posX+tam):
        selecionados.append((x,posY)) 
    pygame.display.get_surface().blit(img,(posX*100,posY*100))
    pygame.display.flip()
    return selecionados

def colocarY(posX,posY,tam,img):
    selecionados = []
    for y in range(posY,posY+tam):
        selecionados.append((posX,y)) 
    pygame.display.get_surface().blit(img,(posX*100,posY*100))
    pygame.display.flip()
    return selecionados
    
def posicionar( jogador=[]):
    barco1=pygame.image.load("imagens/barco1.png")
    barco2_v=pygame.image.load("imagens/barco2_v.png")
    barco2_h=pygame.image.load("imagens/barco2_h.png")
    barco3_v=pygame.image.load("imagens/barco3_v.png")
    barco3_h=pygame.image.load("imagens/barco3_h.png")
    barco4_h=pygame.image.load("imagens/barco4_h.png")
    barco4_v=pygame.image.load("imagens/barco4_v.png")

    marcados = []
    tamanho = 4
    vertical = False
    while len(jogador) < 10:
        for barco in jogador:
            for coord in barco:
                if coord not in marcados:
                    marcados.append(coord)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN :               
                if event.key == pygame.K_x:
                    vertical = not vertical

            posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
            
            if vertical: 
                if tamanho == 4:
                    imagem = barco4_v
                elif tamanho == 3:
                    imagem = barco3_v
                elif tamanho == 2:
                    imagem = barco2_v
                else:
                    imagem = barco1

                if posicao[0] >= 2 and not colisaoY(marcados,posicao,tamanho) and posicao[1]+tamanho <= 10 :
                    marcar(posicao[0],posicao[1],tamanho,vertical)
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        jogador.append(colocarY(posicao[0],posicao[1],tamanho,imagem))
                        if len(jogador) in [1,3,6]:
                            tamanho -=1
                        
                            
                elif posicao[0] >=2 and posicao[1] in range(11-tamanho,11) and not colisaoY(marcados,(posicao[0],10-tamanho),tamanho) :
                    marcar(posicao[0],10-tamanho,tamanho,vertical)
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        jogador.append(colocarY(posicao[0],10-tamanho,tamanho,imagem))
                        if len(jogador) in [1,3,6]:
                            tamanho -=1

                elif colisaoY(marcados,posicao,tamanho):
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.display.flip()

            else:
                if tamanho == 4:
                    imagem = barco4_h
                elif tamanho == 3:
                    imagem = barco3_h
                elif tamanho == 2:
                    imagem = barco2_h
                else:
                    imagem = barco1

                if posicao[0] in range(2,13-tamanho) and not colisaoX(marcados,posicao,tamanho) :
                        marcar(posicao[0],posicao[1],tamanho,vertical)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            jogador.append(colocarX(posicao[0],posicao[1],tamanho,imagem))
                            if len(jogador) in [1,3,6]:
                                tamanho -=1
                            
                elif posicao[0] in range(13-tamanho,13) and not colisaoX(marcados,(12-tamanho,posicao[1]),tamanho):
                    marcar(12-tamanho,posicao[1],tamanho,vertical)
                    if event.type==pygame.MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                        jogador.append(colocarX(12-tamanho,posicao[1],tamanho,imagem))
                        if len(jogador) in [1,3,6]:
                            tamanho -=1
                elif colisaoX(marcados,posicao,tamanho):
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.display.flip()

    return jogador
    
if __name__ == "__main__":
    pygame.init()
    tela=pygame.display.set_mode((1200,1000))#definição de tela
    construir_grid(tela,1200)
    tela.fill((0,0,255))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():#sair 
            if event.type== pygame.QUIT:
                pygame.quit()
                exit()
            print(posicionar())

