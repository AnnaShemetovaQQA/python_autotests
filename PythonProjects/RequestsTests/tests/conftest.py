# импортируем модули и отдельные классы
import pytest

from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# назначаем работу фикстуры в рамках сессии
@pytest.fixture(scope='session')

# каждый тест должен начинаться с test_
def browser():
    """
    Test case WERT-1
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service()
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://testqastudio.me/"
    yield driver
    driver.quit()