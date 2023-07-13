from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()
    url = 'https://ya.ru/'

    def find_text(self, text):
        search_input = self.find(locator=self.locators.SEARCH_INPUT)
        search_input.send_keys(text)
        return search_input

    def check_suggest(self):
        assert self.find(locator=self.locators.SUGGEST_LIST)

    def open_images_page(self):
        self.click(self.locators.SEARCH_INPUT)
        self.click(self.locators.BUTTON_MORE_ITEM)
        self.click(self.locators.BUTTON_IMAGES)
