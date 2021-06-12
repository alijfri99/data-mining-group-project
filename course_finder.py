class CourseFinder:
    def __init__(self, driver, subjects):
        self.driver = driver
        self.subjects = subjects

    def find_courses(self) -> list:
        result = list()
        for subject in self.subjects:
            self.driver.get(subject)
            courses = self.driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/main/div[1]/form/"
                                                         "div/ul/li/a")
            for course in courses:
                result.append(course.get_attribute('href'))
        return result
