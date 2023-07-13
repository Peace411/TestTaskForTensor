import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from pages.locators import ImagesPageLocators


class ImagesPage(BasePage):
    locators = ImagesPageLocators()

    def go_to_first_category(self):
        self.click(self.locators.FIRST_CATEGORY)

    def get_text_first_category(self):
        text_fist_category = self.find(self.locators.FIRST_CATEGORY).get_attribute('data-grid-text')
        return text_fist_category

    def check_text_in_input(self, TEXT):
        search_input = self.find(locator=self.locators.SEARCH_INPUT)
        assert search_input.get_attribute('value') == TEXT

    def click_fist_images(self):
        href = self.find(self.locators.FIRST_IMAGE).get_attribute('href')
        self.driver.get(href)

    def scroll_images(self):
        href_link_images1 = self.find(self.locators.LINK_IMAGES).get_attribute('href')
        self.hover(self.locators.IMAGE_ORIGIN)
        self.click(self.locators.BUTTON_NEXT)
        href_link_images2 = self.find(self.locators.LINK_IMAGES).get_attribute('href')
        assert href_link_images1 != href_link_images2
        self.click(self.locators.BUTTON_BACK)
        href_link_images3 = self.find(self.locators.LINK_IMAGES).get_attribute('href')
        assert href_link_images1 == href_link_images3
