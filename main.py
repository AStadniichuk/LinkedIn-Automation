from config.constants import LinkedInProfessionAndLimits, LinkedInURL, LinkedInCredentials
from webdrivers.web_driver import LinkedInDriver
from core.actions.connect_with_people import ConnectWithPeople
from core.actions.login import Login
from core.actions.search_people import SearchPeople


def create_linkedin_driver(url: str) -> LinkedInDriver:
    """Create a LinkedInDriver instance and navigate to the specified URL.

    :param url: The URL to navigate to.
    :return: LinkedInDriver instance.
    """
    driver = LinkedInDriver()
    driver.get(url)
    return driver


def login_to_linkedin(email: str, password: str, driver: LinkedInDriver):
    """Log in to LinkedIn using the provided email and password.

    :param email: The LinkedIn email address.
    :param password: The LinkedIn password.
    :param driver: LinkedInDriver instance.
    """
    linkedin_login = Login(email, password, driver)
    linkedin_login.login_linkedin()


def search_and_connect_people(profession: str, page_limit: int, driver: LinkedInDriver):
    """Search for and connect with people on LinkedIn based on a profession and page limit.

       :param profession: The profession to search for on LinkedIn.
       :param page_limit: The maximum number of pages to search.
       :param driver: LinkedInDriver instance.
       """
    linkedin_search = SearchPeople(profession, driver)
    linkedin_search.search_people()

    linkedin_connect = ConnectWithPeople(page_limit, driver)
    linkedin_connect.connect_with_people()


def main():
    try:
        driver = create_linkedin_driver(LinkedInURL.BASE_URL)

        login_to_linkedin(LinkedInCredentials.EMAIL, LinkedInCredentials.PASSWORD, driver)

        for profession, page_limit in LinkedInProfessionAndLimits.PROFESSIONS_AND_PAGE_LIMITS:
            search_and_connect_people(profession, page_limit, driver)

    except Exception as error:
        raise RuntimeError(f"An error occurred: {str(error)}")

    finally:
        driver.quit_driver()


if __name__ == '__main__':
    main()
