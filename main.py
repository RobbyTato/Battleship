import keyboard
import print_screen as ps
import colorama
import logging
from player import Player
from bot import Bot
from colorama import Fore, Back, Style

logging.basicConfig(level=logging.DEBUG, filename="logs.txt", filemode="w", format="%(message)s")

colorama.init()

# Logo generated by https://patorjk.com/software/taag/ (Font Name: Roman)
title = r'''
oooooooooo.                .       .   oooo                     oooo         o8o
`888'   `Y8b             .o8     .o8   `888                     `888         `"'
 888     888  .oooo.   .o888oo .o888oo  888   .ooooo.   .oooo.o  888 .oo.   oooo  oo.ooooo.
 888oooo888' `P  )88b    888     888    888  d88' `88b d88(  "8  888P"Y88b  `888   888' `88b
 888    `88b  .oP"888    888     888    888  888ooo888 `"Y88b.   888   888   888   888   888
 888    .88P d8(  888    888 .   888 .  888  888    .o o.  )88b  888   888   888   888   888
o888bood8P'  `Y888""8o   "888"   "888" o888o `Y8bod8P' 8""888P' o888o o888o o888o  888bod8P'
                                                                                   888
                                                                                  o888o
'''

controls = '''
⠀ 🡅          W
🡄   🡆  or  A   D to navigate
  🡇          S
   
   Enter to select/confirm
'''


def menu_screen():
    menu_options = ["Play", "Controls", "Exit"]
    option = 0
    menu_text = ps.add_lines(
        ["", "⮞  " + Back.WHITE + Fore.BLACK + "Play" + Style.RESET_ALL + "  ⮜", "", "Controls", "", "Exit"], title,
        center=True)
    ps.print_screen(menu_text)

    while True:

        # process keyboard input
        key = keyboard.read_event()
        if key.event_type == "up" or key.name not in ("s", "down", "w", "up", "enter"):
            continue
        if key.name in ("s", "down"):
            if option == len(menu_options) - 1:
                option = 0
            else:
                option += 1
        if key.name in ("w", "up"):
            if option == 0:
                option = len(menu_options) - 1
            else:
                option -= 1
        if key.name == "enter":
            return menu_options[option]

        # reload menu
        b = title
        for i in range(len(menu_options)):
            b = ps.add_line("", b)
            if i == option:
                b = ps.add_line("⮞  " + Back.WHITE + Fore.BLACK + menu_options[i] + Style.RESET_ALL + "  ⮜", b,
                                center=True)
            else:
                b = ps.add_line(menu_options[i], b, center=True)
        ps.print_screen(b)


def game():
    # 10 x 10 board grid

    # Ship name     Ship size    Name on board (eg. "c")
    # Carrier	    5            c
    # Battleship    4            b
    # Destroyer	    3            d
    # Submarine	    3            s
    # Patrol Boat   2            p

    # Only strings in the shot boards are "O" for miss, "X" for hit, "+" for sunk, and "-" for empty

    player = Player()
    bot = Bot()

    player.place_ships()


def update_boards_on_shot(pos, player_shot_board, enemy_ship_board):
    enemy_ship_value = enemy_ship_board[pos[0]][pos[1]]
    player_shot_value = player_shot_board[pos[0]][pos[1]]

    if enemy_ship_value in ('c', 'd', 'b', 's', 'p'):
        enemy_ship_value = enemy_ship_value + '+'
        player_shot_value = 'X'
    else:
        player_shot_value = 'O'


def check_sunk(player_board, enemy_board):
    pass


if __name__ == "__main__":
    while True:
        choice = menu_screen()
        if choice == "Play":
            game()
        if choice == "Controls":
            ps.print_screen(controls)
            keyboard.wait('enter')
        if choice == "Exit":
            break
