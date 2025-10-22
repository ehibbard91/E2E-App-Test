from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

class MainFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)


    # Locators
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Enter password']")
    HOME_SCREEN = (By.XPATH, "//span[text()='Home']")
    GO_TO_BUTTON = (By.CSS_SELECTOR, "a[href='/fact-checking-tool']")
    COMPANY_NAME_INPUT = (By.NAME, "companyName")
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    SSN_FIELD = (By.NAME, "ssnNumber")
    STARTUP_NAME = (By.NAME, "startupName")
    JOB_TITLE = (By.NAME, "jobTitle")
    UPLOAD_RESUME_BUTTON = (By.XPATH, "//label[input[@name='resume']]")
    UPLOAD_OTHER_DOCS_BUTTON = (By.XPATH, "//label[input[@name='otherDocs']]")
    SUBMIT_BUTTON = (By.XPATH, "//button[.//span[text()='Fact Check']]")
    INPUT_RESUME = (By.NAME, "resume")
    INPUT_OTHER_DOCS = (By.NAME, "otherDocs")
    REMOVE_RESUME_BTN = (By.XPATH, "//span[contains(@title,'Resume')]/following-sibling::button")
    REMOVE_DOCS_BTN = (By.XPATH, "//span[contains(@title,'Demo')]/following-sibling::button")
    RESUME_PROGRESS = (By.XPATH, "//label[contains(text(),'Resume')]/following::div[contains(@class,'bg-gray-200')][1]")
    OTHER_DOCS_PROGRESS = (By.XPATH, "//label[contains(text(),'Other Docs')]/following::div[contains(@class,'bg-gray-200')][1]")
    RESUME_FILE = (By.XPATH, "//span[contains(@title,'.pdf') and contains(@title,'Resume')]")
    OTHER_DOCS_FILE = (By.XPATH, "//span[@title='Demo Pitch Deck.pdf']")
    WAIT_SCREEN = (By.XPATH, "//h2[contains(text(), 'Analyzing Documents')]")


    # Helper locator method
    def get_elem(self, locator):
        return self.driver.find_element(*locator)

# Home page navigation
    def login(self, pswd):
        password = self.get_elem(self.PASSWORD_INPUT)
        password.click()
        password.send_keys(pswd)
        password.send_keys(Keys.ENTER)

    def get_home_page(self):
        return self.get_elem(self.HOME_SCREEN)

    def click_goto_button(self):
        self.get_elem(self.GO_TO_BUTTON).click()
        return self.driver.current_url

# Getter methods: locate and return page elements without performing actions
    def get_company_name(self):
        return self.get_elem(self.COMPANY_NAME_INPUT)

    def get_first_name(self):
        return self.get_elem(self.FIRST_NAME_INPUT)

    def get_last_name(self):
        return self.get_elem(self.LAST_NAME_INPUT)

    def get_ssn(self):
        return self.get_elem(self.SSN_FIELD)

    def get_startup_name(self):
        return self.get_elem(self.STARTUP_NAME)

    def get_job_title(self):
        return self.get_elem(self.JOB_TITLE)

    def get_upload_resume_button(self):
        return self.get_elem(self.UPLOAD_RESUME_BUTTON)

    def get_upload_other_docs_button(self):
        return self.get_elem(self.UPLOAD_OTHER_DOCS_BUTTON)

    def get_submit_button(self):
        return self.get_elem(self.SUBMIT_BUTTON)

    def is_fact_check_button_disabled(self):
        return self.get_submit_button().get_attribute("disabled") is not None

    def get_wait_screen(self):
        return self.get_elem(self.WAIT_SCREEN)

# Action methods to interact with form fields
    def enter_first_name(self, name):
        self.get_elem(self.FIRST_NAME_INPUT).send_keys(name)

    def enter_last_name(self, name):
        self.get_elem(self.LAST_NAME_INPUT).send_keys(name)

    def enter_ssn(self, ssn):
        self.get_elem(self.SSN_FIELD).send_keys(ssn)

    def enter_company_name(self, company_name):
        self.get_elem(self.COMPANY_NAME_INPUT).send_keys(company_name)

    def enter_startup_name(self, startup_name):
        self.get_elem(self.STARTUP_NAME).send_keys(startup_name)

    def enter_job_title(self, job_title):
        self.get_elem(self.JOB_TITLE).send_keys(job_title)

    def upload_resume(self, filename: str):
        file_path = Path(__file__).parent.parent.parent / "test_data" / filename
        self.driver.find_element(self.INPUT_RESUME[0], self.INPUT_RESUME[1]).send_keys(str(file_path))
        self.wait.until(EC.invisibility_of_element_located(self.RESUME_PROGRESS))

    def upload_other_docs(self, filename: str):
        file_path = Path(__file__).parent.parent.parent / "test_data" / filename
        self.driver.find_element(self.INPUT_OTHER_DOCS[0], self.INPUT_OTHER_DOCS[1]).send_keys(str(file_path))
        self.wait.until(EC.invisibility_of_element_located(self.OTHER_DOCS_PROGRESS))

    def fast_resume_upload(self, filename: str):
        file_path = Path(__file__).parent.parent.parent / "test_data" / filename
        self.driver.find_element(self.INPUT_RESUME[0], self.INPUT_RESUME[1]).send_keys(str(file_path))

    def fast_doc_upload(self, filename: str):
        file_path = Path(__file__).parent.parent.parent / "test_data" / filename
        self.driver.find_element(self.INPUT_OTHER_DOCS[0], self.INPUT_OTHER_DOCS[1]).send_keys(str(file_path))

    def remove_resume(self):
        self.get_elem(self.REMOVE_RESUME_BTN).click()

    def remove_otherdocs(self):
         self.get_elem(self.REMOVE_DOCS_BTN).click()

    def click_submit(self):
        self.get_elem(self.SUBMIT_BUTTON).click()

    def wait_for_report(self, timeout=280):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(self.WAIT_SCREEN))