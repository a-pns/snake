from graphics import *
from board import *

class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.circle = None
        self.drawn = False

    def set_new_position(self, x, y):
        if self.circle is not None:
            x_diff = (Board.CELL_HEIGHT_WIDTH * x + Board.CELL_HEIGHT_WIDTH/2) - (Board.CELL_HEIGHT_WIDTH * self.x + Board.CELL_HEIGHT_WIDTH/2)
            y_diff = (Board.CELL_HEIGHT_WIDTH * y + Board.CELL_HEIGHT_WIDTH/2) - (Board.CELL_HEIGHT_WIDTH * self.y + Board.CELL_HEIGHT_WIDTH/2)
            self.circle.move(x_diff, y_diff)
        self.x = x
        self.y = y

    def draw(self,board, graph):
        if self.circle is None:
            self.circle = Circle(Point(board.CELL_HEIGHT_WIDTH * self.x + board.CELL_HEIGHT_WIDTH/2, board.CELL_HEIGHT_WIDTH * self.y+ board.CELL_HEIGHT_WIDTH/2), board.CELL_HEIGHT_WIDTH / 2)
            self.circle.setOutline('green')
            self.circle.setFill('green')
        if not self.drawn:
            self.circle.draw(graph)
            self.drawn = True
