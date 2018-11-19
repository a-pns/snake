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
