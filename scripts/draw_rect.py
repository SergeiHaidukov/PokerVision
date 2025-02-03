import pygame
import sys
from utils import read_config_file

config = read_config_file()

# Инициализация pygame
pygame.init()

# Устанавливаем размер окна
size = (config['table_size']['width'], config['table_size']['height'])
hero_cards = (config['hero_cards']['x_0'], config['hero_cards']['y_0'], config['hero_cards']['x_1'], config['hero_cards']['y_1'])
table_cards = (config['table_cards']['x_0'], config['table_cards']['y_0'], config['table_cards']['x_1'], config['table_cards']['y_1'])

screen = pygame.display.set_mode(size, pygame.NOFRAME)
pygame.display.set_caption("Прозрачный прямоугольник")

# Устанавливаем прозрачность окна
hwnd = pygame.display.get_wm_info()["window"]
import ctypes
ctypes.windll.user32.SetWindowLongW(hwnd, -20, 0x00080000)
ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, 150, 0x00000002)

# Цвета
BLUE = (0, 0, 255)
GREEN = (50, 100, 50)
TRANSPARENT = (0, 0, 0, 0)

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(TRANSPARENT)

    # Рисуем прямоугольник
    # pygame.draw.rect(screen, BLUE, (50, 50, 100, 100))

    # hero cards
    pygame.draw.rect(screen, GREEN, (hero_cards[0], hero_cards[1], hero_cards[2] - hero_cards[0], hero_cards[3] - hero_cards[1]))

    # table cards
    pygame.draw.rect(screen, GREEN,
                     (table_cards[0], table_cards[1], table_cards[2] - table_cards[0], table_cards[3] - table_cards[1]))

    # Обновление экрана
    pygame.display.flip()

# Выход
pygame.quit()
sys.exit()