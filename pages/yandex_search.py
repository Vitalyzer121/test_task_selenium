from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class YandexSearch(Base):
    """Класс для работы с полем поиска в Yandex"""

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators

    search = '//*[@id="text"]'
    suggest = 'ul > li'
    find_search = "//*[contains(@class, 'serp-list serp-list_left_yes')]"
    link = '//*[@id="search-result"]/li[1]/div[1]/div[2]/div[1]/a/b'

    # Getters

    def get_search(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.search)))

    # Actions

    def assert_search(self):
        """Метод для проверки наличия поля поиска"""

        try:
            self.browser.find_element(By.XPATH, self.search)
        except NoSuchElementException:
            print('Поле для поиска отсутствует')
        print('Поле для поиска присутствует')

    def send_search(self):
        """Метод для ввода данных в поле поиска"""

        self.get_search().send_keys('Тензор')

    def assert_suggest(self):
        """Метод для проверки наличия таблицы с подсказками"""

        locator = (By.CSS_SELECTOR, self.suggest)
        try:
            WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print('Таблица с подсказками отсутсвует')
        print('Таблица с подсказками присутствует')

    def enter_to_click(self):
        """Метод для нажатия кнопки 'найти'"""

        self.get_search().send_keys(Keys.ENTER)

    def search_to_find(self):
        """Метод проверяющий, что появилась страница результатов поиска"""

        locator = (By.XPATH, self.find_search)
        try:
            elements = WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print('Страница результатов поиска не появилась')
        print('Cтраница результатов поиска появилась')

    def verification_link(self):
        """Метод проверяющий, что 1 ссылка ведет на сайт tensor.ru"""

        try:
            self.browser.find_element(By.XPATH, self.link).text == 'tensor.ru'
        except NoSuchElementException:
            print('1 ссылка не ведет на сайт tensor.ru')
        print('1 ссылка ведет на сайт tensor.ru')


