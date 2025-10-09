from typing import Optional
from SinCity.Agent.header import header
from SinCity.Browser.driver_chrome import driver_chrome
from SinCity.colors import (
        RED, 
        RESET, 
        GREEN, 
        YELLOW
        )
from modules.miniTools import (
        init_scraper,
        divide_line,
        recording_single_info
        )
from modules.helper import helper
from modules.config import timeout_parser, preview_info_file
from modules.parser_preview import get_preview_info
from modules.parser_single import get_single_info
import csv
import requests
import sys
import time


def parser_page(url:str, type_page:str, mode:Optional[str]=None) -> dict[str, str | None] | None:
    head = header()
    #простой визуальный разделитель
    divide = divide_line()

    if mode == 'debug':
        print(
                f'{divide}\n'
                f'| {YELLOW}Headers: {head["User-Agent"][0:len(divide)-14]}...{RESET}\n'
                f'| {YELLOW}Type page: {type_page}{RESET}\n'
                f'{divide}'
                )

    print(f'URL: {url}')

    if type_page == 'preview':
        #Собираем инфу с превью
        response = requests.get(url, headers=head)
        status = response.status_code
        if status == 200:
            print(f'{GREEN}Status code: {status}{RESET}')
            data_list = get_preview_info(response)
        else:
            print(f'{RED}STATUS CODE: {status}{RESET}')
    
    elif type_page == 'single':
        driver = None
        company_info = None
        #Собираем инфу с самих страниц
        try:
            driver = driver_chrome()
            driver.get(url)
            time.sleep(timeout_parser)
            page_source = driver.page_source
            #Получаем инфу о компании
            company_info = get_single_info(page_source)
        except Exception as err:
            print(f'{RED}{err}{RESET}')
        finally:
            if driver:
                driver.quit()
        
        return company_info
    
    else:
        sys.exit(f'{RED}Необходим передать тип страницы{RESET}')
    return None

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
    
    elif '--parser-list' in params:
        try:
            divide = divide_line()
            with open(preview_info_file, 'r') as file:
                for number_company, row in enumerate(csv.DictReader(file)):
                    company = row['Company']
                    url = row['URL']
                    image_url = row['Image URL']
                    print(
                            f'[{number_company+1}] {GREEN}{company}{RESET}'
                            )
                    company_info = parser_page(url=url, type_page='single', mode='')
                   
                    if company_info:
                        recording_single_info(
                                company = company,
                                domain = company_info['domain'],
                                phone = company_info['phone'],
                                image_url = image_url,
                                category = 'test category'
                                )
    
        except FileNotFoundError:
            sys.exit(f'{RED}Проверь наличие базы с URL: {preview_info_file}{RESET}')
        except KeyError:
            sys.exit(f'{RED}Проверь правильность наименований колонок{RESET}')
        except KeyboardInterrupt:
            sys.exit(f'{RED}\nExit...{RESET}')
    elif '--help' in params or '-h' in params:
        helper()
    else:
        helper()


