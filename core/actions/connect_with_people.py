from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config.constants import LinkedInSelectors, LinkedInPopups
from core.utils.wait_methods import WebDriverWaitMethods


class ConnectWithPeople(WebDriverWaitMethods):
    """A class for automating the process of connecting with people on LinkedIn.

       This class provides methods for sending connection requests to multiple LinkedIn users.

       Args:
           page_limit (int): The number of pages to process.
           driver (WebDriver): The WebDriver instance.

         Attributes:
           page_limit (int): The number of pages to process.

       Methods:
           connect_with_people: Send connection requests to multiple LinkedIn users.

       Private Methods:
           __make_contact: Click on the "Connect" button and send a connection request.
           __scroll_to_bottom: Scroll to the bottom of the page to load more profiles.
           __click_next_button: Click the "Next" button to navigate to the next page.
           __handle_popup_window: Handle LinkedIn popup window and quit the driver if found.

       Raises:
           RuntimeError: If a timeout occurs while waiting for an element or if the element is not found.
       """

    def __init__(self, page_limit, driver):
        super().__init__(driver)
        self.page_limit = page_limit

    def connect_with_people(self):
        """Send connection requests to multiple LinkedIn users."""
        for _ in range(self.page_limit):
            try:
                make_contact_buttons = self.wait_and_get_elements(By.XPATH,
                                                                  LinkedInSelectors.MAKE_CONTACT_BUTTON_XPATH)
                if make_contact_buttons:
                    self.__make_contact(make_contact_buttons)
            except TimeoutException:
                self.__scroll_and_click_next()

    def __make_contact(self, make_contact_buttons):
        """Click on the "Connect" button and send a connection request."""
        for button in make_contact_buttons:
            button.click()
            self.__handle_contact_popup()
        self.__scroll_and_click_next()

    def __handle_contact_popup(self):
        """Handle the popup window after clicking the 'Connect' button."""
        popup_window = self.wait_for_element(By.XPATH,
                                             LinkedInPopups.POPUP_WINDOW_SET_CONTACT_XPATH,
                                             timeout=1)

        message = 'Чтобы подтвердить, что этот участник вас знает, укажите его(ее) адрес эл. почты для установления контакта. Вы также можете добавить личное сообщение в свое приглашение'

        if message in popup_window.text:
            self.wait_and_click(By.XPATH, LinkedInSelectors.SKIP_BUTTON_XPATH)
        else:
            self.wait_and_click(By.XPATH, LinkedInSelectors.SEND_CONTACT_BUTTON_XPATH)
            self.__handle_popup_window()

    def __handle_popup_window(self):
        """Handle LinkedIn popup window and quit the driver if found."""
        popup_window = WebDriverWait(self.driver, 1).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, LinkedInPopups.POPUP_WINDOW_XPATH)))

        message = 'Достигнуто максимально допустимое число приглашений в неделю'
        if message in popup_window.text:
            print(message)
            self.driver.quit()

        popup_html = popup_window.get_attribute('outerHTML')
        print(popup_window.text, popup_html, sep='\n')
        self.wait_and_click(By.XPATH, LinkedInSelectors.OK_BUTTON_XPATH)

    def __scroll_and_click_next(self):
        """Scroll down and click 'Next' button to navigate to the next page."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_and_click(By.XPATH, LinkedInSelectors.NEXT_BUTTON_XPATH)
