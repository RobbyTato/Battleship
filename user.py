import logging
import keyboard
from colorama import Fore, Back, Style
import print_screen as ps

logging.basicConfig(level=logging.DEBUG, filename="logs.txt", filemode="w", format="%(message)s")


class User:
    def __init__(self):
        self.ship_board = [["-" for _ in range(10)] for _ in range(10)]
        self.shot_board = [["-" for _ in range(10)] for _ in range(10)]

    def place_ships(self):

        def refresh_ship_pos():
            nonlocal ship_offset, ship_pos, extra, placeable
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
                ship_pos.append([x, y])
            outside = False  # check if ship is outside the box
            for x, y in ship_pos:
                if not (0 <= x <= 9 and 0 <= y <= 9):
                    outside = True
                    placeable = False
                    break
            extra = []
            for x, y in ship_pos:
                if not (0 <= x <= 9 and 0 <= y <= 9):
                    placeable = False
                elif not self.ship_board[x][y] == "-":
                    placeable = False
                    extra.append([[x, y], Fore.RED + Back.RED])
                else:
                    if outside:
                        extra.append([[x, y], Fore.LIGHTRED_EX + Back.RED])
                    else:
                        extra.append([[x, y], Fore.BLACK + Back.LIGHTBLACK_EX])

        ships = {"c": 5, "b": 4, "d": 3, "s": 3, "p": 2}
        ship_offset = []
        ship_pos = []
        extra = []
        placeable = True
        rotations = ((1, 0), (0, 1))
        current_rotation = 0
        for ship in ships:
            cursor = [0, 0]
            refresh_ship_pos()
            self.display_ship_board(extra=extra)
            while True:
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
                            self.ship_board[i[0]][i[1]] = ship
                        break
                    else:
                        continue

                refresh_ship_pos()
                self.display_ship_board(extra=extra)

    def take_shot(self):
        cursor = [0, 0]
        while True:
            extra = []
            if self.shot_board[cursor[0]][cursor[1]] == "-":
                extra.append([cursor, Fore.WHITE + Back.LIGHTBLACK_EX])
            elif self.shot_board[cursor[0]][cursor[1]] == "O":
                extra.append([cursor, Fore.BLACK + Back.LIGHTBLACK_EX])
            else:
                extra.append([cursor, Fore.BLACK + Back.RED])
            self.display_shot_board(extra=extra)
            key = keyboard.read_event()
            if key.event_type == "up" or key.name not in ("up", "down", "left", "right",
                                                          "w", "s", "a", "d", "enter"):
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
            if key.name == "enter":
                return cursor

    def ship_board_to_string(self, extra=None):
        s = Fore.LIGHTBLACK_EX + "▄" + ("▄" * 40) + "▄\n" + Style.RESET_ALL  # first row
        for x in range(10):  # add the board
            line = Fore.LIGHTBLACK_EX + "█" + Style.RESET_ALL
            for y in range(10):
                if extra is None:
                    if self.ship_board[x][y] == "-":
                        line += Back.LIGHTBLUE_EX + "    " + Style.RESET_ALL
                    else:
                        line += Fore.BLACK + Back.LIGHTBLACK_EX + "▓▓▓▓" + Style.RESET_ALL
                else:
                    for i in extra:
                        if i[0] == [x, y]:
                            line += i[1] + "▓▓▓▓" + Style.RESET_ALL
                            break
                    else:
                        if self.ship_board[x][y] == "-":
                            line += Back.LIGHTBLUE_EX + "    " + Style.RESET_ALL
                        else:
                            line += Fore.BLACK + Back.LIGHTBLACK_EX + "▓▓▓▓" + Style.RESET_ALL
            line += Fore.LIGHTBLACK_EX + "█\n" + Style.RESET_ALL
            s += line * 2
        s += Fore.LIGHTBLACK_EX + "▀" + ("▀" * 40) + "▀" + Style.RESET_ALL  # last row
        return s

    def shot_board_to_string(self, extra=None):
        s = Fore.LIGHTBLACK_EX + "▄" + ("▄" * 40) + "▄\n" + Style.RESET_ALL  # first row
        for x in range(10):  # add the board
            line = Fore.LIGHTBLACK_EX + "█" + Style.RESET_ALL
            for y in range(10):
                if extra is None:
                    if self.shot_board[x][y] == "-":
                        line += Back.LIGHTBLUE_EX + "    " + Style.RESET_ALL
                    elif self.shot_board[x][y] == "O":
                        line += Fore.LIGHTBLACK_EX + Back.WHITE + "▓▓▓▓" + Style.RESET_ALL
                    else:
                        line += Fore.LIGHTRED_EX + Back.RED + "▓▓▓▓" + Style.RESET_ALL
                else:
                    for i in extra:
                        if i[0] == [x, y]:
                            line += i[1] + "▓▓▓▓" + Style.RESET_ALL
                            break
                    else:
                        if self.shot_board[x][y] == "-":
                            line += Back.LIGHTBLUE_EX + "    " + Style.RESET_ALL
                        elif self.shot_board[x][y] == "O":
                            line += Fore.LIGHTBLACK_EX + Back.WHITE + "▓▓▓▓" + Style.RESET_ALL
                        else:
                            line += Fore.LIGHTRED_EX + Back.RED + "▓▓▓▓" + Style.RESET_ALL
            line += Fore.LIGHTBLACK_EX + "█\n" + Style.RESET_ALL
            s += line * 2
        s += Fore.LIGHTBLACK_EX + "▀" + ("▀" * 40) + "▀" + Style.RESET_ALL  # last row
        return s

    def display_ship_board(self, extra=None):
        ps.print_screen(self.ship_board_to_string(extra))

    def display_shot_board(self, extra=None):
        ps.print_screen(self.shot_board_to_string(extra))



