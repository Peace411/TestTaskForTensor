from pages.base_page import BasePage
from pages.locators import SearchPageLocators


class SearchPage(BasePage):
    locators = SearchPageLocators()

    def check_text_in_input(self, text):
        search_input = self.find(locator=self.locators.SEARCH_INPUT)
        assert search_input.get_attribute('value') == text

    def get_href_first_url_in_result(self):
        result = self.find(locator=self.locators.FIRST_URL_IN_RESULT)
        return result.get_attribute('href')
