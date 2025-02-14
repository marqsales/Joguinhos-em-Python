import pygame
import random

# Inicializa o Pygame
pygame.init()

# Definir cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

# Definindo tamanho da tela e tamanho dos blocos
LARGURA_TELA = 600
ALTURA_TELA = 600
TAMANHO_BLOCO = 30
LARGURA_LABIRINTO = LARGURA_TELA // TAMANHO_BLOCO
ALTURA_LABIRINTO = ALTURA_TELA // TAMANHO_BLOCO

# Criar a tela
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Jogo de Labirinto')

# Fonte para o texto
fonte = pygame.font.SysFont("comicsansms", 25)

# Função para desenhar o labirinto
def desenhar_labirinto(labirinto):
    for y in range(len(labirinto)):
        for x in range(len(labirinto[y])):
            if labirinto[y][x] == 1:
                pygame.draw.rect(tela, PRETO, [x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO])
            elif labirinto[y][x] == 2:
                pygame.draw.rect(tela, VERDE, [x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO])
            elif labirinto[y][x] == 3:
                pygame.draw.rect(tela, AZUL, [x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO])

# Função para desenhar o texto
def mostrar_texto(texto, cor, pos):
    mensagem = fonte.render(texto, True, cor)
    tela.blit(mensagem, pos)

# Função para gerar um labirinto simples
def gerar_labirinto():
    labirinto = [[1] * LARGURA_LABIRINTO for _ in range(ALTURA_LABIRINTO)]

    for y in range(1, ALTURA_LABIRINTO - 1, 2):
        for x in range(1, LARGURA_LABIRINTO - 1, 2):
            labirinto[y][x] = 0
            if random.randint(0, 1):
                if x + 1 < LARGURA_LABIRINTO:
                    labirinto[y][x + 1] = 0
                if y + 1 < ALTURA_LABIRINTO:
                    labirinto[y + 1][x] = 0

    # Definir entrada e saída
    labirinto[1][0] = 2  # Posição de início
    labirinto[ALTURA_LABIRINTO - 2][LARGURA_LABIRINTO - 1] = 3  # Posição de saída

    return labirinto

# Função principal do jogo
def jogo():
    # Criando labirinto
    labirinto = gerar_labirinto()

    # Posições do jogador (início)
    x_jogador = 1
    y_jogador = 1

    # Loop do jogo
    rodando = True
    while rodando:
        tela.fill(BRANCO)

        # Desenhar o labirinto
        desenhar_labirinto(labirinto)

        # Verificar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Movimentação do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and labirinto[y_jogador][x_jogador - 1] != 1:
            x_jogador -= 1
        if teclas[pygame.K_RIGHT] and labirinto[y_jogador][x_jogador + 1] != 1:
            x_jogador += 1
        if teclas[pygame.K_UP] and labirinto[y_jogador - 1][x_jogador] != 1:
            y_jogador -= 1
        if teclas[pygame.K_DOWN] and labirinto[y_jogador + 1][x_jogador] != 1:
            y_jogador += 1

        # Desenhar o jogador
        pygame.draw.rect(tela, VERDE, [x_jogador * TAMANHO_BLOCO, y_jogador * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO])

        # Verificar se o jogador chegou à saída
        if labirinto[y_jogador][x_jogador] == 3:
            mostrar_texto("Você venceu!", BRANCO, (LARGURA_TELA // 3, ALTURA_TELA // 3))
            pygame.display.update()
            pygame.time.wait(2000)  # Exibir mensagem de vitória por 2 segundos
            rodando = False

        # Atualizar a tela
        pygame.display.update()

        # Controlar a taxa de atualização
        pygame.time.Clock().tick(30)

    pygame.quit()

# Rodar o jogo
jogo()
