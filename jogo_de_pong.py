import pygame

# Inicializa o Pygame
pygame.init()

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Tamanho da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pong Game")

# Definindo as configurações
raquete_largura = 15
raquete_altura = 100
bola_raio = 10

# Velocidade da bola e das raquetes
velocidade_raquete = 10
velocidade_bola_x = 7
velocidade_bola_y = 7

# Função para desenhar a raquete
def desenhar_raquete(x, y):
    pygame.draw.rect(tela, BRANCO, [x, y, raquete_largura, raquete_altura])

# Função para desenhar a bola
def desenhar_bola(x, y):
    pygame.draw.circle(tela, BRANCO, (x, y), bola_raio)

# Função para desenhar o placar
def desenhar_placar(pontos_jogador1, pontos_jogador2):
    fonte = pygame.font.SysFont("comicsansms", 30)
    texto_pontos = fonte.render(f"Jogador 1: {pontos_jogador1} | Jogador 2: {pontos_jogador2}", True, BRANCO)
    tela.blit(texto_pontos, [largura_tela / 3, 20])

# Função principal do jogo
def jogo():
    # Posições iniciais
    x_raquete1 = 30
    y_raquete1 = altura_tela // 2 - raquete_altura // 2
    x_raquete2 = largura_tela - 30 - raquete_largura
    y_raquete2 = altura_tela // 2 - raquete_altura // 2
    x_bola = largura_tela // 2
    y_bola = altura_tela // 2
    velocidade_y_bola = velocidade_bola_y
    velocidade_x_bola = velocidade_bola_x

    pontos_jogador1 = 0
    pontos_jogador2 = 0

    # Loop principal do jogo
    rodando = True
    while rodando:
        tela.fill(PRETO)

        # Verificar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Movimentação das raquetes
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and y_raquete1 > 0:
            y_raquete1 -= velocidade_raquete
        if teclas[pygame.K_s] and y_raquete1 < altura_tela - raquete_altura:
            y_raquete1 += velocidade_raquete
        if teclas[pygame.K_UP] and y_raquete2 > 0:
            y_raquete2 -= velocidade_raquete
        if teclas[pygame.K_DOWN] and y_raquete2 < altura_tela - raquete_altura:
            y_raquete2 += velocidade_raquete

        # Movimentação da bola
        x_bola += velocidade_x_bola
        y_bola += velocidade_y_bola

        # Colisão com a parte superior e inferior da tela
        if y_bola <= 0 or y_bola >= altura_tela:
            velocidade_y_bola = -velocidade_y_bola

        # Colisão com as raquetes
        if x_bola <= x_raquete1 + raquete_largura and y_raquete1 <= y_bola <= y_raquete1 + raquete_altura:
            velocidade_x_bola = -velocidade_x_bola
        elif x_bola >= x_raquete2 - bola_raio and y_raquete2 <= y_bola <= y_raquete2 + raquete_altura:
            velocidade_x_bola = -velocidade_x_bola

        # Marcar ponto quando a bola sai da tela
        if x_bola < 0:
            pontos_jogador2 += 1
            x_bola = largura_tela // 2
            y_bola = altura_tela // 2
            velocidade_x_bola = -velocidade_x_bola

        if x_bola > largura_tela:
            pontos_jogador1 += 1
            x_bola = largura_tela // 2
            y_bola = altura_tela // 2
            velocidade_x_bola = -velocidade_x_bola

        # Desenhar os elementos
        desenhar_raquete(x_raquete1, y_raquete1)
        desenhar_raquete(x_raquete2, y_raquete2)
        desenhar_bola(x_bola, y_bola)
        desenhar_placar(pontos_jogador1, pontos_jogador2)

        # Atualizar a tela
        pygame.display.update()

        # Controlar a taxa de atualização do jogo
        pygame.time.Clock().tick(60)

    pygame.quit()

# Rodar o jogo
jogo()
