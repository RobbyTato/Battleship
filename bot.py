from player import Player

class Bot(Player):

    def __init__(self):
        super().__init__()


    def find_next_move(self, board):
        
        for row_idx, row in enumerate(board):
            for pos_idx, pos in enumerate(row):
                if pos == 'x':
                    next_move = self.analyse_hit(board, (row_idx, pos_idx))




    def analyse_hit(self, board, pos):
        
        for offset in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            row_pos = pos[0] + offset[0]
            column_pos = pos[1] + offset[1]
            if board[row_pos][column_pos] == 'x':
                match offset:
                    case (-1, 0):
                        self.analyse_hit()
                    case (0, -1):
                        pass
                    case (0, 1):
                        pass
                    case (1, 0):
                        pass
                



