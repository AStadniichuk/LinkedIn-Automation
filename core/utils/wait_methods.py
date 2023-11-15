from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class WebDriverWaitMethods:
    """Utility class for waiting for elements and interacting with them using Selenium's WebDriverWait."""

    def __init__(self, driver, default_timeout=10):
        """Initialize a WebDriverWaitMethods object.

        :param driver: WebDriver instance.
        :param default_timeout: Default timeout in seconds for waiting operations.
        """
        self.driver: WebDriver = driver.driver
        self.default_timeout: int = default_timeout

    def wait_for_element(self, by: str, value: str, timeout: int | None = None) -> WebElement:
        """Wait for an element to appear on the page.

        :param by: The way to search for the element (e.g., By.ID, By.XPATH).
        :param value: The value of the element attribute (e.g., ID or XPath).
        :param timeout: Timeout in seconds (default_timeout is used by default).
        :return: WebElement.
        :raises: RuntimeError if the timeout is exceeded.
        """
        timeout = timeout or self.default_timeout
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.element_to_be_clickable((by, value)))
            return element
        except TimeoutException:
            raise RuntimeError(f"Element with {by}='{value}' not found within {timeout} seconds.")

    def wait_and_send_keys(self, by: str, value: str, keys: str, timeout: int | None = None) -> None:
        """Wait for an element and enter text into it.

        :param by: The way to search for the element (e.g., By.ID, By.XPATH).
        :param value: The value of the element attribute (e.g., ID or XPath).
        :param keys: Text to enter.
        :param timeout: Timeout in seconds (default_timeout is used by default).
        """
        element = self.wait_for_element(by, value, timeout)
        element.clear()
        element.send_keys(keys)

    def wait_and_click(self, by: str, value: str, timeout: int | None = None) -> None:
        """Wait for an element and click on it.

        :param by: The way to search for the element (e.g., By.ID, By.XPATH).
        :param value: The value of the element attribute (e.g., ID or XPath).
        :param timeout: Timeout in seconds (default_timeout is used by default).
        """
        element = self.wait_for_element(by, value, timeout)
        element.click()

    def wait_and_get_elements(self, by: str, value: str, timeout: int | None = None) -> list[WebElement]:
        """Waiting for items and retrieving a list of items.

        :param by: The way to search for elements (e.g. By.ID, By.XPATH).
        :param value: The value of the elements attribute (e.g. ID or XPath).
        :param timeout: Timeout in seconds (default_timeout is used by default).
        :return: WebElement list.
        """
        timeout = timeout or self.default_timeout
        elements = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_all_elements_located((by, value)))
        return elements
