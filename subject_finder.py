class SubjectFinder:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_subjects(self) -> list:
        result = list()
        self.driver.get(self.url)
        links = self.driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/main/div[1]/ul/li/a")
        for link in links:
            result.append(link.get_attribute('href'))
        return result
