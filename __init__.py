from graphics import *
import time
from board import Board
from snake import *
from fruit import *
from player import *
import random
import datetime

win = GraphWin("Snake", width=400, height=400, autoflush=False)
win.setBackground('black')
time.sleep(1)
board = Board(10, 10)
snake = Snake(1, 1)
fruit = Fruit(random.randint(0,9),random.randint(0,9))
player = Player(1,10,10)

game_is_dead = False
while not game_is_dead:
    print ("Start: ", datetime.datetime.now().time())
    if not game_is_dead:
        print ("Calc Move: ", datetime.datetime.now().time())
        player.new_move(snake, fruit, board)
        print ("Move: ", datetime.datetime.now().time())
        snake.move(fruit)
    if not snake.is_dead(board):
        print ("Check Fruit: ", datetime.datetime.now().time())
        if snake.has_eaten(fruit):
            fruit = Fruit(random.randint(0,9),random.randint(0,9))
    else:
        game_is_dead = True
    print ("Start Draw: ", datetime.datetime.now().time())
    board.draw_board(win)
    fruit.draw(board, win)
    snake.draw(board, win)
    print ("End Draw: ", datetime.datetime.now().time())
    win.flush()
    time.sleep(.05)
