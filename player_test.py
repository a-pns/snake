from snake import *
from player import *
from fruit import *

def test_how_close_in_direction_LEFT():
    snake = Snake(4,4);
    player = Player(1)
    test_snake_body = [SnakeBodyPart(4,4,1),SnakeBodyPart(4,3,2),SnakeBodyPart(3,3,2),SnakeBodyPart(3,4,2)]
    snake.body_parts = test_snake_body
    result = player.how_close_in_direction(snake, Direction.LEFT)
    print(result)
    assert result == 0

    test_snake_body = [SnakeBodyPart(4,4,1),SnakeBodyPart(4,3,2),SnakeBodyPart(3,3,2),SnakeBodyPart(2,3,2),SnakeBodyPart(2,4,2)]
    snake.body_parts = test_snake_body
    result = player.how_close_in_direction(snake, Direction.LEFT)
    print(result)
    assert result == 1

def test_how_close_in_direction_UP():
    snake = Snake(4,4);
    player = Player(1)
    test_snake_body = [SnakeBodyPart(4,4,1),SnakeBodyPart(5,4,2),SnakeBodyPart(5,3,2),SnakeBodyPart(4,3,2)]
    snake.body_parts = test_snake_body
    result = player.how_close_in_direction(snake, Direction.UP)
    print(result)
    assert result == 0

    test_snake_body = [SnakeBodyPart(4,4,1),SnakeBodyPart(5,4,2),SnakeBodyPart(5,3,2),SnakeBodyPart(5,2,2),SnakeBodyPart(4,2,2)]
    snake.body_parts = test_snake_body
    result = player.how_close_in_direction(snake, Direction.UP)
    print(result)
    assert result == 1

def test_how_close_in_direction_RIGHT():
    snake = Snake(4,4);
    player = Player(1)
    test_snake_body = [SnakeBodyPart(4,4,1),SnakeBodyPart(4,3,2),SnakeBodyPart(5,3,2),SnakeBodyPart(5,4,2)]
    snake.body_parts = test_snake_body
    result = player.how_close_in_direction(snake, Direction.RIGHT)
    print(result)
    assert result == 0

    test_snake_body = [SnakeBodyPart(4,4,1),SnakeBodyPart(4,3,2),SnakeBodyPart(5,3,2),SnakeBodyPart(6,3,2),SnakeBodyPart(6,4,2)]
    snake.body_parts = test_snake_body
    result = player.how_close_in_direction(snake, Direction.RIGHT)
    print(result)
    assert result == 1

def test_how_close_in_direction_DOWN():
    snake = Snake(4,4);
    player = Player(1)
    test_snake_body = [SnakeBodyPart(4,4,1),SnakeBodyPart(5,4,2),SnakeBodyPart(5,5,2),SnakeBodyPart(4,5,2)]
    snake.body_parts = test_snake_body
    result = player.how_close_in_direction(snake, Direction.DOWN)
    print(result)
    assert result == 0

    test_snake_body = [SnakeBodyPart(4,4,1),SnakeBodyPart(5,4,2),SnakeBodyPart(5,5,2),SnakeBodyPart(5,6,2),SnakeBodyPart(4,6,2)]
    snake.body_parts = test_snake_body
    result = player.how_close_in_direction(snake, Direction.DOWN)
    print(result)
    assert result == 1

def test_number_steps_to_fruit():
    snake = Snake(4,4).body_parts[0];
    player = Player(1)
    fruit = Fruit(2,2)
    assert player.number_steps_to_fruit(snake,fruit) == 4
    fruit = Fruit(3,2)
    assert player.number_steps_to_fruit(snake,fruit) == 3
    fruit = Fruit(4,2)
    assert player.number_steps_to_fruit(snake,fruit) == 2
    fruit = Fruit(5,2)
    assert player.number_steps_to_fruit(snake,fruit) == 3
    fruit = Fruit(6,2)
    assert player.number_steps_to_fruit(snake,fruit) == 4
    fruit = Fruit(2,3)
    assert player.number_steps_to_fruit(snake,fruit) == 3
    fruit = Fruit(6,3)
    assert player.number_steps_to_fruit(snake,fruit) == 3
    fruit = Fruit(2,4)
    assert player.number_steps_to_fruit(snake,fruit) == 2
    fruit = Fruit(6,4)
    assert player.number_steps_to_fruit(snake,fruit) == 2
    fruit = Fruit(2,5)
    assert player.number_steps_to_fruit(snake,fruit) == 3
    fruit = Fruit(6,5)
    assert player.number_steps_to_fruit(snake,fruit) == 3
    fruit = Fruit(2,6)
    assert player.number_steps_to_fruit(snake,fruit) == 4
    fruit = Fruit(3,6)
    assert player.number_steps_to_fruit(snake,fruit) == 3
    fruit = Fruit(4,6)
    assert player.number_steps_to_fruit(snake,fruit) == 2
    fruit = Fruit(5,6)
    assert player.number_steps_to_fruit(snake,fruit) == 3
    fruit = Fruit(6,6)
    assert player.number_steps_to_fruit(snake,fruit) == 4
