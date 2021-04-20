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
    # TODO make this more efficient?
    if any(option in BRIGHT for option in options):
        colored_string = '\33[1m'+colored_string
    if any(option in DARK for option in options):
        colored_string = '\33[2m'+colored_string
    if any(option in ITALIC for option in options):
        colored_string = '\33[3m'+colored_string
    if any(option in UNDERLINE for option in options):
        colored_string = '\33[4m'+colored_string
    if any(option in BLINK for option in options):
        colored_string = '\33[5m'+colored_string
    if any(option in SELECTED for option in options):
        colored_string = '\33[7m'+colored_string
    return colored_string

def colored_string(string: str, color_number: int, options, background) -> str:
    colored_string = '\33['+str(color_number)+'m'+string+'\33[0m'
    if background:
        return '\33['+str(color_number+10)+'m'+string+'\33[0m'
    colored_string = color_options(colored_string, options)
    return colored_string

def black(string: str, options: list[str] = [], background: str = '') -> str:
    return colored_string(string, 30, options, background)

def red(string: str, options: list[str] = [], background: bool = False) -> str:
    return colored_string(string, 31, options, background)

def green(string: str, options: list[str] = [], background: bool = False) -> str:
    return colored_string(string, 32, options, background)

def yellow(string: str, options: list[str] = [], background: bool = False) -> str:
    return colored_string(string, 33, options, background)

def blue(string: str, options: list[str] = [], background: bool = False) -> str:
    return colored_string(string, 34, options, background)

def magenta(string: str, options: list[str] = [], background: bool = False) -> str:
    return colored_string(string, 35, options, background)

def cyan(string: str, options: list[str] = [], background: bool = False) -> str:
    return colored_string(string, 36, options, background)

def white(string: str, options: list[str] = [], background: bool = False) -> str:
    return colored_string(string, 37, options, background)
