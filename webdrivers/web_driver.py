from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver


class LinkedInDriver:
    """A singleton class for managing the WebDriver instance for LinkedIn automation.

    This class ensures that only one WebDriver instance is created and reused.

    Attributes:
        _instance: The singleton instance of LinkedInDriver.
        _driver: The WebDriver instance.

    Methods:
        driver: Property to get the WebDriver instance.
        _initialize_driver: Private method to initialize the WebDriver.
        quit_driver: Method to quit the WebDriver."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._driver = None

    @property
    def driver(self) -> WebDriver:
        """Get the WebDriver instance.

        :return: The WebDriver instance.
        :rtype: webdriver.Chrome"""
        if self._driver is None:
            try:
                self._initialize_driver()
            except WebDriverException as error:
                raise RuntimeError(f'Web driver initialization error: {error}')
        return self._driver

    def _initialize_driver(self):
        """ Initialize the WebDriver with Chrome options."""
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self._driver = webdriver.Chrome(options=options)

    def get(self, url: str):
        """Navigate to the specified URL.

        :param url: The URL to navigate to.
        """
        self.driver.get(url)

    def quit_driver(self):
        """Quit the WebDriver if it's running."""
        if self._driver:
            self._driver.quit()
