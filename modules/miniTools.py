from typing import Optional
from modules.config import result_dir, preview_info_file
import os
import csv

def init_scraper():
    if not os.path.exists(result_dir):os.makedirs(result_dir)

def modif_url(url:Optional[str]=None) -> Optional[str]:
    """Скоратим длину URL для отображения в терминале """
    modif = None
    if url and len(url) > 60:
        modif = f'{url[0:50]}...'
    
    return modif


def recording_preview_info(company:str, company_url:str, image_url:str) -> None:
    if not os.path.exists(preview_info_file):
        with open(preview_info_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Company', 'URL', 'Image URL'])

    with open(preview_info_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([company, company_url, image_url])
