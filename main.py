import pygame


def draw():
    pygame.draw.rect(screen, 'green', pygame.Rect(1, 1, 50, 50))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = width, height = 1000, 400
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))

    fps = 100
    clock = pygame.time.Clock()
    running = True
    move_circles = False
    circles = []
    x, y = 0, 0
    v = 100
    pos = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                circles.append(event.pos)
                x, y = event.pos
                pos = 0
                move_circles = True
        if move_circles:
            for circle in circles:
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, 'white', (circle[0] - pos, circle[1] - pos), 10)
                pos += v / fps

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
