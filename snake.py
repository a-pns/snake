from graphics import *
from board import *
import copy


class Direction():
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    def __str__(self):
        if self == Direction.LEFT:
            return "LEFT"
        if self == Direction.RIGHT:
            return "RIGHT"
        if self == Direction.UP:
            return "UP"
        if self == Direction.DOWN:
            return "DOWN"

    def __repr__(self):
        return self.__str__()

class Snake:

    def __init__(self, start_x, start_y):
        self.body_parts = [SnakeBodyPart(start_x,start_y,1)]
        self.direction = Direction.DOWN;

    def change_direction(self, new_direction):
        self.direction = new_direction

    def has_eaten(self, fruit, body_parts = None):
        if body_parts is None:
            body_parts = self.body_parts;
        head = body_parts[0]
        return head.x == fruit.x and head.y == fruit.y

    def move(self,fruit, do_move = True, direction = None):
        if direction is None:
            direction = self.direction
        if not do_move:
            old_position = copy.deepcopy(self.body_parts)
        else:
            old_position = self.body_parts
        temp_body_parts = []
        i = 0
        old_x = 0
        old_y = 0
        for i in range(len(self.body_parts)):
            part = old_position[i]
            if part.body_type == 1:
                # if head then move 1 place in 1 direction
                old_x = part.x
                old_y = part.y
                part.set_new_position(part.x + direction[0], part.y + direction[1])
                temp_body_parts.append(part)
            else:
                # if not head then take place of pre-ceeding body part
                temp_old_x = part.x
                temp_old_y = part.y
                part.set_new_position(old_x, old_y)
                temp_body_parts.append(part)
                old_x = temp_old_x
                old_y = temp_old_y
        if self.has_eaten(fruit, temp_body_parts) and do_move:
            temp_body_parts.append(SnakeBodyPart(old_x, old_y, 2))
        if do_move:
            self.body_parts = temp_body_parts
        else:
            return temp_body_parts

    def draw(self,board, graph):
        for part in self.body_parts:
            part.draw(board, graph)

    def is_dead(self, board):
        head = self.body_parts[0]
        if head.x >= board.columns or head.x < 0 or head.y >= board.rows or head.y < 0:
            return True;
        for part in self.body_parts:
            if part.body_type == 2 and part.x == head.x and part.y == head.y:
                return True
        return False

    def head(self):
        return self.body_parts[0]

    def contains_pos(self, x, y):
        for part in self.body_parts:
            if part.x == x and part.y == y:
                return True
        return False

    def __str__(self):
        return ", ".join(str(part) for part in self.body_parts)

    def __repr__(self):
        return self.__str__()


class SnakeBodyPart:
    def __init__(self, x, y, body_type):
        self.x = x;
        self.y = y;
        self.body_type = body_type
        self.circle = None
        self.drawn = False

    def __str__(self):
        return "{x},{y},{t}".format(x=self.x,y=self.y,t=self.body_type)

    def __repr__(self):
        return self.__str__()

    def set_new_position(self, x, y):
        if self.circle is not None:
            x_diff = (Board.CELL_HEIGHT_WIDTH * x + Board.CELL_HEIGHT_WIDTH/2) - (Board.CELL_HEIGHT_WIDTH * self.x + Board.CELL_HEIGHT_WIDTH/2)
            y_diff = (Board.CELL_HEIGHT_WIDTH * y + Board.CELL_HEIGHT_WIDTH/2) - (Board.CELL_HEIGHT_WIDTH * self.y + Board.CELL_HEIGHT_WIDTH/2)
            self.circle.move(x_diff, y_diff)
        self.x = x
        self.y = y

    def draw(self, board, graph):
        if self.circle is None:
            self.circle = Circle(Point(board.CELL_HEIGHT_WIDTH * self.x + board.CELL_HEIGHT_WIDTH/2, board.CELL_HEIGHT_WIDTH * self.y + board.CELL_HEIGHT_WIDTH/2), board.CELL_HEIGHT_WIDTH / 2)
            self.circle.setOutline('red')
            if self.body_type == 1:
                self.circle.setFill('red')
            else:
                self.circle.setFill('blue')
        if not self.drawn:
            self.circle.draw(graph)
            self.drawn = True

    def __deepcopy__(self, memo):
        return SnakeBodyPart(self.x, self.y, self.body_type)
