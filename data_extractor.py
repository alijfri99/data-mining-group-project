class DataExtractor:
    def __init__(self, driver, courses):
        self.driver = driver
        self.courses = courses

    def extract_data(self):
        result = list()
        for course in self.courses:
            course_data = list()
            self.driver.get(course)
            course_data.append("University of Glasgow")
            course_data.append("Glas")
            course_data.append(self.extract_course_school())
            course_data.append(self.extract_course_title())
            course_data.append(self.extract_course_aims())

            result.append(course_data)
        return result

    def extract_course_school(self):
        school = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/main/div[1]/ul/li[2]")
        return school.text[8:]

    def extract_course_title(self):
        course_title = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/main/div[1]/h2")
        return course_title.text

    def extract_course_aims(self):
        course_aims = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/main/div[1]/div[7]")
        return course_aims.text
