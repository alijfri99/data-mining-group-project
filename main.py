from selenium import webdriver
from subject_finder import SubjectFinder
from course_finder import CourseFinder
from data_extractor import DataExtractor

PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
INITIAL_URL = "https://www.gla.ac.uk/coursecatalogue/browsebysubjectarea/"
driver = webdriver.Chrome(PATH)

# subject_finder = SubjectFinder(driver, INITIAL_URL)
# subjects = subject_finder.find_subjects()

# course_finder = CourseFinder(driver, subjects)
# courses = course_finder.find_courses()

data_extractor = DataExtractor(driver, ["https://www.gla.ac.uk/coursecatalogue/course/?code=COMPSCI5095"])
data = data_extractor.extract_data()
print(data)