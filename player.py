

class Player:

    def __init__(self):
        self.ship_board = [["-" for _ in range(10)] for _ in range(10)]
        self.shot_board = [["-" for _ in range(10)] for _ in range(10)]
        # stores all the ships that are sunk - holds the letter components
        self.sunk_ships = []