import pygame


def draw():
    pygame.draw.rect(screen, 'green', pygame.Rect(1, 1, 50, 50))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = width, height = 1000, 400
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 255))
    draw()

    fps = 60
    clock = pygame.time.Clock()
    running = True
    movement = False
    r = 1
    x_min = 1
    y_min = 1
    rt = False
    x = 0
    y = 0
    v = 10
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if x_min <= event.pos[0] <= x_min + 50 and y_min <= event.pos[1] <= y_min + 50:
                    rt = True
                    x, y = event.pos
            elif event.type == pygame.MOUSEMOTION and rt:
                movement = True
        if movement:
            pygame.draw.rect(screen, 'yellow', pygame.Rect(1 + , 1, 50, 50))
            r += v / fps
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
