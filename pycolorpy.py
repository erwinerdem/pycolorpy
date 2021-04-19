def color_options(colored_string: str, options) -> str:
    options = [option.lower() for option in options]
    BRIGHT = ['bright', 'bold', 'b']
    DARK = ['dark', 'dim', 'd']
    ITALIC = ['italic', 'i']
    UNDERLINE = ['underline', 'u']
    BLINK = ['blink', 'bl']
    SELECTED = ['selected', 's']
    all_valid_options = BRIGHT + DARK + ITALIC + UNDERLINE + BLINK + SELECTED
    invalid_options = ', '.join(['"'+option+'"' for option in options if option not in all_valid_options])
    if invalid_options:
        raise Exception('Invalid option(s) used!\n'+invalid_options+' are not valid options...')
    if any(option in BRIGHT for option in options):
        colored_string = '\33[1m'+colored_string+'\33[0m'
    if any(option in DARK for option in options):
        colored_string = '\33[2m'+colored_string+'\33[0m'
    if any(option in ITALIC for option in options):
        colored_string = '\33[3m'+colored_string+'\33[0m'
    if any(option in UNDERLINE for option in options):
        colored_string = '\33[4m'+colored_string+'\33[0m'
    if any(option in BLINK for option in options):
        colored_string = '\33[5m'+colored_string+'\33[0m'
    if any(option in SELECTED for option in options):
        colored_string = '\33[7m'+colored_string+'\33[0m'
    return colored_string


def black(string: str, options = [], background: bool = False) -> str:
    color_number = 30
    colored_string = '\33['+str(color_number)+'m'+string+'\33[0m'
    if background:
        return '\33['+str(color_number+10)+'m'+string+'\33[0m'
    colored_string = color_options(colored_string, options)
    return colored_string


def red(string: str, options = [], background: bool = False) -> str:
    color_number = 31
    colored_string = '\33['+str(color_number)+'m'+string+'\33[0m'
    if background:
        return '\33['+str(color_number+10)+'m'+string+'\33[0m'
    colored_string = color_options(colored_string, options)
    return colored_string


def green(string: str, options = [], background: bool = False) -> str:
    color_number = 32
    colored_string = '\33['+str(color_number)+'m'+string+'\33[0m'
    if background:
        return '\33['+str(color_number+10)+'m'+string+'\33[0m'
    colored_string = color_options(colored_string, options)
    return colored_string


def yellow(string: str, options = [], background: bool = False) -> str:
    color_number = 33
    colored_string = '\33['+str(color_number)+'m'+string+'\33[0m'
    if background:
        return '\33['+str(color_number+10)+'m'+string+'\33[0m'
    colored_string = color_options(colored_string, options)
    return colored_string


def blue(string: str, options = [], background: bool = False) -> str:
    color_number = 34
    colored_string = '\33['+str(color_number)+'m'+string+'\33[0m'
    if background:
        return '\33['+str(color_number+10)+'m'+string+'\33[0m'
    colored_string = color_options(colored_string, options)
    return colored_string


def magenta(string: str, options = [], background: bool = False) -> str:
    color_number = 35
    colored_string = '\33['+str(color_number)+'m'+string+'\33[0m'
    if background:
        return '\33['+str(color_number+10)+'m'+string+'\33[0m'
    colored_string = color_options(colored_string, options)
 
    return colored_string


def cyan(string: str, options = [], background: bool = False) -> str:
    color_number = 36
    colored_string = '\33['+str(color_number)+'m'+string+'\33[0m'
    if background:
        return '\33['+str(color_number+10)+'m'+string+'\33[0m'
    colored_string = color_options(colored_string, options)
    return colored_string


def white(string: str, options = [], background: bool = False) -> str:
    color_number = 37
    colored_string = '\33['+str(color_number)+'m'+string+'\33[0m'
    if background:
        return '\33['+str(color_number+10)+'m'+string+'\33[0m'
    colored_string = color_options(colored_string, options)
    return colored_string
