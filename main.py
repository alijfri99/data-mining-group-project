from selenium import webdriver
from subject_finder import SubjectFinder

PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
SUBJECTS_URL = "https://www.gla.ac.uk/coursecatalogue/browsebysubjectarea/"
driver = webdriver.Chrome(PATH)

subject_finder = SubjectFinder(driver, SUBJECTS_URL)
subjects = subject_finder.find_subjects()
print(subjects)
