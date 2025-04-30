import pygame
import random

pygame.init()

# Tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Coletando Frutas com Perigo!")

# Cores
cor_fundo = (0, 0, 0)

# Personagem
personagem = pygame.image.load("personagem.png")
tamanho = 50
personagem = pygame.transform.scale(personagem, (tamanho, tamanho))
x = 100
y = 100
velocidade = 5

# Fruta boa
fruta_boa = pygame.image.load("fruta-boa.png")
fruta_boa = pygame.transform.scale(fruta_boa, (40, 40))
fruta_boa_x = random.randint(0, largura - 40)
fruta_boa_y = random.randint(0, altura - 40)

# Fruta ruim
fruta_ruim = pygame.image.load("fruta-ruim.png")
fruta_ruim = pygame.transform.scale(fruta_ruim, (40, 40))
fruta_ruim_x = random.randint(0, largura - 40)
fruta_ruim_y = random.randint(0, altura - 40)

# Pontos
pontos = 0
fonte = pygame.font.SysFont("Arial", 30)

# Relógio
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

    # Retângulos
    ret_personagem = pygame.Rect(x, y, tamanho, tamanho)
    ret_boa = pygame.Rect(fruta_boa_x, fruta_boa_y, 40, 40)
    ret_ruim = pygame.Rect(fruta_ruim_x, fruta_ruim_y, 40, 40)

    # Colisão com fruta-boa
    if ret_personagem.colliderect(ret_boa):
        pontos += 1
        fruta_boa_x = random.randint(0, largura - 40)
        fruta_boa_y = random.randint(0, altura - 40)
        fruta_ruim_x = random.randint(0, largura - 40)
        fruta_ruim_y = random.randint(0, altura - 40)

    # Colisão com fruta-ruim
    if ret_personagem.colliderect(ret_ruim):
        print("Fim de jogo! Você pegou a fruta ruim.")
        rodando = False

    # Desenhar
    tela.fill(cor_fundo)
    tela.blit(personagem, (x, y))
    tela.blit(fruta_boa, (fruta_boa_x, fruta_boa_y))
    tela.blit(fruta_ruim, (fruta_ruim_x, fruta_ruim_y))

    texto = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
    tela.blit(texto, (10, 10))

    pygame.display.update()

pygame.quit()
