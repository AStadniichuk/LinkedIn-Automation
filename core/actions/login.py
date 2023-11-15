from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from config.constants import LinkedInSelectors
from core.utils.wait_methods import WebDriverWaitMethods


class Login(WebDriverWaitMethods):
    """Login to your LinkedIn account using the provided email and password.

       This class provides methods to perform the login operation on LinkedIn.

       Args:
           email (str): The email address used for login.
           password (str): The password used for login.
           driver (WebDriver): The WebDriver instance.

       Methods:
           login_linkedin: Logs in to the LinkedIn account with the provided credentials.

       Raises:
           RuntimeError: If a timeout occurs while waiting for an element or if the element is not found.
       """

    def __init__(self, email, password, driver):
        super().__init__(driver)
        self.email = email
        self.password = password

    def login_linkedin(self):
        """Log in to the LinkedIn account with the provided email and password."""
        try:
            self.wait_and_send_keys(By.ID, LinkedInSelectors.EMAIL_INPUT_ID, self.email)
            self.wait_and_send_keys(By.ID, LinkedInSelectors.PASSWORD_INPUT_ID, self.password)
            self.wait_and_click(By.XPATH, LinkedInSelectors.LOGIN_BUTTON_XPATH)

        except TimeoutException as error:
            raise RuntimeError(f"Timeout while waiting for element: {error}")
        except NoSuchElementException as error:
            raise RuntimeError(f"Element not found: {error}")
