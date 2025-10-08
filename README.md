# парсер сервиса Yelp

## Установка
Клонируем репозиторий + поставим зависимости в окружени
```sh
git clone https://github.com/rickert157/yelp_scrapy.git
```
```sh
cd yelp_scrapy/
```
```sh
python3 -m venv venv && ./venv/bin/pip install -r package.txt
```

## Debug Mode
В режиме debug можно парсить по одной странице. Пример
```sh
python3 yelp_scraper.py --debug 'https://www.yelp.com.au/search?find_desc=Zum+Abholen&find_loc=California+City%2C+CA'
```

