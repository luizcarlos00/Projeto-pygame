
import pygame

def construir_grid(tela,largura):
    pygame.draw.rect(tela,(0,0,0),(198,0,2,1000),)
    for xey in range(200,largura,100):
        for i in range(0,largura,100):
            pygame.draw.rect(tela,(0,0,0),(xey,i,100,100),(2))
    pygame.display.flip()
            
    





