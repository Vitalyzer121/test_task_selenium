import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from urllib.parse import unquote
from base.base_class import Base


class ImagesYandex(Base):
    """Класс для работы с картинками в Yandex"""

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators

    menu = 'services-suggest__icons-more'
    image = "//*[@class = 'Link PopularRequestList-Preview']"
    category_locator = '.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > img'
    category_text_locator = '.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > div.PopularRequestList-SearchText'
    picture_locator = 'serp-item__link'
    next_page = '/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[4]'
    previous_page = '/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[1]'

    # Actions

    def assert_menu(self):
        """Метод для проверки кнопки 'меню' на странице"""

        self.browser.find_element(By.XPATH, "//*[@id='text']").click()
        try:
            self.browser.find_element(By.CLASS_NAME, self.menu).click()
        except NoSuchElementException:
            print('Меню нет на странице')
        print('Меню есть на странице')
        self.browser.find_element(By.LINK_TEXT,"Картинки").click()

    def assert_url(self):
        """Метод для проверки url"""

        url = self.browser.current_url
        try:
            url == 'https://yandex.ru/images/'
        except NoSuchElementException:
            print('URL не соответствует https://yandex.ru/images/')
        print('URL соответствует https://yandex.ru/images/')
        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)

    def open_image(self):
        """Метод для проверки категории в поле поиска"""

        category = self.browser.find_element(By.CSS_SELECTOR, self.category_locator)
        category_text = self.browser.find_element(By.CSS_SELECTOR, self.category_text_locator).text
        self.browser.execute_script("arguments[0].click();", category)
        search_text = unquote(self.browser.current_url)

        try:
            category_text in search_text
        except NoSuchElementException:
            print('Название категории не отображается в поле поиска')
        print('Название категории отображается в поле поиска')

    def assert_image(self):
        """Метод для проверки отображения картинок"""

        image1 = self.browser.find_element(By.CLASS_NAME, self.picture_locator)
        try:
            image1.click()
        except NoSuchElementException:
            print('Картинка не открылась')
        print('Картинка открылась')
        time.sleep(2)
        self.browser.find_element(By.XPATH, self.next_page).click()
        image2 = self.browser.find_element(By.CLASS_NAME, 'MMImageContainer')

        try:
            image1 != image2
        except NoSuchElementException:
            print('Картинка не изменилась после нажатия кнопки "вперед"!')
        print('Картинка изменилась после нажатия кнопки "вперед"!')

        self.browser.find_element(By.XPATH, self.previous_page).click()
        assert image1, 'Картинка изменилась'
        print('Картинка не изменилась')







