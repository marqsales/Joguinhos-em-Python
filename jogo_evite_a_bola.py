import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Evite os Blocos!')

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Configurações do jogador
raio_jogador = 20
x_jogador = largura_tela // 2
y_jogador = altura_tela - 50
velocidade_jogador = 5

# Configurações dos obstáculos
largura_obstaculo = 50
altura_obstaculo = 30
velocidade_obstaculo = 5
obstaculos = []

# Função para desenhar o jogador
def desenhar_jogador(x, y):
    pygame.draw.circle(tela, AZUL, (x, y), raio_jogador)

# Função para desenhar os obstáculos
def desenhar_obstaculos(obstaculos):
    for obstaculo in obstaculos:
        pygame.draw.rect(tela, VERMELHO, obstaculo)

# Função para criar um novo obstáculo
def criar_obstaculo():
    x = random.randint(0, largura_tela - largura_obstaculo)
    y = -altura_obstaculo
    return pygame.Rect(x, y, largura_obstaculo, altura_obstaculo)

# Função principal do jogo
def jogo():
    global x_jogador
    global y_jogador

    # Loop principal do jogo
    rodando = True
    clock = pygame.time.Clock()

    while rodando:
        tela.fill(BRANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Movimentação do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and x_jogador > raio_jogador:
            x_jogador -= velocidade_jogador
        if teclas[pygame.K_RIGHT] and x_jogador < largura_tela - raio_jogador:
            x_jogador += velocidade_jogador

        # Criar obstáculos
        if random.randint(1, 30) == 1:
            obstaculos.append(criar_obstaculo())

        # Mover obstáculos
        for obstaculo in obstaculos[:]:
            obstaculo.y += velocidade_obstaculo
            if obstaculo.y > altura_tela:
                obstaculos.remove(obstaculo)

            # Colisão com o jogador
            if obstaculo.colliderect(pygame.Rect(x_jogador - raio_jogador, y_jogador - raio_jogador, 2 * raio_jogador, 2 * raio_jogador)):
                rodando = False  # Fim de jogo

        # Desenhar tudo
        desenhar_jogador(x_jogador, y_jogador)
        desenhar_obstaculos(obstaculos)

        # Atualizar a tela
        pygame.display.update()

        # Controlar a taxa de quadros
        clock.tick(60)

    # Exibir "Game Over"
    fonte = pygame.font.Font(None, 74)
    texto = fonte.render("Game Over", True, VERDE)
    tela.blit(texto, (largura_tela // 3, altura_tela // 3))
    pygame.display.update()

    # Esperar para o jogador ver o "Game Over"
    pygame.time.wait(2000)

    # Fechar o Pygame
    pygame.quit()

# Rodar o jogo
jogo()
