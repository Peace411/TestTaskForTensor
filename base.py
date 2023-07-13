import pytest
import socket

from pages.images_page import ImagesPage
from pages.main_page import MainPage
from _pytest.fixtures import FixtureRequest

from pages.search_page import SearchPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest,logger):
        self.driver = driver
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.search_page: SearchPage = request.getfixturevalue('search_page')
        self.images_page: ImagesPage = request.getfixturevalue('images_page')
        self.logger = logger