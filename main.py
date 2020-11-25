import pygame

try:
    w, n = map(int, input().split())
except Exception:
    print('Неправильный формат ввода')
    exit(0)


def draw():
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (n * w / 2, n * w / 2), 40, width=10)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = w * n, w * n
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    draw()
    # формирование кадра:
    # команды рисования на холсте
    # ...
    # ...
    # смена (отрисовка) кадра:
    pygame.display.set_caption('Шахматная клетка')
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    # завершение работы:
    pygame.quit()
