import logging
import keyboard
from playsound import playsound
from colorama import Fore, Back
from player import Player

logging.basicConfig(level=logging.DEBUG, filename="logs.txt", filemode="w", format="%(message)s")


class User(Player):
    
    def __init__(self):
        super().__init__()

    def place_ships(self):
        """
        Takes player input from keyboard to select the ships position.
        :return: None
        """

        def refresh_ship_pos():
            """
            Refreshes the coordinates of the ship parts with respect to the player's cursor
            (Not to be used outside this function).
            :return: None
            """
            nonlocal ship_offset, ship_pos, extra, placeable
            placeable = True
            ship_offset = []
            for i in range(ships[ship][1]):
                x_offset = (i - (ships[ship][1] // 2)) * rotations[current_rotation][0]
                y_offset = (i - (ships[ship][1] // 2)) * rotations[current_rotation][1]
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

        ships = {"c": ["Carrier", 5],
                 "b": ["Battleship", 4],
                 "d": ["Destroyer", 3],
                 "s": ["Submarine", 3],
                 "p": ["Patrol board", 2]}
        ship_offset = []
        ship_pos = []
        extra = []
        placeable = True
        rotations = ((1, 0), (0, 1))
        current_rotation = 0
        for ship in ships:
            cursor = [0, 0]
            refresh_ship_pos()
            top_text = "Player's turn to place ships"
            bottom_text = f"Placing {ships[ship][0]} {ships[ship][1]}x1"
            self.display_ship_board(extra=extra, top_text=top_text, bottom_text=bottom_text)
            while True:
                key = keyboard.read_event()
                if key.event_type == "up" or key.name not in ("up", "down", "left", "right",
                                                              "w", "s", "a", "d", "enter", "space", "r"):
                    continue
                playsound('sounds/move.mp3', False)
                if key.name in ("up", "w"):
                    if cursor[1] != 0:
                        cursor[1] -= 1
                    else:
                        continue
                if key.name in ("down", "s"):
                    if cursor[1] != 9:
                        cursor[1] += 1
                    else:
                        continue
                if key.name in ("left", "a"):
                    if cursor[0] != 0:
                        cursor[0] -= 1
                    else:
                        continue
                if key.name in ("right", "d"):
                    if cursor[0] != 9:
                        cursor[0] += 1
                    else:
                        continue
                if key.name == "r":
                    if current_rotation != len(rotations) - 1:
                        current_rotation += 1
                    else:
                        current_rotation = 0
                if key.name in ("enter", "space"):
                    if placeable:
                        for i in ship_pos:
                            self.ship_board[i[0]][i[1]] = ship
                        break
                    else:
                        continue

                refresh_ship_pos()
                top_text = "Player's turn to place ships"
                bottom_text = f"Placing {ships[ship][0]} {ships[ship][1]}x1"
                self.display_ship_board(extra=extra, top_text=top_text, bottom_text=bottom_text)

    def take_shot(self):
        """
        Takes player input from keyboard to take a shot.
        :return: [y, x]
        """
        cursor = [0, 0]
        extra = []
        if self.shot_board[cursor[0]][cursor[1]] == "-":
            extra.append([cursor, Fore.WHITE + Back.LIGHTBLACK_EX])
            bottom_text = "⠀"  # invisible unicode character only works here, not space
        elif self.shot_board[cursor[0]][cursor[1]] == "O":
            extra.append([cursor, Fore.BLACK + Back.LIGHTBLACK_EX])
            bottom_text = "Cannot take shot here"
        else:
            extra.append([cursor, Fore.BLACK + Back.RED])
            bottom_text = "Cannot take shot here"
        top_text = "Player's turn to take a shot"
        self.display_shot_board(extra=extra, top_text=top_text, bottom_text=bottom_text)
        while True:
            key = keyboard.read_event()
            if key.event_type == "up" or key.name not in ("up", "down", "left", "right",
                                                          "w", "s", "a", "d", "enter", "space"):
                continue
            playsound('sounds/move.mp3', False)
            if key.name in ("up", "w"):
                if cursor[1] != 0:
                    cursor[1] -= 1
                else:
                    continue
            if key.name in ("down", "s"):
                if cursor[1] != 9:
                    cursor[1] += 1
                else:
                    continue
            if key.name in ("left", "a"):
                if cursor[0] != 0:
                    cursor[0] -= 1
                else:
                    continue
            if key.name in ("right", "d"):
                if cursor[0] != 9:
                    cursor[0] += 1
                else:
                    continue
            if key.name in ("space", "enter"):
                if self.shot_board[cursor[0]][cursor[1]] == "-":
                    return cursor[::-1]
                else:
                    continue
            extra = []
            if self.shot_board[cursor[0]][cursor[1]] == "-":
                extra.append([cursor, Fore.WHITE + Back.LIGHTBLACK_EX])
                bottom_text = "⠀"  # invisible unicode character only works here, not space
            elif self.shot_board[cursor[0]][cursor[1]] == "O":
                extra.append([cursor, Fore.BLACK + Back.LIGHTBLACK_EX])
                bottom_text = "Cannot take shot here"
            else:
                extra.append([cursor, Fore.BLACK + Back.RED])
                bottom_text = "Cannot take shot here"
            top_text = "Player's turn to take a shot"
            self.display_shot_board(extra=extra, top_text=top_text, bottom_text=bottom_text)




