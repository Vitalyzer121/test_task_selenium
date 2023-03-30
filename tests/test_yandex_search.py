from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.yandex_search import YandexSearch


options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.implicitly_wait(5)

def test_yandex_search():
    """Тест для проверки первой части задания"""

    browser.get('https://ya.ru/')
    print('Начало теста')
    start = YandexSearch(browser)
    start.assert_search()
    start.send_search()
    start.assert_suggest()
    start.enter_to_click()
    start.search_to_find()
    start.verification_link()
    print('Окончание теста')
    browser.quit()


if __name__ == '__main__':
    test_yandex_search()


