from selenium.webdriver.common.by import By

from config.constants import LinkedInSelectors
from core.utils.wait_methods import WebDriverWaitMethods


class SearchPeople(WebDriverWaitMethods):
    """A class for performing LinkedIn people searches.

       This class provides methods for conducting LinkedIn searches and applying filters to the results.

       Args:
           profession (str): The profession or search query.
           driver (WebDriver): The WebDriver instance.

       Methods:
           search_people: Perform a people search on LinkedIn and apply filters.

       Attributes:
           __search_people_filter (bool): A class-level flag to track whether filters have been applied.

       Raises:
           RuntimeError: If a timeout occurs while waiting for an element or if the element is not found.
       """

    __search_people_filter = True

    def __init__(self, profession, driver):
        """Initialize LinkedInSearch.

                :param profession: The profession or search query.
                :param driver: WebDriver instance."""
        super().__init__(driver)
        self.profession = profession

    def search_people(self):
        """Perform a people search on LinkedIn."""
        self.__search_by_profession()

        if self.__class__.__search_people_filter:
            self.__apply_people_filter()
            self.__class__.__search_people_filter = False

    def __search_by_profession(self):
        """Enter the search query and submit."""
        self.wait_and_send_keys(By.CLASS_NAME, LinkedInSelectors.SEARCH_INPUT_CLASS, self.profession + '\n')

    def __apply_people_filter(self):
        """Apply people filter to the search results."""
        self.wait_and_click(By.XPATH, LinkedInSelectors.FILTER_PEOPLE_BUTTON_XPATH)
        self.wait_and_click(By.XPATH, LinkedInSelectors.FILTER_REGION_BUTTON_XPATH)
        self.wait_and_click(By.XPATH, LinkedInSelectors.FILTER_REGION_UKRAINE_BUTTON_XPATH)
        self.wait_and_click(By.XPATH, LinkedInSelectors.SHOW_RESULT_COUNTRY_BUTTON_XPATH)

    def search_one_people(self):
        self.wait_and_send_keys(By.CLASS_NAME, LinkedInSelectors.SEARCH_INPUT_CLASS, self.profession + '\n')

    def search_people_for_send_message(self):
        self.wait_and_send_keys(By.CLASS_NAME, LinkedInSelectors.SEARCH_INPUT_CLASS, self.profession + '\n')
        self.wait_and_click(By.XPATH, LinkedInSelectors.FILTER_PEOPLE_BUTTON_XPATH)
        self.wait_and_click(By.XPATH, LinkedInSelectors.FILTER_CONTACTS_BUTTON_XPATH)
        self.wait_and_click(By.XPATH, LinkedInSelectors.FILTER_CONTACTS_FIRST_BUTTON_XPATH)
        self.wait_and_click(By.XPATH, LinkedInSelectors.SHOW_RESULT_CONTACTS_BUTTON_XPATH)
