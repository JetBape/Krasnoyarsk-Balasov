import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 70
        self.top = 20
        self.cell_size = 50
        self.bottom = 20 + self.cell_size * self.height
        self.right = 70 + self.cell_size * self.width

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        t = []
        for h in range(self.height):
            for w in range(self.width):
                sell_w = 1
                if self.board[6][4] != 0:
                    print(self.board)
                    print(w, h)
                    sell_w = self.board[w][h][2]
                pygame.draw.rect(screen, 'white',
                                 pygame.Rect(self.left + self.cell_size * w,
                                             self.top + self.cell_size * h,
                                             self.cell_size, self.cell_size), sell_w)
                t.append((self.left + self.cell_size * w, self.top + self.cell_size * h, sell_w))
            self.board[h] = t
            t = []

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell):
        print(cell)
        if cell is not None:
            cur_left = self.left + cell[0] * self.cell_size
            cur_top = self.top + cell[1] * self.cell_size
            for x in range(self.height):
                for y in range(self.width):
                    if self.board[x][y][0] == cur_left:
                        if self.board[x][y][2] == 1:
                            self.board[x][y][2] = None
                        else:
                            self.board[x][y][2] = 1

    def get_cell(self, mouse_pos):
        x_m, y_m = mouse_pos
        res = 0
        if self.left <= x_m <= self.right and self.top <= y_m <= self.bottom:
            for x in range(self.height):
                for y in range(self.width):
                    if self.board[x][y][0] <= x_m <= self.board[x][y][0] + self.cell_size \
                            and self.board[x][y][1] <= y_m <= self.board[x][y][1] + self.cell_size:
                        return x, y

        else:
            return None


if __name__ == '__main__':
    pygame.init()
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    screen.fill('black')

    board = Board(5, 7)
    running = True
    check_m_pos = False
    pos_ = ()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                check_m_pos = True
                pos_ = event.pos

        screen.fill((0, 0, 0))
        board.render()

        if check_m_pos:
            board.get_click(pos_)
            check_m_pos = False
        pygame.display.flip()
