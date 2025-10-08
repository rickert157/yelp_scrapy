from bs4 import BeautifulSoup
from SinCity.colors import RED, RESET, GREEN
from modules.miniTools import modif_url, recording_preview_info

def get_preview_info(response) -> list[dict]:
    bs = BeautifulSoup(response.text, 'lxml')
    
    data_list = []

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
            
            #собираем данные в словарь
            company_info = {
                    "company":company_name,
                    "company_url":company_url_yelp,
                    "image_url":image_url
                    }
            #и отправляем в список
            data_list.append(company_info)

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
        
    return data_list
