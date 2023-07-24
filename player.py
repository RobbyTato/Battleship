from colorama import Fore, Back, Style
import print_screen as ps
import logging

logging.basicConfig(level=logging.DEBUG, filename="logs.txt", filemode="a", format="%(message)s")


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

        Returns:
            result (str): 'X' if hit, 'O' if miss
        """

        enemy_ship_value = enemy_ship_board[pos[0]][pos[1]]

        if enemy_ship_value in ('c', 'd', 'b', 's', 'p'):
            enemy_ship_board[pos[0]][pos[1]] = enemy_ship_value + '+'
            self.shot_board[pos[0]][pos[1]] = 'X'
            return 'X'
        else:
            self.shot_board[pos[0]][pos[1]] = 'O'
            return 'O'

    def ship_board_to_string(self, extra=None, top_text="", bottom_text=""):
        """
        Converts self.ship_board into a multiline string.
        :param extra: To add any extra details to the string that is not on the board (e.g. the cursor of the player)
                      Format: [ [[y,x], color], ... ]
        :param top_text: Adds text to the top of the board (can be multiline)
        :param bottom_text: Adds text to the bottom of the board (can be multiline)
        :return: string
        """
        lines_list = []
        top_width = ps.get_docstring_width(top_text)
        bottom_width = ps.get_docstring_width(bottom_text)
        if top_width > bottom_width and top_width > 42:
            longest_width = top_width
        elif bottom_width > top_width and bottom_width > 42:
            longest_width = bottom_width
        else:
            longest_width = 42
        string = "⠀" * longest_width  # invisible unicode character only works here, not space
        for i in top_text.split("\n"):
            lines_list.append(i)
        lines_list.append(Fore.LIGHTBLACK_EX + "▄" + ("▄" * 40) + "▄" + Style.RESET_ALL)  # first row
        for x in range(10):  # add the board
            line = Fore.LIGHTBLACK_EX + "█" + Style.RESET_ALL
            for y in range(10):
                if extra is None:
                    if self.ship_board[y][x] == "-":
                        line += Back.LIGHTBLUE_EX + "    " + Style.RESET_ALL
                    else:
                        line += Fore.BLACK + Back.LIGHTBLACK_EX + "▓▓▓▓" + Style.RESET_ALL
                else:
                    for i in extra:
                        if i[0] == [y, x]:
                            line += i[1] + "▓▓▓▓" + Style.RESET_ALL
                            break
                    else:
                        if self.ship_board[y][x] == "-":
                            line += Back.LIGHTBLUE_EX + "    " + Style.RESET_ALL
                        else:
                            line += Fore.BLACK + Back.LIGHTBLACK_EX + "▓▓▓▓" + Style.RESET_ALL
            line += Fore.LIGHTBLACK_EX + "█" + Style.RESET_ALL
            lines_list.append(line)
            lines_list.append(line)
        lines_list.append(Fore.LIGHTBLACK_EX + "▀" + ("▀" * 40) + "▀" + Style.RESET_ALL)  # last row
        for j in bottom_text.split("\n"):
            lines_list.append(j)
        string = ps.add_lines(lines_list, string, center=True)
        return string

    def shot_board_to_string(self, extra=None, top_text="", bottom_text=""):
        """
        Converts self.shot_board into a multiline string.
        :param extra: To add any extra details to the string that is not on the board (e.g. the cursor of the player)
                      Format: [ [[y,x], color], ... ]
        :param top_text: Adds text to the top of the board (can be multiline)
        :param bottom_text: Adds text to the bottom of the board (can be multiline)
        :return: string
        """
        lines_list = []
        top_width = ps.get_docstring_width(top_text)
        bottom_width = ps.get_docstring_width(bottom_text)
        if top_width > bottom_width and top_width > 42:
            longest_width = top_width
        elif bottom_width > top_width and bottom_width > 42:
            longest_width = bottom_width
        else:
            longest_width = 42
        string = "⠀" * longest_width  # invisible unicode character only works here, not space
        for i in top_text.split("\n"):
            lines_list.append(i)
        lines_list.append(Fore.LIGHTBLACK_EX + "▄" + ("▄" * 40) + "▄" + Style.RESET_ALL)  # first row
        for x in range(10):  # add the board
            line = Fore.LIGHTBLACK_EX + "█" + Style.RESET_ALL
            for y in range(10):
                if extra is None:
                    if self.shot_board[y][x] == "-":
                        line += Back.LIGHTBLUE_EX + "    " + Style.RESET_ALL
                    elif self.shot_board[y][x] == "O":
                        line += Fore.LIGHTBLACK_EX + Back.WHITE + "▓▓▓▓" + Style.RESET_ALL
                    else:
                        line += Fore.LIGHTRED_EX + Back.RED + "▓▓▓▓" + Style.RESET_ALL
                else:
                    for i in extra:
                        if i[0] == [y, x]:
                            line += i[1] + "▓▓▓▓" + Style.RESET_ALL
                            break
                    else:
                        if self.shot_board[y][x] == "-":
                            line += Back.LIGHTBLUE_EX + "    " + Style.RESET_ALL
                        elif self.shot_board[y][x] == "O":
                            line += Fore.LIGHTBLACK_EX + Back.WHITE + "▓▓▓▓" + Style.RESET_ALL
                        else:
                            line += Fore.LIGHTRED_EX + Back.RED + "▓▓▓▓" + Style.RESET_ALL
            line += Fore.LIGHTBLACK_EX + "█" + Style.RESET_ALL
            lines_list.append(line)
            lines_list.append(line)
        lines_list.append(Fore.LIGHTBLACK_EX + "▀" + ("▀" * 40) + "▀" + Style.RESET_ALL)  # last row
        for j in bottom_text.split("\n"):
            lines_list.append(j)
        string = ps.add_lines(lines_list, string, center=True)
        return string

    def display_ship_board(self, extra=None, top_text="", bottom_text=""):
        """
        Prints self.ship_board to the screen.
        :param extra: To add any extra details to the screen that is not on the board (e.g. the cursor of the player)
                      Format: [ [[y,x], color], ... ]
        :param top_text: Adds text to the top of the board (can be multiline)
        :param bottom_text: Adds text to the bottom of the board (can be multiline)
        :return: None
        """
        ps.print_screen(self.ship_board_to_string(extra, top_text, bottom_text))

    def display_shot_board(self, extra=None, top_text="", bottom_text=""):
        """
        Prints self.shot_board to the screen.
        :param extra: To add any extra details to the screen that is not on the board (e.g. the cursor of the player)
                      Format: [ [[y,x], color], ... ]
        :param top_text: Adds text to the top of the board (can be multiline)
        :param bottom_text: Adds text to the bottom of the board (can be multiline)
        :return: None
        """
        ps.print_screen(self.shot_board_to_string(extra, top_text, bottom_text))
