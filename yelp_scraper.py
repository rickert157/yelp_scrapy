import requests
import sys
from typing import Optional
from SinCity.Agent.header import header
from SinCity.colors import (
        RED, 
        RESET, 
        GREEN, 
        YELLOW
        )
from modules.parser_preview import get_preview_info
from modules.miniTools import (
        init_scraper,
        divide_line
        )
from modules.helper import helper

def parser_page(url:str, type_page:str, mode:Optional[str]=None) -> list[str]:
    head = header()
    #простой визуальный разделитель
    divide = divide_line()

    if mode == 'debug':
        print(
                f'{divide}\n'
                f'| {YELLOW}Headers: {head['User-Agent'][0:len(divide)-14]}...{RESET}\n'
                f'| {YELLOW}Type page: {type_page}{RESET}\n'
                f'{divide}'
                )

    print(f'URL: {url}')
    response = requests.get(url, headers=head)
    status = response.status_code
    
    if status == 200:
        print(f'{GREEN}Status code: {status}{RESET}')
        if type_page == 'preview':
            data_list = get_preview_info(response)
            print(data_list)
        if type_page == 'single':
            print(f'{RED}В процессе разработки{RESET}')
    elif status == 404:
        print(f'Данной страницы не существует')
    else:
        print(f'{RED}Status code: {status}{RESET}')

if __name__ == '__main__':
    init_scraper()

    params = sys.argv
    mode = None
    if '--debug' in params and len(params) > 2:
        mode = f'{RED}DEBUG MODE{RESET}'
        url = params[-1]
        if "type=" in params[-2]:
            target_type_page = params[-2].split('=')[1]
            if target_type_page == 'preview' or target_type_page == 'single':
                type_page = target_type_page
            else:
                helper()
        else:
            helper()
        print(mode)

        """
        type_page - имеется ввиду тип страницы, которую парсим - preview или single
        это временное имя параметра, в дальнейшем необходимо заменить
        """
        parser_page(url=url, mode='debug', type_page=type_page)
    
    elif '--help' in params or '-h' in params:
        helper()
    else:
        helper()


