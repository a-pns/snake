from players import Player

class FutureMovePlayer(Player):
    def __init__(self, columns, rows):
        super(OneMovePlayer, self).__init__(columns, rows)

    def new_move(self, snake, fruit, board):
        raise Error("Not Implemented")
