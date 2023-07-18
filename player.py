class Player:
    def __init__(self):
        self.ship_board = [["-" for _ in range(10)] for _ in range(10)]
        self.shot_board = [["-" for _ in range(10)] for _ in range(10)]

    def find_next_move(self):
        pass