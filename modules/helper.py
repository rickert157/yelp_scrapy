from SinCity.colors import RED, RESET, GREEN, BLUE
from modules.miniTools import divide_line

def help_debug():
    text = f"""\
    {BLUE}Debug Mode{RESET}{GREEN}
    В режиме Debug доступны парсинг превью ресторанов 
    и страницы самих ресторанов. Синтаксис команды 
    получается такой:{RESET}

    python3 yelp_scraper.py --debug type=[preview/single] [url]
    
    Или же реальный пример
    python3 yelp_scraper.py \\
            --debug type=preview \\
            'https://www.yelp.de/search?find_desc=Zum+Abholen&find_loc=California+City%2C+CA'
    """
    return text

def helper():
    divide = divide_line()
    print(
            f"{divide}\n"
            f"{help_debug()}\n"
            f"{divide}\n"
            )
