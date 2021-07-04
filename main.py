from selenium import webdriver
from subject_finder import SubjectFinder
from course_finder import CourseFinder
import pickle
from data_extractor import DataExtractor

PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
INITIAL_URL = "https://www.gla.ac.uk/coursecatalogue/browsebysubjectarea/"
driver = webdriver.Chrome(PATH)

# subject_finder = SubjectFinder(driver, INITIAL_URL)
# subjects = subject_finder.find_subjects()

'''
course_finder = CourseFinder(driver, subjects)
courses = course_finder.find_courses()
courses_output_file = open('courses.bin', 'wb')
pickle.dump(courses, courses_output_file)
courses_output_file.close()
'''
courses_file = open('courses.bin', 'rb')
courses = pickle.load(courses_file)
courses_file.close()

print(courses, len(courses))
