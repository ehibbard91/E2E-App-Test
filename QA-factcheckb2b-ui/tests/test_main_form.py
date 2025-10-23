import pytest_check as check
from src.pages.education_page import EducationPage
from src.pages.main_form_page import MainFormPage
from src.pages.experience_page import ExperiencePage

def test_main_form(driver):
    page = MainFormPage(driver)

# Tests and navigates through home screen to form page
    page.login("")
    page.get_home_page()
    page.click_goto_button()
# List of getters to check on the form page
    form_getters = [
        page.get_company_name,
        page.get_first_name,
        page.get_last_name,
        page.get_ssn,
        page.get_startup_name,
        page.get_job_title,
        page.get_upload_resume_button,
        page.get_upload_other_docs_button,
        page.get_submit_button
    ]

# Loop over form getters and check display
    for getter in form_getters:
        try:
            elem = getter()
            check.is_true(elem.is_displayed(), f"FAILED on: {getter.__name__}")
        except Exception as e:
            check.is_true(False, f"EXCEPTION in {getter.__name__}: {e}")

    check.is_true(page.is_fact_check_button_disabled(), "Fact check button should be disabled")

    # Fill out form fields and validate values
    actions = [
        (page.enter_company_name, page.COMPANY_NAME_INPUT, "Company Name"),
        (page.enter_first_name, page.FIRST_NAME_INPUT, "John"),
        (page.enter_last_name, page.LAST_NAME_INPUT, "Smithereens"),
        (page.enter_ssn, page.SSN_FIELD, "123456789", "***-**-6789"),
        (page.enter_startup_name, page.STARTUP_NAME, "Startup Name"),
        (page.enter_job_title, page.JOB_TITLE, "CFO")
    ]

    for action in actions:
        enter_func, field, value = action[:3]
        obfuscated = action[3] if len(action) > 3 else None
        enter_func(value)
        try:
            actual = page.get_elem(field).get_attribute("value")
            expected = obfuscated if obfuscated else value
            check.equal(actual, expected, f"Value mismatch for {field}")
        except Exception as e:
            check.is_true(False, f"EXCEPTION checking field {field}: {e}")

    page.upload_resume("John Smithereens Resume.pdf")
    resume_elem = page.get_elem(page.RESUME_FILE)
    assert resume_elem.is_displayed()
    assert "John Smithereens Resume.pdf" in resume_elem.get_attribute("title")

    page.upload_other_docs("Demo Pitch Deck.pdf")
    docs_elem = page.get_elem(page.OTHER_DOCS_FILE)
    assert docs_elem.is_displayed()
    assert "Demo Pitch Deck.pdf" in docs_elem.get_attribute("title")

    page.remove_resume()
    assert page.get_elem(page.UPLOAD_RESUME_BUTTON).text.strip() == "+ Upload Docs"

    page.remove_otherdocs()
    assert page.get_elem(page.UPLOAD_OTHER_DOCS_BUTTON).text.strip() == "+ Upload Docs"

    page.fast_resume_upload("John Smithereens Resume.pdf")
    page.fast_doc_upload("Demo Pitch Deck.pdf")

    page.click_submit()
    assert page.get_wait_screen().is_displayed()

    page.wait_for_report()

# Hands over control to the reports_page.py POM file. Runs Report Page tests
    edu = EducationPage(driver)

    # List of all element getter functions
    elements_to_check = [
        edu.get_company_name,
        edu.get_startup_name_sidebar,
        edu.get_name_header,
        edu.get_startup_name,
        edu.get_education_button_sidebar,
        edu.get_experience_button_sidebar,
        edu.get_license_button_sidebar,
        edu.get_background_check_sidebar,
        edu.get_education_button,
        edu.get_experience_button,
        edu.get_license_button,
        edu.get_background_check,
        edu.get_verification_score,
        edu.get_suitability_score,
        edu.get_see_more_button_verification,
        edu.get_see_more_button_suitability,
        # University 1
        edu.get_university_name_1,
        edu.get_university_badge_1,
        edu.get_degree_title_1,
        edu.get_degree_badge_1,
        edu.get_attendance_1,
    #    edu.get_grad_date_1,
    #    edu.get_grad_badge,
        edu.get_major_1,
        edu.get_major_1_badge,
        edu.get_see_more_major,
        edu.get_minor_1,
        edu.get_see_more_minor,
        edu.get_honors_program_1,
        edu.get_academic_honors_1,
        # University 2
        edu.get_university_name_2,
        edu.get_university_badge_2,
        edu.get_degree_title_2,
        edu.get_degree_badge_2,
        edu.get_attendance_2,
    #    edu.get_grad_date_2,
    #    edu.get_grad_badge_2,
        edu.get_major_2,
        edu.get_major_badge_2,
        edu.get_minor_2,
        edu.get_minor_badge_2,
        edu.get_honors_program_2,
        edu.get_academic_honors_2
    ]

    # Loop once over the list
    for getter in elements_to_check:
        try:
            elem = getter()
            check.is_true(elem.is_displayed(), f"FAILED on: {getter.__name__}")
        except Exception as e:
            check.is_true(False, f"EXCEPTION in {getter.__name__}: {e}")

# Clicks experience btn and hands over control to experience_page.py POM file
    btn = edu.press_experience_button()
    check.is_true("bg-[#8aecb3]" in btn.get_attribute("class"), "Experience button did not activate")

    exp_page = ExperiencePage(driver)
    all_data = exp_page.get_employer_data()
    assert len(all_data) > 0, "No experience blocks found on Experience page"

    for i, exp_values in enumerate(all_data, start=1):
        for j, value in enumerate(exp_values, start=1):

            assert value, f"Experience {i} field {j} is empty"
