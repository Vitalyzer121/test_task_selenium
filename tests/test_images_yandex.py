from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.images_yandex import ImagesYandex


options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.implicitly_wait(5)

def test_images_yandex():
    """Тест для проверки второй части задания"""

    browser.get('https://ya.ru/')
    print('Начало теста')
    start = ImagesYandex(browser)
    start.assert_menu()
    start.assert_url()
    start.open_image()
    start.assert_image()
    print('Окончание теста')
    browser.quit()

if __name__ == '__main__':
    test_images_yandex()