from typing import Optional
from shutil import get_terminal_size
from modules.config import (
        result_dir, 
        preview_info_file,
        single_info_file_domain,
        single_info_file_no_domain,
        done_file
        )
import os
import csv

def divide_line():
    terminal_size = int(get_terminal_size().columns-3)
    divide = '-'*terminal_size
    return divide

def init_scraper():
    if not os.path.exists(result_dir):os.makedirs(result_dir)

def modif_url(url:Optional[str]=None) -> Optional[str]:
    """Скоратим длину URL для отображения в терминале """
    modif = None
    if url and len(url) > 60:
        modif = f'{url[0:50]}...'
    
    return modif


def recording_preview_info(
        company:Optional[str], 
        company_url:Optional[str], 
        image_url:Optional[str]
        ) -> None:
    if not os.path.exists(preview_info_file):
        with open(preview_info_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Company', 'URL', 'Image URL'])

    with open(preview_info_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([company, company_url, image_url])

def list_done_domain() -> list[str | None]:
    list_domains = set()
    if os.path.exists(done_file):
        with open(done_file, 'r') as file:
            for line in file.readlines():
                list_domains.add(line.strip())
    return list_domains

def recording_single_info(
        company:Optional[str],
        image_url:Optional[str],
        category:Optional[str]=None,
        domain:Optional[str]=None,
        phone:Optional[str]=None
        ) -> None:
    file_name = single_info_file_domain if domain else single_info_file_no_domain
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            columns = ['Company', 'Domain', 'Phone', 'Category', 'Image URL'] if domain \
                    else ['Company', 'Phone', 'Category', 'Image URL']
            writer.writerow(columns)
    
    with open(file_name, 'a') as file:
        writer = csv.writer(file)
        data_line = [company, domain, phone, category, image_url] if domain \
                else [company, phone, category, image_url]
        writer.writerow(data_line)
    
    return None
