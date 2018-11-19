from graphics import *
import time
from board import Board
from snake import *
from fruit import *
from player import *
import random
import datetime

class Game:
    def __init__(self, player, width, height, speed):
        self.speed = speed
        self.player = player
        self.width = width
        self.height = height
        self.board = Board(width, height)
        self.snake = Snake(random.randint(0,width-1),random.randint(0,height-1))
        self.fruit = Fruit(random.randint(0,width-1),random.randint(0,height-1))
        self.score = 0
        self.game_is_dead = False
        # Cecil was a caterpilla, Cecil was my friend - Mum
        self.window = GraphWin("Cecil", width=300, height=300, autoflush=False)
        self.window.setBackground('white')

    def run(self):
        while not self.game_is_dead:
            self.move()
            self.update_game_state()
            self.draw()
            time.sleep(self.speed)

        self.window.close()
        print("Final Score: {0}".format(self.score))


    def move(self):
        self.player.new_move(self.snake, self.fruit, self.board)
        self.snake.move(self.fruit)

    def update_game_state(self):
        if not self.snake.is_dead(self.board):
            if self.snake.has_eaten(self.fruit):
                new_x = random.randint(0,9)
                new_y = random.randint(0,9)
                while (self.snake.contains_pos(new_x, new_y)):
                    new_x = random.randint(0,9)
                    new_y = random.randint(0,9)
                self.fruit.set_new_position(new_x, new_y)
                self.score += 1
        else:
            self.game_is_dead = True

    def draw(self):
        self.fruit.draw(self.board, self.window)
        self.snake.draw(self.board, self.window)
        self.window.flush()

if __name__ == "__main__":
    sim_speed = 0.1
    player = Player(1,10,10)
    the_game = Game(player, 10, 10, sim_speed)
    the_game.run()
    time.sleep(5)
