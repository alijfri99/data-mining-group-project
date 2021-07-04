class DataExtractor:
    def __init__(self, driver, subjects):
        self.driver = driver
        self.subjects = subjects

    def extract_data(self):
        for subject in self.subjects:
            self.driver.get(subject)
            element = self.driver.find_element_by_xpath("//a[@href='JavaScript:printCatalogue()']")
            element.click()
            
