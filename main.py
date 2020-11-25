import pygame

try:
    w, n = map(int, input().split())
except Exception:
    print('Неправильный формат ввода')
    exit(0)


def draw():
    screen.fill((0, 0, 0))
    color = ()
    for i in range(1, n + 1):
        if i % 2 == 0 or i == 1:
            color = (255, 0, 0)
        elif i % 3 == 0:
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)

        pygame.draw.circle(screen, color, (w * n, w * n), (n + 1 - i) * w)



if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = w * n * 2, w * n * 2
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
