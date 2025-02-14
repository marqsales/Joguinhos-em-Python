import pygame
import random
import time

# Inicializar o Pygame
pygame.init()

# Definir cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)

# Configurações da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Atirar em Alvos")

# Definir fontes
fonte_pontos = pygame.font.SysFont("comicsansms", 30)
fonte_fim = pygame.font.SysFont("comicsansms", 50)

# Definir o relógio
clock = pygame.time.Clock()

# Carregar imagens
imagem_tiro = pygame.Surface((10, 20))
imagem_tiro.fill(AMARELO)
imagem_alvo = pygame.Surface((40, 40))
pygame.draw.circle(imagem_alvo, VERDE, (20, 20), 20)

# Função para exibir o texto na tela
def mostrar_texto(texto, fonte, cor, pos):
    mensagem = fonte.render(texto, True, cor)
    tela.blit(mensagem, pos)

# Função para o jogo
def jogo():
    # Posições iniciais
    x_jogador = LARGURA_TELA // 2
    y_jogador = ALTURA_TELA - 50
    velocidade_jogador = 7

    tiros = []
    alvos = []

    pontos = 0

    # Criar o alvo
    def criar_alvo():
        x_alvo = random.randint(50, LARGURA_TELA - 50)
        y_alvo = random.randint(50, 200)
        return [x_alvo, y_alvo]

    # Adicionar um alvo ao jogo
    alvos.append(criar_alvo())

    # Loop do jogo
    rodando = True
    while rodando:
        tela.fill(PRETO)

        # Checar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Movimentar o jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and x_jogador > 0:
            x_jogador -= velocidade_jogador
        if teclas[pygame.K_RIGHT] and x_jogador < LARGURA_TELA - 50:
            x_jogador += velocidade_jogador

        # Disparar tiros
        if teclas[pygame.K_SPACE]:
            tiros.append([x_jogador + 20, y_jogador])

        # Movimentar tiros
        for tiro in tiros[:]:
            tiro[1] -= 10  # A bala sobe
            if tiro[1] < 0:  # Remover bala fora da tela
                tiros.remove(tiro)

        # Desenhar os elementos
        pygame.draw.rect(tela, AZUL, [x_jogador, y_jogador, 50, 50])  # Jogador

        # Desenhar os alvos
        for alvo in alvos[:]:
            tela.blit(imagem_alvo, (alvo[0] - 20, alvo[1] - 20))

        # Desenhar os tiros
        for tiro in tiros:
            tela.blit(imagem_tiro, (tiro[0], tiro[1]))

        # Verificar colisões
        for tiro in tiros[:]:
            for alvo in alvos[:]:
                if alvo[0] - 20 < tiro[0] < alvo[0] + 20 and alvo[1] - 20 < tiro[1] < alvo[1] + 20:
                    alvos.remove(alvo)
                    tiros.remove(tiro)
                    pontos += 1
                    alvos.append(criar_alvo())  # Criar novo alvo

        # Exibir pontuação
        mostrar_texto(f"Pontos: {pontos}", fonte_pontos, BRANCO, (10, 10))

        # Se não tiver mais alvos, o jogo acaba
        if len(alvos) == 0:
            mostrar_texto("Você venceu!", fonte_fim, AMARELO, (LARGURA_TELA // 3, ALTURA_TELA // 3))
            pygame.display.update()
            time.sleep(2)
            rodando = False

        pygame.display.update()
        clock.tick(60)  # Controlar FPS

    pygame.quit()

# Iniciar o jogo
jogo()
