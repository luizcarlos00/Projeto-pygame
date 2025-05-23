import pygame
from posiciona import posicionar
from turno import turno


def main():
    pygame.init()

    jogador1 = []
    jogador2 = []
    marcadosJ1 = []
    marcadosJ2 = []
    vencedor = "?"
    condicaoJ1 = []
    condicaoJ2 = []
    jogar = 0
    transicao = pygame.USEREVENT
    cont_transicoes = 0
    executar = True

    tela=pygame.display.set_mode((1000,1000))
    pygame.display.set_icon(pygame.image.load("imagens/icone.png"))
    pygame.display.set_caption("Batalha Naval")

    relogio = pygame.time.Clock()

    tela.blit(pygame.transform.scale(pygame.image.load("imagens/tela_fundo_menu.png"),(1000,1000)),(0,0))
    pygame.display.flip()

    pygame.mixer.music.load("audio/musica_fundo.mp3")
    pygame.mixer.music.play(-1)
    fonte = pygame.font.SysFont("Britannic Bold", 105)
    
    while executar:
        relogio.tick(60)
        for event in pygame.event.get(): 
            if event.type== pygame.QUIT:
                pygame.quit()
                exit()

            if jogar == 0 :
                
                if event.type == pygame.MOUSEBUTTONDOWN :
                    if (pygame.mouse.get_pos()[0]//100) <= 2 and (pygame.mouse.get_pos()[1]//100) == 8:
                            tela.blit(pygame.transform.scale(pygame.image.load("imagens/J1_posiciona.png"),(1000,1000)),(0,0))
                            pygame.time.set_timer(transicao, 1500,1)
                            cont_transicoes += 1
                            pygame.display.flip()
                    if (pygame.mouse.get_pos()[0]//100) <= 2 and (pygame.mouse.get_pos()[1]//100) <= 96 and (pygame.mouse.get_pos()[1]//10) >= 90 :
                            jogar = 5

                if event.type == transicao:
                    pygame.mixer.music.load("audio/musica_planos.mp3")
                    pygame.mixer.music.play(-1)
                    jogar = 1

                    
            if jogar==5:
                tela.blit(pygame.transform.scale(pygame.image.load("imagens/fundo_instruções.png"),(1000,1000)),(0,0))
                pygame.display.flip()

                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        jogar=0
                        tela.blit(pygame.transform.scale(pygame.image.load("imagens/tela_fundo_menu.png"),(1000,1000)),(0,0))
                        pygame.display.flip()
                
            if jogar==1:
                if jogador1 == []:

                    jogador1 = posicionar(jogador1)
                    tela.blit(pygame.transform.scale(pygame.image.load("imagens/J2_posiciona.png"),(1000,1000)),(0,0))
                    transicao = pygame.USEREVENT + cont_transicoes
                    pygame.time.set_timer(transicao,1500,1)
                    cont_transicoes += 1

                if event.type == transicao:
                    jogador2 = posicionar(jogador2) 
                    tela.blit(pygame.transform.scale(pygame.image.load("imagens/J1_vez.png"),(1000,1000)),(0,0))
                    transicao = pygame.USEREVENT + cont_transicoes
                    pygame.time.set_timer(transicao,1500,1)
                    cont_transicoes += 1
                    pygame.display.flip()
                    pygame.mixer.music.load("audio/musica_fundo.mp3")   
                    pygame.mixer.music.play(-1)         
                    jogar = 2

                
            
                
                            
            if jogar == 2:
                if event.type == transicao:
                    while vencedor == "?":
                        jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2 = turno(jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2)

                        if len(condicaoJ1) == 10:
                            vencedor = "Jogador 01"
                            transicao = pygame.USEREVENT + cont_transicoes
                            pygame.time.set_timer(transicao, 8000,1)
                            cont_transicoes += 1
                            pygame.mixer.music.load("audio/vitoria.mp3")   
                            pygame.mixer.music.play(0)
                        
                        if len(condicaoJ2) == 10:
                            vencedor = "Jogador 02"
                            transicao = pygame.USEREVENT + cont_transicoes
                            pygame.time.set_timer(transicao, 5000,1)
                            cont_transicoes += 1
                            pygame.mixer.music.load("audio/vitoria.mp3")   
                            pygame.mixer.music.play(0)

                if vencedor != "?":
                    texto_vitoria=fonte.render(f"{vencedor}",True,(100,50,255))
                    tela.blit(pygame.transform.scale(pygame.image.load("imagens/fundo_parabéns.png"),(1000,1000)),(0,0))
                    pygame.display.flip()
                    tela.blit(texto_vitoria,(300,450))
                    pygame.display.flip()
                    

                    if event.type == transicao:
                        jogar = 3
            
            if jogar==3:
                tela.blit(pygame.transform.scale(pygame.image.load("imagens/tela_creditos.png"),(1000,1000)),(0,0))
                pygame.display.flip()
                
                if event.type == pygame.KEYDOWN :               
                    if event.key == pygame.K_j:
                        jogar = 0
                        jogador1 = []
                        jogador2 = []
                        marcadosJ1 = []
                        marcadosJ2 = []
                        vencedor = "?"
                        condicaoJ1 = []
                        condicaoJ2 = []
                        pygame.mixer.music.load("audio/musica_fundo.mp3")
                        pygame.mixer.music.play(-1)
                        tela.blit(pygame.transform.scale(pygame.image.load("imagens/tela_fundo_menu.png"),(1000,1000)),(0,0))
                        pygame.display.flip()
    
                


        
       

        pygame.display.flip()


if __name__=="__main__":
    main()
    
