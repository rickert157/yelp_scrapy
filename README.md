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
В режиме debug можно парсить по одной странице(preview или single).   
Необходимо передать --debug для режима отладки  
Необходимо передать type - single или preview  
Пример:
```sh
python3 yelp_scraper.py \
            --debug type=preview \
            'https://www.yelp.de/search?find_desc=Zum+Abholen&find_loc=California+City%2C+CA'
```

## Финальный сбор
Для обхода списка URL можно использовать эту команду
```sh
python3 yelp_scraper.py --parser-list
```
