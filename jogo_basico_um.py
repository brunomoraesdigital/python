import pygame

# Inicializa o Pygame
pygame.init()

# Cria a janela do jogo
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Primeiro Joguinho em Python")

# Define as cores
cor_fundo = (0, 0, 0)
cor_quadrado = (0, 255, 0)

# Posição inicial do quadrado
x = 100
y = 100
tamanho = 50
velocidade = 5

# Relógio para controlar FPS
relogio = pygame.time.Clock()

# Loop principal do jogo 
rodando = True
while rodando: 

    relogio.tick(60) # limita a 60 FPS

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and x > 0:
        x -= velocidade
    if teclas[pygame.K_RIGHT] and x < largura - tamanho:
        x += velocidade
    if teclas[pygame.K_UP] and y > 0:
        y -= velocidade
    if teclas[pygame.K_DOWN] and y < altura - tamanho:
        y += velocidade
        
    # Atualiza a tela
    tela.fill(cor_fundo)
    pygame.draw.rect(tela, cor_quadrado, (x, y, tamanho, tamanho))
    pygame.display.update()

# Encerra o Pygame
pygame.quit()

