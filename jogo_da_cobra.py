import pygame
import time
import random

# Inicializando o Pygame
pygame.init()

# Definindo as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (213, 50, 80)
AZUL = (50, 153, 213)
CINZA = (200, 200, 200)

# Configurações da tela
largura_tela = 600
altura_tela = 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

# Configurações do relógio
clock = pygame.time.Clock()
velocidade = 15  # A velocidade da cobra

# Definindo o tamanho do bloco da cobra
tamanho_bloco = 10

# Fonte para o texto
fonte = pygame.font.SysFont("bahnschrift", 25)

# Função para mostrar a pontuação
def mostrar_pontuacao(pontos):
    valor = fonte.render("Pontuação: " + str(pontos), True, BRANCO)
    tela.blit(valor, [0, 0])

# Função para a cobra
def desenhar_cobra(tamanho_bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, VERDE, [x[0], x[1], tamanho_bloco, tamanho_bloco])

# Função principal do jogo
def jogo():
    game_over = False
    fim_de_jogo = False

    # Posições iniciais da cobra
    x_cobra = largura_tela / 2
    y_cobra = altura_tela / 2

    # Direção inicial da cobra
    x_mudar = 0
    y_mudar = 0

    # Lista para a cobra
    corpo_cobra = []
    comprimento_cobra = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 10.0) * 10.0

    # Loop principal do jogo
    while not game_over:

        while fim_de_jogo:
            tela.fill(AZUL)
            mensagem = fonte.render("Fim de Jogo! Pressione C para jogar novamente ou Q para sair", True, VERMELHO)
            tela.blit(mensagem, [largura_tela / 6, altura_tela / 3])
            mostrar_pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True
                    fim_de_jogo = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        fim_de_jogo = False
                    if evento.key == pygame.K_c:
                        jogo()

        # Lidar com os eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudar = -tamanho_bloco
                    y_mudar = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudar = tamanho_bloco
                    y_mudar = 0
                elif evento.key == pygame.K_UP:
                    y_mudar = -tamanho_bloco
                    x_mudar = 0
                elif evento.key == pygame.K_DOWN:
                    y_mudar = tamanho_bloco
                    x_mudar = 0

        # Verificar se a cobra bateu nas bordas
        if x_cobra >= largura_tela or x_cobra < 0 or y_cobra >= altura_tela or y_cobra < 0:
            fim_de_jogo = True
        x_cobra += x_mudar
        y_cobra += y_mudar
        tela.fill(AZUL)

        # Desenhar a comida
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        # Atualizar a lista da cobra
        corpo_cobra.append([x_cobra, y_cobra])
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]

        # Verificar se a cobra colidiu com ela mesma
        for x in corpo_cobra[:-1]:
            if x == [x_cobra, y_cobra]:
                fim_de_jogo = True

        desenhar_cobra(tamanho_bloco, corpo_cobra)
        mostrar_pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        # Verificar se a cobra comeu a comida
        if x_cobra == comida_x and y_cobra == comida_y:
            comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 10.0) * 10.0
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

# Rodar o jogo
jogo()
