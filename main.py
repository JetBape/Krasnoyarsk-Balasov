import pygame

try:
    x, n = map(int, input().split())
except Exception:
    print('Неправильный формат ввода')
    exit(0)


def draw():
    screen.fill((255, 255, 255))
    cnt = x / n
    color = ()
    for i in range(n):
        if i % 2 == 0:
            color = (0, 0, 0)
            for j in range(n):
                if i % 2 == 0:
                    color = (0, 0, 0)
                    pygame.draw.rect(screen, )




if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = x, x
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
