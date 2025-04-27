
import pygame
barco1=pygame.image.load("imagens/barco1.png")
barco2_v=pygame.image.load("imagens/barco2_v.png")
barco2_h=pygame.image.load("imagens/barco2_h.png")
barco3_v=pygame.image.load("imagens/barco3_v.png")
barco3_h=pygame.image.load("imagens/barco3_h.png")
barco4_h=pygame.image.load("imagens/barco4_h.png")
barco4_v=pygame.image.load("imagens/barco4_v.png")
mar = [pygame.transform.scale(pygame.image.load("imagens/aguaspt01.png"),(100,100)),
    pygame.transform.scale(pygame.image.load("imagens/aguaspt02.png"),(100,100)),
    pygame.transform.scale(pygame.image.load("imagens/aguaspt03.png"),(100,100)),
    pygame.transform.scale(pygame.image.load("imagens/aguaspt04.png"),(100,100))]
nuvem = [pygame.transform.scale(pygame.image.load("imagens/nuvem01.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem02.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem03.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem04.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem05.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem06.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem07.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem08.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem09.png"),(100,100)),
         pygame.transform.scale(pygame.image.load("imagens/nuvem10.png"),(100,100)),]

def construir_grid(tela,largura,repeticao,barcos = []):
    coordenadas = []
    for barco in barcos:
        for lugar in barco:
            if lugar not in coordenadas:
                coordenadas.append(lugar)
        
    for xey in range(0,largura,100):
        for i in range(0,largura,100):
            
            tela.blit(mar[repeticao%4],(xey,i))
            pygame.draw.rect(tela,(0,0,0),(xey,i,100,100),(2))

    if len(barcos) > 0:
        for barco in barcos:
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
    
            
    





