from graphics import *
import copy

class Board:

    CELL_HEIGHT_WIDTH = 30;

    # 0 = empty space
    # 1 = snake head
    # 2 = snake tail
    # 3 = fruit

    def __init__(self, columns, rows):
        self.columns = columns;
        self.rows = rows;
        self.top_left = Point(0,0)
        self.bottom_right = Point(
        ((columns * self.CELL_HEIGHT_WIDTH)),
        ((columns * self.CELL_HEIGHT_WIDTH))
        )

        self.drawn = False

    def draw_board(self, graph):
        if not self.drawn:
            self.board_background = Rectangle(self.top_left, self.bottom_right)
            self.board_background.setFill('white')
            self.board_background.draw(graph)
            for x in range(self.columns):
                for y in range(self.rows):
                    cell = Rectangle(
                                Point(((x * self.CELL_HEIGHT_WIDTH)), ((y * self.CELL_HEIGHT_WIDTH))),
                                Point((((x + 1) * self.CELL_HEIGHT_WIDTH)), (((y + 1) * self.CELL_HEIGHT_WIDTH)))
                            )
                    cell.draw(graph)
            self.drawn = True
