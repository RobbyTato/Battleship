

class Player:

    def __init__(self):
        self.ship_board = [["-" for _ in range(10)] for _ in range(10)]
        self.shot_board = [["-" for _ in range(10)] for _ in range(10)]
        # stores all the ships that are sunk - holds the letter components
        self.sunk_ships = []

    def update_boards_on_shot(self, pos, enemy_ship_board):
        """updates boards of both players after a shot has been fired

        Args:
            pos (tuple): tuple containing the y and x coordinates of the shot
            enemy_ship_board (list): the ship board of the player that recieved the shot
        """    

        enemy_ship_value = enemy_ship_board[pos[0]][pos[1]]

        if enemy_ship_value in ('c', 'd', 'b', 's', 'p'):
            enemy_ship_board[pos[0]][pos[1]] = enemy_ship_value + '+'
            self.shot_board[pos[0]][pos[1]] = 'X'
        else:
            self.shot_board[pos[0]][pos[1]] = 'O'