from selenium.webdriver.common.by import By


class MainPageLocators():
    SEARCH_INPUT = (By.XPATH, '//input[@id="text"]')
    SUGGEST_LIST = (By.CSS_SELECTOR, '.mini-suggest__popup-content')
    BUTTON_MORE_ITEM = (By.CSS_SELECTOR, 'li.services-suggest__list-item-more')
    BUTTON_IMAGES = (By.XPATH, '//a[contains(@href,"https://yandex.ru/images/")]')


class SearchPageLocators():
    SEARCH_INPUT = (By.CSS_SELECTOR, '.input__box .input__control')
    SEARCH_RESULT = (By.ID, 'search-result')
    FIRST_RESULT = (By.CSS_SELECTOR, '.serp-item')
    FIRST_URL_IN_RESULT = (By.CSS_SELECTOR, '.serp-item .Link')


class ImagesPageLocators():
    FIRST_CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0')
    SEARCH_INPUT = (By.CSS_SELECTOR, '.input__box .input__control')
    FIRST_IMAGE = (By.CSS_SELECTOR, 'a.serp-item__link')
    LINK_IMAGES = (By.CSS_SELECTOR, '.Link.Link_view_default')
    IMAGE_ORIGIN = (By.CSS_SELECTOR, '.MMImage-Origin')
    BUTTON_NEXT = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_next')
    BUTTON_BACK = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_prev')
