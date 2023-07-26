from player import Player
from random import randint

class Bot(Player):

    def __init__(self):
        super().__init__()

    def place_ships(self):

        ships = {'c':5, 'b':4, 'd':3, 's':3, 'p':2}

        for ship in ships:

            while True:

                ship_coordinates = []
                count = 0

                # coordinates of one end of the ship and rotation | r=0, vertical - r=1, horizontal
                x, y, r = randint(0,9), randint(0,9), randint(0,1)

                if r:
                    for i in range(ships[ship]):
                        ship_coordinates.append((y, x+i))
                else:
                    for i in range(ships[ship]):
                        ship_coordinates.append((y+i, x))
                
                for y, x in ship_coordinates:
                    if 0 <= x <= 9 and 0 <= y <= 9 and self.ship_board[y][x] == '-':
                        count += 1

                if count == ships[ship]:
                    for y, x in ship_coordinates:
                        self.ship_board[y][x] = ship
                    break


    def find_next_shot(self, min_value=2):
        """finds the next shot to take given the current shot board        

        Args:
            min_value (int, optional): used for recursion. Defaults to 2.

        Returns:
            tuple: two coordinates in the form (y, x)
        """
        
        hits = []

        for row_idx, row in enumerate(self.shot_board):
            for column_idx, pos in enumerate(row):
                if pos == 'X':
                    hits.append((row_idx, column_idx))

        if not hits:
            while True:

                x, y = randint(0, 9), randint(0, 9)

                if self.shot_board[y][x] not in ('O', 'X', '+'):
                    return (y, x)

        if len(hits) == 1:
            coords = hits[0]
            if coords[1]-1 >= 0:
                if self.shot_board[coords[0]][coords[1]-1] not in ('O', 'X', '+'):
                    return (coords[0], coords[1]-1)
            if coords[1]+1 < 10:
                if self.shot_board[coords[0]][coords[1]+1] not in ('O', 'X', '+'):
                    return (coords[0], coords[1]+1)
            if coords[0]-1 >= 0:
                if self.shot_board[coords[0]-1][coords[1]] not in ('O', 'X', '+'):
                    return (coords[0]-1, coords[1])
            if coords[0]+1 < 10:
                if self.shot_board[coords[0]+1][coords[1]] not in ('O', 'X', '+'):
                    return (coords[0]+1, coords[1])

        rows = {}
        cols = {}

        for row, col in hits:
            if row not in rows:
                rows[row] = 1
            else:
                rows[row] += 1
            if col not in cols:
                cols[col] = 1
            else:
                cols[col] += 1

        for row in rows:

            current_columns = []

            if rows[row] >= min_value:
                for y, x in hits:
                    if y == row:
                        current_columns.append(x)

                if min(current_columns)-1 >= 0:
                    if self.shot_board[row][min(current_columns)-1] not in ('O', '+'):
                        return (row, min(current_columns)-1)
                if max(current_columns)+1 < 10:
                    if self.shot_board[row][max(current_columns)+1] not in ('O', '+'):
                        return (row, max(current_columns)+1)

        for column in cols:
            current_row = []

            if cols[column] >= min_value:
                for y, x in hits:
                    if x == column:
                        current_row.append(y)

                if min(current_row)-1 >= 0:
                    if self.shot_board[min(current_row)-1][column] not in ('O', '+'):
                        return (min(current_row)-1, column)
                if max(current_row)+1 < 10:
                    if self.shot_board[max(current_row)+1][column] not in ('O', '+'):
                        return (max(current_row)+1, column)
                        
        if min_value != 1:
            return self.find_next_shot(min_value=1)
        
        
                
if __name__ == '__main__':

    bot = Bot()
    
    bot.shot_board = [['+', '+', 'X', 'X', '+', '-', 'O', '-', '-', '-'], 
                      ['+', '+', 'X', 'X', '+', 'O', '-', '-', '-', '-'], 
                      ['+', '+', '-', '-', '-', '-', '-', '-', '-', '-'], 
                      ['+', '+', '-', '-', '-', 'O', '-', '-', '-', '-'], 
                      ['+', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
                      ['-', 'O', '-', '-', 'O', 'O', '-', 'O', 'O', '-'], 
                      ['O', '-', '-', '-', '-', '-', '-', '-', '-', 'O'], 
                      ['-', '-', '-', '-', '-', '-', 'O', '-', '-', '-'], 
                      ['-', '-', 'O', '-', '-', '-', '-', 'O', '-', '-'], 
                      ['-', '-', '-', '-', 'O', '-', '-', 'O', '-', '-']]
    
    print(bot.find_next_shot())
    # bot.place_ships()
    # for i in bot.ship_board:
    #     print(i)


