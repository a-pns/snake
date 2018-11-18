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
        self.board_state = self.new_board_state()


    def draw_board(self, graph):

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

    def new_board_state(self):
        return [[0] * self.columns] * self.rows;

    def add_fruit(self, fruit, persist = True):
        if persist:
            the_board = self.board_state
        else:
            the_board = copy.deepcopy(self.board_state)
        the_board[fruit.x][fruit.y] = 3
        if not persist:
            return the_board

    def add_snake(self, snake, persist = True):
        # 0 = x
        # 1 = y
        # 2 = is snake body part (head or tail)

        if persist:
            the_board = self.board_state
        else:
            the_board = copy.deepcopy(self.board_state)
        for part in snake.body_parts:
            the_board[part.x][part.y] = part.body_type
        if not persist:
            return the_board
