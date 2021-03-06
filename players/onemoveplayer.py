from players import Player
from utils import Direction


class OneMovePlayer(Player):
    def __init__(self, columns, rows):
        super(OneMovePlayer, self).__init__(columns, rows)

    def how_close_in_direction(self, snake, direction):
        head = snake.head()
        if direction == Direction.LEFT or direction == Direction.RIGHT:
            temp_parts = list(filter( lambda part:  part.y == head.y and part != head, snake.body_parts))
            if direction == Direction.LEFT:
                temp_parts = list(filter( lambda part:  part.x < head.x, temp_parts))
                temp_parts.sort(key=lambda part: part.x, reverse=True)
            else:
                temp_parts = list(filter( lambda part:  part.x > head.x, temp_parts))
                temp_parts.sort(key=lambda part: part.x)
            if len(temp_parts) > 0:
                result = abs(temp_parts[0].x - head.x) - 1
                if result == 0:
                    return -150
                return result
        else:
            temp_parts = list(filter( lambda part:  part.x == head.x and part != head, snake.body_parts))
            if direction == Direction.UP:
                temp_parts = list(filter( lambda part: part.y < head.y, temp_parts))
                temp_parts.sort(key=lambda part: part.y, reverse=True)
            else:
                temp_parts = list(filter( lambda part: part.y > head.y, temp_parts))
                temp_parts.sort(key=lambda part: part.y)
            if len(temp_parts) > 0:
                result = abs(temp_parts[0].y - head.y) - 1
                if result == 0:
                    return -150
                return result
        return 5

    def score_for_direction(self, snake, direction, fruit):
        how_close = self.how_close_in_direction(snake, direction)
        head = snake.move(fruit, False, direction)[0]
        if head.x < 0 or head.x >= self.columns or head.y < 0 or head.y > self.rows:
            return -200
        return how_close - self.number_steps_to_fruit(head, fruit)

    def number_steps_to_fruit(self,head,fruit):
        result = abs(head.x - fruit.x) + abs(head.y - fruit.y)
        return result


    def new_move(self, snake, fruit, board):
        moves = {}
        moves[Direction.LEFT] = self.score_for_direction(snake, Direction.LEFT, fruit)
        moves[Direction.RIGHT] =  self.score_for_direction(snake, Direction.RIGHT, fruit)
        moves[Direction.UP] = self.score_for_direction(snake, Direction.UP, fruit)
        moves[Direction.DOWN] = self.score_for_direction(snake, Direction.DOWN, fruit)
        the_direction = None
        the_current_value = 0;
        for key in moves:
            if the_direction is None:
                the_direction = key
                the_current_value = moves[key]
            elif moves[key] > the_current_value:
                the_direction = key
                the_current_value = moves[key]
        snake.change_direction(the_direction)
