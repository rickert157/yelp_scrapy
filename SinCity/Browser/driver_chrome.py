from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from SinCity.Agent.header import header

def driver_chrome():
    profileChrome = 'ProfileChrome'

    head = header()['User-Agent']

    chrome_options = Options()
    chrome_options.add_argument(f"--user-agent={head}")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--dns-server=8.8.8.8,8.8.4.4")
    chrome_options.add_argument("--disable-blink-features")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("start-maximized")
    
    driver_chrome = webdriver.Chrome(options=chrome_options)

    return driver_chrome
