from graphics import *
import time
from board import Board
from snake import *
from fruit import *
from player import *
import random
import datetime


time.sleep(1)
game_length = 10
sim_speed = 0.1
games = {}
for game in range(10):
    win = GraphWin("Cecil", width=300, height=300, autoflush=False)
    # Cecil was a caterpilla, Cecil was my friend - Mum
    win.setBackground('black')
    board = Board(10, 10)
    snake = Snake(random.randint(0,9),random.randint(0,9))
    fruit = Fruit(random.randint(0,9),random.randint(0,9))
    player = Player(1,10,10)
    board.draw_board(win)
    score = 0
    game_is_dead = False
    while not game_is_dead:
        if not game_is_dead:
            player.new_move(snake, fruit, board)
            snake.move(fruit)
        if not snake.is_dead(board):
            if snake.has_eaten(fruit):
                new_x = random.randint(0,9)
                new_y = random.randint(0,9)
                while (snake.contains_pos(new_x, new_y)):
                    new_x = random.randint(0,9)
                    new_y = random.randint(0,9)
                fruit.set_new_position(new_x, new_y)
                score += 1
        else:
            game_is_dead = True
        fruit.draw(board, win)
        snake.draw(board, win)
        win.flush()
        time.sleep(sim_speed)
    games[game] = score
    print("Final Score for game({g}) = {s} and final state of snake: {sn}".format(g=game, s=score, sn=snake))
    win.close()
print("Game results: ", games)
total_score = 0
for g_k in games:
    total_score += games[g_k]
average_score = total_score / len(games)
print("Average Game Score: ", average_score)
