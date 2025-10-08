import requests
import sys
from typing import Optional
from bs4 import BeautifulSoup
from SinCity.Agent.header import header
from SinCity.colors import (
        RED, 
        RESET, 
        GREEN, 
        YELLOW
        )
from modules.miniTools import (
        init_scraper,
        modif_url, 
        recording_preview_info
        )

def get_info(response) -> dict[str, list[str]]:
    bs = BeautifulSoup(response.text, 'lxml')
    title = bs.title.get_text()
    for block in bs.find_all(class_='y-css-pwt8yl'):
        #Перебираем по отдельности каждый блок с рестораном
        try:
            #В этом блоке и название компании, и локальная ссылка на ресторан
            company_name_tag = block.find(class_="y-css-1x1e1r2")
            #собираем имя ресторана
            company_name = company_name_tag.get_text() if company_name_tag else None
            #собираем внутреннюю ссылку на ресторан
            company_url_yelp = f"https://www.yelp.de{company_name_tag.get('href')}" \
                    if company_name_tag else None
            
            #собираем ссылку на фото ресторана
            image_url_tag = block.find(class_='y-css-fex5b')
            image_url = image_url_tag.get('src') if image_url_tag else None

            company_modif_url_yelp = modif_url(url=company_url_yelp)
            image_modif_url = modif_url(url=image_url)

            print(
                    f'{GREEN}Company name:\t{company_name}\n{RESET}'
                    f'{GREEN}URL Yelp:{RESET}\t{company_modif_url_yelp}\n'
                    f'{GREEN}Image URL:{RESET}\t{image_modif_url}\n'
                    )
            recording_preview_info(
                    company=company_name, 
                    company_url=company_url_yelp,
                    image_url=image_url
                    )

        except AttributeError as err:
            print(f'{YELLOW}AttributeError: {err}{RESET}')
        except Exception as err:
            print(f'{RED}{err}{RESET}')

    return [title]

            

def parser_page(url:str, mode:Optional[str]=None) -> list[str]:
    head = header()
    if mode:
        print(f'{YELLOW}Headers: {head}{YELLOW}')

    print(f'URL: {url}')
    response = requests.get(url, headers=head)
    status = response.status_code
    
    if status == 200:
        print(f'{GREEN}Status code: {status}{RESET}')
        title = get_info(response)
        print(title)
    elif status == 404:
        print(f'Данной страницы не существует')
    else:
        print(f'{RED}Status code: {status}{RESET}')

if __name__ == '__main__':
    init_scraper()

    params = sys.argv
    mode = None
    if '--debug' in params:
        mode = f'{RED}DEBUG MODE{RESET}'
        url = params[-1]
        print(mode)
        parser_page(url=url, mode='debug')
    
    else:
        print('Передай режим работы и URL параметром')


