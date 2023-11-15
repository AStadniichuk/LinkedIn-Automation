import time

import pyautogui

from selenium.webdriver.common.by import By

from config.constants import LinkedInSelectors, LinkedInURL, LinkedInCredentials
from core.utils.wait_methods import WebDriverWaitMethods
from core.utils.manipulations_with_file import ManipulationWithFile as mf
from core.actions.login import Login
from core.actions.search_people import SearchPeople
from webdrivers.web_driver import LinkedInDriver


class SendMessage(WebDriverWaitMethods):
    def __init__(self, driver, file_with_message: str, file_to_message: str):
        super().__init__(driver)
        self.file_with_message = file_with_message
        self.file_to_message = file_to_message

    def send_message(self):
        self.wait_and_click(By.XPATH, LinkedInSelectors.SEND_MESSAGE_BUTTON_XPATH)
        self.wait_and_click(By.XPATH, LinkedInSelectors.ADD_FILE_BUTTON_XPATH)

        message = mf.read_file(self.file_with_message)
        self.wait_and_send_keys(By.CLASS_NAME, LinkedInSelectors.MESSAGE_INPUT_CLASS, message)

        time.sleep(1)
        file_path = mf.give_path_to_file(self.file_to_message)
        pyautogui.write(file_path)
        pyautogui.press('enter')

        self.wait_and_click(By.XPATH, LinkedInSelectors.FOR_MESSAGE_SEND_BUTTON_XPATH)
        time.sleep(10)


if __name__ == '__main__':
    driver = LinkedInDriver()
    driver.get(LinkedInURL.BASE_URL)

    linkedin_login = Login(LinkedInCredentials.EMAIL, LinkedInCredentials.PASSWORD, driver)
    linkedin_login.login_linkedin()

    linkedin_search = SearchPeople('', driver)
    linkedin_search.search_one_people()
    # linkedin_search.search_people_for_send_message()
    send_message = SendMessage(driver,
                               file_with_message='message.txt',
                               file_to_message='test.txt')
    send_message.send_message()
    time.sleep(10)
