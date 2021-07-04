from selenium import webdriver
from subject_finder import SubjectFinder
from data_extractor import DataExtractor

import json
import platform

if platform.system() == 'Windows':
    PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
else:
    PATH = "/home/parsas/Documents/projects/chromedriver"
INITIAL_URL = "https://www.gla.ac.uk/coursecatalogue/browsebysubjectarea/"
driver = webdriver.Chrome(PATH)

subject_finder = SubjectFinder(driver, INITIAL_URL)
subjects = subject_finder.find_subjects()

# course_finder = CourseFinder(driver, subjects)
# courses = course_finder.find_courses()

data_extractor = DataExtractor(driver, subjects)
data = data_extractor.extract_all_subjects_data()

with open('data7.json', 'w') as fp:
    json.dump(data, fp, indent=4)

driver.close()
