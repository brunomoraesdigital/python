import pygame
import random

# Inicializa o Pygame
pygame.init()

# Tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Coletando Frutas Saudáveis")

# Cores
cor_fundo = (0, 0, 0)

# Personagem
personagem = pygame.image.load("personagem.png")
tamanho = 50
personagem = pygame.transform.scale(personagem, (tamanho, tamanho))
x = 100
y = 100
velocidade = 5

# Fruta
fruta = pygame.image.load("fruta-boa.png")
fruta = pygame.transform.scale(fruta, (40, 40))
fruta_x = random.randint(0, largura - 40)
fruta_y = random.randint(0, altura - 40)

# Pontuação
pontos = 0
fonte = pygame.font.SysFont("Arial", 30)

# Relógio de FPS
relogio = pygame.time.Clock()

# Loop do jogo
rodando = True
while rodando:
    relogio.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and x > 0:
        x -= velocidade
    if teclas[pygame.K_RIGHT] and x < largura - tamanho:
        x += velocidade
    if teclas[pygame.K_UP] and y > 0:
        y -= velocidade
    if teclas[pygame.K_DOWN] and y < altura - tamanho:
        y += velocidade

    # Retângulos para colisão
    ret_personagem = pygame.Rect(x, y, tamanho, tamanho)
    ret_fruta = pygame.Rect(fruta_x, fruta_y, 40, 40)

    # Colisão
    if ret_personagem.colliderect(ret_fruta):
        pontos += 1
        fruta_x = random.randint(0, largura - 40)
        fruta_y = random.randint(0, altura - 40)

    # Desenhar tudo
    tela.fill(cor_fundo)
    tela.blit(personagem, (x, y))
    tela.blit(fruta, (fruta_x, fruta_y))

    # Mostrar pontos
    texto = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
    tela.blit(texto, (10, 10))

    pygame.display.update()

pygame.quit()
