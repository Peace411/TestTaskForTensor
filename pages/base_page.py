import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import logging

CLICK_RETRY = 3
logger = logging.getLogger('test')


class BasePage():
    url = 'https://ya.ru/'

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    @allure.step('Find elements {locator}')
    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def hover(self, locator):
        element = self.find(locator=locator)
        self.scroll_to(element)
        hov = ActionChains(self.driver).move_to_element(element)
        hov.perform()

    @allure.step('Clicking on {locator}')
    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                self.scroll_to(element)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise TimeoutException
