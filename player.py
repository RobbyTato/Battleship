import logging
import keyboard
from colorama import Fore, Back, Style
import print_screen as ps
logging.basicConfig(level=logging.DEBUG, filename="logs.txt", filemode="w", format="%(message)s")


class Player:
    def __init__(self):
        self.ship_board = [["-" for _ in range(10)] for _ in range(10)]
        self.shot_board = [["-" for _ in range(10)] for _ in range(10)]

    def setup_ships(self):
        ships = {"c": 5, "b": 4, "d": 3, "s": 3, "p": 2}
        rotations = ((1, 0), (0, 1))
        current_rotation = 0
        for ship in ships:
            cursor = [0, 0]
            while True:
                placeable = True
                ship_offset = []
                for i in range(ships[ship]):
                    x_offset = (i - (ships[ship] // 2)) * rotations[current_rotation][0]
                    y_offset = (i - (ships[ship] // 2)) * rotations[current_rotation][1]
                    ship_offset.append([x_offset, y_offset])
                ship_pos = []
                for i in ship_offset:
                    x = i[0] + cursor[0]
                    y = i[1] + cursor[1]
                    if not (0 <= x <= 9 and 0 <= y <= 9):
                        placeable = False
                    if not self.ship_board[x][y] == "-":
                        placeable = False
                        ship_pos.append([[x, y], Back.RED])
                    else:
                        ship_pos.append([[x, y], Back.LIGHTBLACK_EX])
                logging.debug(ship_pos)
                self.display_ship_board(extra=ship_pos)

                key = keyboard.read_event()
                if key.event_type == "up" or key.name not in ("up", "down", "left", "right",
                                                               "w", "s", "a", "d", "enter", "r"):
                    continue
                if key.name in ("up", "w"):
                    if cursor[0] != 0:
                        cursor[0] -= 1
                    else:
                        continue
                if key.name in ("down", "s"):
                    if cursor[0] != 9:
                        cursor[0] += 1
                    else:
                        continue
                if key.name in ("left", "a"):
                    if cursor[1] != 0:
                        cursor[1] -= 1
                    else:
                        continue
                if key.name in ("right", "d"):
                    if cursor[1] != 9:
                        cursor[1] += 1
                    else:
                        continue
                if key.name == "r":
                    if current_rotation != len(rotations) - 1:
                        current_rotation += 1
                    else:
                        current_rotation = 0
                if key.name == "enter":
                    if placeable:
                        for i in ship_pos:
                            self.ship_board[i[0][0]][i[0][1]] = ship
                        break
                    else:
                        continue

            ship_offset = []

    def ship_board_to_string(self, extra=None):
        s = "╔" + ("═" * 20) + "╗\n"  # first row
        for x in range(10):  # add the board
            s += "║"
            for y in range(10):
                if extra is None:
                    if self.ship_board[x][y] == "-":
                        s += "  "
                    else:
                        s += Back.LIGHTBLACK_EX + "  " + Style.RESET_ALL
                else:
                    for i in extra:
                        if i[0] == [x, y]:
                            s += i[1] + "  " + Style.RESET_ALL
                            break
                    else:
                        if self.ship_board[x][y] == "-":
                            s += "  "
                        else:
                            s += Back.LIGHTBLACK_EX + "  " + Style.RESET_ALL
            s += "║\n"
        s += "╚" + ("═" * 20) + "╝"  # last row
        return s

    def display_ship_board(self, extra=None):
        ps.print_screen(self.ship_board_to_string(extra))

    def find_next_move(self):
        pass
