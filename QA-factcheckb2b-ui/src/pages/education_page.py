from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EducationPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    COMPANY_NAME = (By.XPATH, "//p[normalize-space(text())='Company Name']")
    STARTUP_NAME_SIDEBAR = (By.XPATH, "//span[contains(@class,'text-[#296ddc]')][contains(@class,'font-medium')][.='Startup Name']")
    NAME_HEADER = (By.XPATH, "//h1[contains(normalize-space(.),'John Smithereens')]")
    STARTUP_NAME = (By.XPATH, "//span[contains(@class,'text-lg') and normalize-space(.)='Startup Name']")
    EDUCATION_BUTTON_SIDEBAR = (By.XPATH, "//button[normalize-space(text())='Education']")
    EXPERIENCE_BUTTON_SIDEBAR = (By.XPATH, "//button[normalize-space(text())='Experience']")
    LICENSE_BUTTON_SIDEBAR = (By.XPATH, "//button[normalize-space(text())='License']")
    BACKGROUND_CHECK_SIDEBAR = (By.XPATH, "//button[normalize-space(text())='Background Check']")
    EDUCATION_BUTTON = (By.XPATH, "//button[contains(@class,'bg-[#8aecb3]') and text()='Education']")
    EXPERIENCE_BUTTON = (By.XPATH, "//button[contains(@class,'bg-gray-100') and text()='Experience']")
    LICENSE_BUTTON = (By.XPATH, "//button[contains(@class,'bg-gray-100') and text()='License']")
    BACKGROUND_CHECK = (By.XPATH, "//button[contains(@class,'bg-gray-100') and text()='Background Check']")
    VERIFICATION_SCORE = (By.XPATH, "//h3[normalize-space(text())='Verification Score']/following::p[contains(text(), '%')][1]")
    SUITABILITY_SCORE = (By.XPATH, "//h3[normalize-space(text())='Suitability Score']/following::p[contains(text(), '%')][1]")
    SEE_MORE_BUTTON_VERIFICATION = (By.XPATH, "//h3[normalize-space(text())='Verification Score']/following::button[normalize-space(text())='See more'][1]")
    SEE_MORE_BUTTON_SUITABILITY = (By.XPATH, "//h3[normalize-space(text())='Suitability Score']/following::button[normalize-space(text())='See more'][1]")
    UNIVERSITY_NAME_1 = (By.XPATH, "(//div[@class='bg-white p-4 rounded-lg relative'])[1]//h4[normalize-space(text())='VS Hometown University']")
    UNIVERSITY_BADGE_1 = (By.XPATH, "(//img[@alt='verified by equifax badge'])[1]")
    DEGREE_TITLE_1 = (By.XPATH, "//div[.//p[normalize-space(text())='Degree Title']]//h4[normalize-space(text())='Master of Science']")
    DEGREE_BADGE_1 = (By.XPATH, "(//img[@alt='verified by equifax badge'])[2]")
    ATTENDANCE_1 = (By.XPATH, "(//h4[normalize-space(text())='N/A'])[1]")
    GRAD_DATE_1 = (By.XPATH, "//div[.//p[normalize-space(text())='Date of Degree Award']]//h4[normalize-space(text())='1997']")
    GRAD_BADGE = (By.XPATH, "(//div[.//p[normalize-space(text())='Date of Degree Award']]//img[@alt='mismatch equifax verification icon'])[1]")
    MAJOR_1 = (By.XPATH, "(//div[p[normalize-space(text())='Major Courses']]//h4[normalize-space(text())='Engineering'])[1]")
    MAJOR_1_BADGE = (By.XPATH, "(//img[@alt='verified by equifax badge'])[3]")
    SEE_MORE_MAJOR = (By.XPATH, "//div[p[normalize-space(text())='Major Courses']]//button[starts-with(normalize-space(text()),'Show More')]")
    MINOR_1 = (By.XPATH, "(//h4[normalize-space(text())='N/A'])[2]")
    SEE_MORE_MINOR = (By.XPATH, "//div[p[normalize-space(text())='Minor Courses']]//button[starts-with(normalize-space(text()),'Show More')]")
    HONORS_PROGRAM_1 = (By.XPATH, "(//h4[normalize-space(text())='N/A'])[3]")
    ACADEMIC_HONORS_1 = (By.XPATH, "(//h4[normalize-space(text())='N/A'])[4]")
    UNIVERSITY_NAME_2 = (By.XPATH, "(//div[.//p[normalize-space(text())='University']]//h4[normalize-space(text())='VS Hometown University'])[2]")
    UNIVERSITY_BADGE_2 = (By.XPATH, "(//img[@alt='verified by equifax badge'])[4]")
    DEGREE_TITLE_2 = (By.XPATH, "//div[.//p[normalize-space(text())='Degree Title']]//h4[normalize-space(text())='BS']")
    DEGREE_BADGE_2 = (By.XPATH, "(//img[@alt='verified by equifax badge'])[5]")
    ATTENDANCE_2 = (By.XPATH, "(//h4[normalize-space(text())='N/A'])[5]")
    GRAD_DATE_2 = (By.XPATH, "//div[.//p[normalize-space(text())='Date of Degree Award']]//h4[normalize-space(text())='1995']")
    GRAD_BADGE_2 = (By.XPATH, "(//div[.//p[normalize-space(text())='Date of Degree Award']]//img[@alt='mismatch equifax verification icon'])[1]")
    MAJOR_2 = (By.XPATH, "(//div[p[normalize-space(text())='Major Courses']]//h4[normalize-space(text())='Engineering'])[2]")
    MAJOR_BADGE_2 = (By.XPATH, "(//img[@alt='ai prediction information icon'])[1]")
    MINOR_2 = (By.XPATH, "//h4[normalize-space(text())='Computer Science']")
    MINOR_BADGE_2 = (By.XPATH, "(//img[@alt='ai prediction information icon'])[2]")
    HONORS_PROGRAM_2 = (By.XPATH, "(//h4[normalize-space(text())='N/A'])[6]")
    ACADEMIC_HONORS_2 = (By.XPATH, "(//h4[normalize-space(text())='N/A'])[7]")

    def get_elem(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
# Sidebar and Header Elements

    def get_company_name(self):
        return self.get_elem(self.COMPANY_NAME)

    def get_startup_name_sidebar(self):
        return self.get_elem(self.STARTUP_NAME_SIDEBAR)

    def get_name_header(self):
        return self.get_elem(self.NAME_HEADER)

    def get_startup_name(self):
        return self.get_elem(self.STARTUP_NAME)

    def get_education_button_sidebar(self):
        return self.get_elem(self.EDUCATION_BUTTON_SIDEBAR)

    def get_experience_button_sidebar(self):
        return self.get_elem(self.EXPERIENCE_BUTTON_SIDEBAR)

    def get_license_button_sidebar(self):
        return self.get_elem(self.LICENSE_BUTTON_SIDEBAR)

    def get_background_check_sidebar(self):
        return self.get_elem(self.BACKGROUND_CHECK_SIDEBAR)

    def get_education_button(self):
        return self.get_elem(self.EDUCATION_BUTTON)

    def get_experience_button(self):
        return self.get_elem(self.EXPERIENCE_BUTTON)

    def get_license_button(self):
        return self.get_elem(self.LICENSE_BUTTON)

    def get_background_check(self):
        return self.get_elem(self.BACKGROUND_CHECK)

    def get_verification_score(self):
        return self.get_elem(self.VERIFICATION_SCORE)

    def get_suitability_score(self):
        return self.get_elem(self.SUITABILITY_SCORE)

    def get_see_more_button_verification(self):
        return self.get_elem(self.SEE_MORE_BUTTON_VERIFICATION)

    def get_see_more_button_suitability(self):
        return self.get_elem(self.SEE_MORE_BUTTON_SUITABILITY)

# University 1
    def get_university_name_1(self):
        return self.get_elem(self.UNIVERSITY_NAME_1)

    def get_university_badge_1(self):
        return self.get_elem(self.UNIVERSITY_BADGE_1)

    def get_degree_title_1(self):
        return self.get_elem(self.DEGREE_TITLE_1)

    def get_degree_badge_1(self):
        return self.get_elem(self.DEGREE_BADGE_1)

    def get_attendance_1(self):
        return self.get_elem(self.ATTENDANCE_1)

    def get_grad_date_1(self):
        return self.get_elem(self.GRAD_DATE_1)

    def get_grad_badge(self):
        return self.get_elem(self.GRAD_BADGE)

    def get_major_1(self):
        return self.get_elem(self.MAJOR_1)

    def get_major_1_badge(self):
        return self.get_elem(self.MAJOR_1_BADGE)

    def get_see_more_major(self):
        return self.get_elem(self.SEE_MORE_MAJOR)

    def get_minor_1(self):
        return self.get_elem(self.MINOR_1)

    def get_see_more_minor(self):
        return self.get_elem(self.SEE_MORE_MINOR)

    def get_honors_program_1(self):
        return self.get_elem(self.HONORS_PROGRAM_1)

    def get_academic_honors_1(self):
        return self.get_elem(self.ACADEMIC_HONORS_1)

    # University 2
    def get_university_name_2(self):
        return self.get_elem(self.UNIVERSITY_NAME_2)

    def get_university_badge_2(self):
        return self.get_elem(self.UNIVERSITY_BADGE_2)

    def get_degree_title_2(self):
        return self.get_elem(self.DEGREE_TITLE_2)

    def get_degree_badge_2(self):
        return self.get_elem(self.DEGREE_BADGE_2)

    def get_attendance_2(self):
        return self.get_elem(self.ATTENDANCE_2)

    def get_grad_date_2(self):
        return self.get_elem(self.GRAD_DATE_2)

    def get_grad_badge_2(self):
        return self.get_elem(self.GRAD_BADGE_2)

    def get_major_2(self):
        return self.get_elem(self.MAJOR_2)

    def get_major_badge_2(self):
        return self.get_elem(self.MAJOR_BADGE_2)

    def get_minor_2(self):
        return self.get_elem(self.MINOR_2)

    def get_minor_badge_2(self):
        return self.get_elem(self.MINOR_BADGE_2)

    def get_honors_program_2(self):
        return self.get_elem(self.HONORS_PROGRAM_2)

    def get_academic_honors_2(self):
        return self.get_elem(self.ACADEMIC_HONORS_2)

    def press_experience_button(self):
        btn = self.get_elem(self.EXPERIENCE_BUTTON)
        btn.click()
        return btn
