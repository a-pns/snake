from graphics import *

class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self,board, graph):
        cir = Circle(Point(board.CELL_HEIGHT_WIDTH * self.x + board.CELL_HEIGHT_WIDTH/2, board.CELL_HEIGHT_WIDTH * self.y+ board.CELL_HEIGHT_WIDTH/2), board.CELL_HEIGHT_WIDTH / 2)
        cir.setOutline('green')
        cir.setFill('green')
        cir.draw(graph)
