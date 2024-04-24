import pygame
import sys
import random
import requests
from io import BytesIO

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 2000, 1100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Efeitos Psicodélicos")

# Função para gerar cor aleatória
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Classe para representar um círculo
class Circle:
    def __init__(self):
        self.radius = random.randint(10, 50)
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.color = random_color()
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Lista para armazenar os círculos
circles = [Circle() for _ in range(10)]

# Contador para o efeito de glitch
glitch_count = 0

# URLs das imagens de erro
error_image_urls = [
    "https://compumake.com.br/wp-content/uploads/2020/06/Falha-no-Windows-faz-computador-reiniciar-sozinho.png",
    "https://s2-techtudo.glbimg.com/mw4q-49-XcfPOFaHjJenMn7gtlY=/0x0:695x521/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2021/o/f/l7au59TTCc6ySijKjXAQ/2014-03-19-telaazul1.jpg",
    "https://compumake.com.br/wp-content/uploads/2020/06/Falha-no-Windows-faz-computador-reiniciar-sozinho.png"
]

# Carrega as imagens de erro
error_images = []
for url in error_image_urls:
    response = requests.get(url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        error_images.append(pygame.image.load(image_data))

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpa a tela
    screen.fill((0, 0, 0))

    # Desenha e move os círculos
    for circle in circles:
        circle.move()
        circle.draw(screen)

    # Efeito de luz piscando
    if random.random() < 0.02:  # Ajuste a frequência piscante conforme desejado
        pygame.draw.rect(screen, random_color(), (0, 0, WIDTH, HEIGHT))

    # Efeito de glitch
    if glitch_count < 20:  # Ajuste a intensidade do glitch conforme desejado
        screen.fill(random_color())
        glitch_count += 1
    else:
        glitch_count = 0
        # Exibe uma imagem de erro aleatória
        error_image = random.choice(error_images)
        error_width = error_image.get_width()
        error_height = error_image.get_height()

        # Verifica se a largura da imagem é maior que a largura da tela
        if error_width > WIDTH:
            error_width = WIDTH  # Define a largura da imagem como a largura da tela

        # Verifica se a altura da imagem é maior que a altura da tela
        if error_height > HEIGHT:
            error_height = HEIGHT  # Define a altura da imagem como a altura da tela

        error_x = random.randint(0, WIDTH - error_width)
        error_y = random.randint(0, HEIGHT - error_height)
        screen.blit(error_image, (error_x, error_y))

    # Atualiza a tela
    pygame.display.flip()

    # Limita a taxa de quadros por segundo
    pygame.time.Clock().tick(30)
