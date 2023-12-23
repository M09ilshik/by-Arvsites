import pygame
import sys

pygame.init()

# Определяем цвета
WHITE = (255, 255, 255)

# Создаем окно
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Ввод текста через Pygame")

# Загружаем шрифт
font = pygame.font.Font(None, 36)

text = ''
input_box = pygame.Rect(100, 100, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False

# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Если клик по input_box
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    # Выполняем какие-то действия с текстом
                    print(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.fill(WHITE)
    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, color, input_box, 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
