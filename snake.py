from graphics import *


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
        temp_body_parts = []
        i = 0
        for i in range(len(self.body_parts)):
            part = self.body_parts[i]
            if part.body_type == 1:
                # if head then move 1 place in 1 direction
                temp_body_parts.append(SnakeBodyPart(part.x + direction[0], part.y + direction[1], part.body_type))
            else:
                # if not head then take place of pre-ceeding body part
                part = self.body_parts[i-1]
                temp_body_parts.append(SnakeBodyPart(part.x, part.y, 2))
        if self.has_eaten(fruit, temp_body_parts) and do_move:
            part = self.body_parts[len(self.body_parts)-1]
            temp_body_parts.append(SnakeBodyPart(part.x, part.y, 2))
        if do_move:
            self.body_parts = temp_body_parts
        else:
            return temp_body_parts

    def draw(self,board, graph):
        for part in self.body_parts:
            cir = Circle(Point(board.CELL_HEIGHT_WIDTH * part.x + board.CELL_HEIGHT_WIDTH/2, board.CELL_HEIGHT_WIDTH * part.y + board.CELL_HEIGHT_WIDTH/2), board.CELL_HEIGHT_WIDTH / 2)
            cir.setOutline('red')
            if part.body_type == 1:
                cir.setFill('red')
            else:
                cir.setFill('blue')
            cir.draw(graph)

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

    def __str__(self):
        snake_str = ""
        for part in self.body_parts:
            snake_str += ", ({p}})".format(p=part)
        return snake_str

    def __repr__(self):
        return self.__str__()


class SnakeBodyPart:
    def __init__(self, x, y, body_type):
        self.x = x;
        self.y = y;
        self.body_type = body_type

    def __str__(self):
        return "{x},{y},{t}".format(x=self.x,y=self.y,t=self.body_type)

    def __repr__(self):
        return self.__str__()
