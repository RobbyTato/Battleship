import os
from colorama import Back, Fore, Style


def print_screen(string):
    """
    Prints a single or multi-line string to the center of the terminal.
    :param string: The string
    :return: None
    """
    w = os.get_terminal_size().columns
    h = os.get_terminal_size().lines
    dw = get_docstring_width(string)
    dh = get_docstring_height(string)
    strings = string.strip().split("\n")
    final = ""

    # top half of screen
    if h % 2 == 0 and dh % 2 == 1:
        final += "\n"*((h//2) - (dh//2) - 1)
    else:
        final += "\n"*((h//2) - (dh//2))

    # add spaces before the text
    for i in strings:
        final += " "*(((w//2) - (dw//2)) - 1) + i + "\n"

    # bottom half of screen
    if h % 2 == 1 and dh % 2 == 0:
        final += "\n"*((h//2) - (dh//2))
    else:
        final += "\n"*((h//2) - (dh//2) - 1)

    # clear the terminal and then print
    os.system('cls||clear')
    print(final, end="")


def get_docstring_width(string):
    """
    Gets the maximum width of a docstring by splitting it into lines and finding the largest length from all the lines.
    :param string: The docstring
    :return: The maximum length
    """
    max_len = 0
    for s in string.strip().split("\n"):
        if len(remove_ansi(s)) > max_len:
            max_len = len(remove_ansi(s))
    return max_len


def get_docstring_height(string):
    """
    Gets the maximum height of a docstring by returning the number of lines
    :param string: The docstring
    :return: The maximum height
    """
    return len(string.strip().split("\n"))


def remove_ansi(string):
    """
    Removes any ansi characters (color codes) from the string
    :param string: The string
    :return: The string without ansi characters (color codes)
    """
    styles = (Fore.BLACK,
              Fore.RED,
              Fore.GREEN,
              Fore.YELLOW,
              Fore.BLUE,
              Fore.MAGENTA,
              Fore.CYAN,
              Fore.WHITE,
              Fore.RESET,
              Fore.LIGHTBLACK_EX,
              Fore.LIGHTRED_EX,
              Fore.LIGHTGREEN_EX,
              Fore.LIGHTYELLOW_EX,
              Fore.LIGHTBLUE_EX,
              Fore.LIGHTMAGENTA_EX,
              Fore.LIGHTCYAN_EX,
              Fore.LIGHTWHITE_EX,
              Back.BLACK,
              Back.RED,
              Back.GREEN,
              Back.YELLOW,
              Back.BLUE,
              Back.MAGENTA,
              Back.CYAN,
              Back.WHITE,
              Back.RESET,
              Back.LIGHTBLACK_EX,
              Back.LIGHTRED_EX,
              Back.LIGHTGREEN_EX,
              Back.LIGHTYELLOW_EX,
              Back.LIGHTBLUE_EX,
              Back.LIGHTMAGENTA_EX,
              Back.LIGHTCYAN_EX,
              Back.LIGHTWHITE_EX,
              Style.BRIGHT,
              Style.DIM,
              Style.NORMAL,
              Style.RESET_ALL)

    for style in styles:
        string = string.replace(style, "")

    return string


def add_line(new_string, docstring, center=False):
    """
    Takes the main string `docstring` and adds a new string `new_string` to the bottom.
    :param new_string: The string that will be added to the main string.
    :param docstring: The main string.
    :param center: Whether the string should be added to the center of the line.
    :return: The final string (main + new).
    """
    if center:
        w = len(remove_ansi(new_string))
        dw = get_docstring_width(docstring)
        return docstring + "\n" + " "*((dw//2) - (w//2)) + new_string
    else:
        return docstring + "\n" + new_string


def add_lines(new_strings, docstring, center=False):
    """
    Takes the main string `docstring` and adds all the lines in the list `new_strings` to the bottom.
    :param new_string: The list of strings that will be added to the main string.
    :param docstring: The main string.
    :param center: Whether each string should be added to the center of the line.
    :return: The final string (main + new).
    """
    for string in new_strings:
        docstring = add_line(string, docstring, center=center)
    return docstring

