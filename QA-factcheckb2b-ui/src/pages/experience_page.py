from selenium.webdriver.common.by import By

class ExperiencePage:
    EMPLOYER_CHUNKS = "//div[contains(@class,'border-2 border-[#296ddc]')]"

    def __init__(self, driver):
        self.driver = driver

    def get_employer_data(self):
        employers = []
        chunks = self.driver.find_elements(By.XPATH, self.EMPLOYER_CHUNKS)

        for chunk in chunks:
            # First h4 is the block title, skip it
            h4_elements = chunk.find_elements(By.XPATH, ".//h4")
            values = [h4.text.strip() for h4 in h4_elements[1:]]  # skip first
            employers.append(values)

        return employers