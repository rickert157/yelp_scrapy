from bs4 import BeautifulSoup
from SinCity.colors import (
        RED, 
        RESET, 
        GREEN, 
        YELLOW
        )
from modules.miniTools import divide_line

def get_single_info(response) -> dict[str, str | None]:
    divide = divide_line()

    bs = BeautifulSoup(response, 'lxml')
    
    company_tag = bs.find(class_='y-css-olzveb')
    company_name = company_tag.get_text() if company_tag else None
    
    domain = None
    for domain_tag in bs.find_all(class_='y-css-14ckas3'):
        domain_href = domain_tag.get('href')
        if domain_href and '/biz_redir?' in domain_href:
            domain_redirect = domain_tag.get('href')
            domain = domain_redirect.split('%3A%2F%2F')[1]
            if '%2F' in domain:domain = domain.split('%2F')[0]
            if '&cachebuster=' in domain:domain = domain.split('&cachebuster=')[0]
    
    phone = None
    for phone_div in bs.find_all(class_='y-css-8x4us'):
        if 'Phone' in phone_div.get_text() or 'Telefonnummer' in phone_div.get_text():
            phone = phone_div.find(class_='y-css-qn4gww').get_text()
            break
        
    data = {
            "company_name":company_name,
            "domain":domain,
            "phone":phone
            }

    print(
            f'{GREEN}Company name:\t{company_name}\n{RESET}'
            f'{GREEN}Domain:\t\t{domain}{RESET}\n'
            f'{GREEN}Phone:\t\t{phone}{RESET}\n\n'
            f'{divide}\n'
            )
    return data
