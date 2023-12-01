from decouple import config


class LinkedInCredentials:
    """LinkedIn credential."""
    EMAIL = config('EMAIL', default='')
    PASSWORD = config('PASSWORD', default='')


class LinkedInURL:
    """LinkedIn URL."""
    BASE_URL = 'https://www.linkedin.com/'


class LinkedInButtons:
    """LinkedIn button text constants."""
    LOGIN_BUTTON = "Войти"

    PEOPLE_FILTER = "Люди"
    REGION_FILTER = "Регионы"
    UKRAINE_REGION_FILTER = "Ukraine"
    CONTACTS_FILTER = "Контакты"
    FIRST_CONTACT_FILTER = "1-й"

    CONNECT_BUTTON = "Установить контакт"
    SEND_BUTTON = "Отправить без заметки"
    NEXT_BUTTON = "Далее"
    SHOW_RESULT_BUTTON = "Показать результаты"

    OK_BUTTON = "ОК"

    SEND_MESSAGE_BUTTON = "Отправить сообщение"
    ADD_FILE_TO_DRAFT_BUTTON = "Добавить файл в черновик обсуждения"
    ADD_FILE_TO_OBSERVATION_BUTTON = "Добавить файл в обсуждение с участником"


class LinkedInSelectors:
    """LinkedIn selector for elements on a pages."""
    EMAIL_INPUT_ID = 'session_key'
    PASSWORD_INPUT_ID = 'session_password'
    LOGIN_BUTTON_XPATH = f'//button[contains(., "{LinkedInButtons.LOGIN_BUTTON}")]'

    SEARCH_INPUT_CLASS = 'search-global-typeahead__input'

    FILTER_PEOPLE_BUTTON_XPATH = f'//button[contains(., "{LinkedInButtons.PEOPLE_FILTER}")]'
    FILTER_REGION_BUTTON_XPATH = f'//button[contains(., "{LinkedInButtons.REGION_FILTER}")]'
    FILTER_REGION_UKRAINE_BUTTON_XPATH = f'//span[contains(., "{LinkedInButtons.UKRAINE_REGION_FILTER}")]'
    SHOW_RESULT_COUNTRY_BUTTON_XPATH = f'{FILTER_REGION_BUTTON_XPATH}/../..//button[contains(., "{LinkedInButtons.SHOW_RESULT_BUTTON}")]'
    FILTER_CONTACTS_BUTTON_XPATH = f'//button[contains(., "{LinkedInButtons.CONTACTS_FILTER}")]'
    FILTER_CONTACTS_FIRST_BUTTON_XPATH = f'//span[contains(., "{LinkedInButtons.FIRST_CONTACT_FILTER}")]'
    SHOW_RESULT_CONTACTS_BUTTON_XPATH = f'{FILTER_CONTACTS_BUTTON_XPATH}/../..//button[contains(., "{LinkedInButtons.SHOW_RESULT_BUTTON}")]'

    MAKE_CONTACT_BUTTON_XPATH = f'//button[contains(., "{LinkedInButtons.CONNECT_BUTTON}")]'
    SEND_CONTACT_BUTTON_XPATH = f'//button[contains(., "{LinkedInButtons.SEND_BUTTON}")]'
    NEXT_BUTTON_XPATH = f'//button[contains(., "{LinkedInButtons.NEXT_BUTTON}")]'

    OK_BUTTON_XPATH = f'//span[contains(., "{LinkedInButtons.OK_BUTTON}")]'
    SKIP_BUTTON_XPATH = f'//button[contains(@aria-label, "Пропустить") and @data-test-modal-close-btn]'

    SEND_MESSAGE_BUTTON_XPATH = f'//button[contains(., "{LinkedInButtons.SEND_MESSAGE_BUTTON}")]'
    MESSAGE_INPUT_CLASS = "msg-form__contenteditable"
    ADD_FILE_BUTTON_XPATH = f'//button[contains(., "{LinkedInButtons.ADD_FILE_TO_DRAFT_BUTTON}") or contains(@title,"{LinkedInButtons.ADD_FILE_TO_OBSERVATION_BUTTON}")]'
    FOR_MESSAGE_SEND_BUTTON_XPATH = "//button[contains(., 'Отправить') and contains(@class, 'msg-form__send-button')]"


class LinkedInPopups:
    """LinkedIn pop-up notification windows."""
    POPUP_WINDOW_XPATH = "//div[contains(@class, 'artdeco-modal') and contains(@class, 'artdeco-modal--layer-default')]"
    POPUP_WINDOW_SET_CONTACT_XPATH = "//div[contains(@class, 'artdeco-modal-overlay') and contains(@class, 'artdeco-modal-overlay--layer-default')]"


class SearchProfession:
    """Profession to search on LinkedIn contacts."""
    PYTHON = 'python'
    HR = 'hr'


class LinkedInProfessionAndLimits:
    """LinkedIn search limits constants."""
    PROFESSIONS_AND_PAGE_LIMITS = [
        (SearchProfession.HR, 100),
        (SearchProfession.PYTHON, 100),
    ]
