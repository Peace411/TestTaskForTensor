from base import BaseCase


class TestSearchInput(BaseCase):
    def test_find_tensor(self):
        text = 'Тензор'
        self.main_page.open()
        search_input = self.main_page.find_text(text)
        self.main_page.check_suggest()
        search_input.submit()
        self.search_page.check_text_in_input(text)
        href = self.search_page.get_href_first_url_in_result()
        assert href == 'https://tensor.ru/'

    def test_images(self):
        self.main_page.open()
        self.main_page.open_images_page()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == 'https://yandex.ru/images/'
        text = self.images_page.get_text_first_category()
        self.images_page.go_to_first_category()
        self.images_page.check_text_in_input(text)
        href = self.images_page.find(self.images_page.locators.FIRST_IMAGE).get_attribute('href')
        self.images_page.driver.get(href)
        self.images_page.scroll_images()
