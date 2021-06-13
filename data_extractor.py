class DataExtractor:
    def __init__(self, driver, subjects):
        self.driver = driver
        self.subjects = subjects

    def extract_all_subjects_data(self):
        result = {}
        result['all_courses'] = []
        subjects_done_count = 0
        for subject in self.subjects:
            self.driver.get(subject)
            self.click_print_friendly_btn()
            page_courses = self.extract_all_courses_in_page()
            for key, value in page_courses.items():
                value['Course Name'] = key
                result['all_courses'].append(value)
            subjects_done_count += 1
            print(f'{subjects_done_count} of {len(self.subjects)} subjects done ')
        return result

    def click_print_friendly_btn(self):
        print_friendly_btn_xpath = "//a[contains(text(),'in print friendly format')]"
        print_friendly_btn = self.driver.find_element_by_xpath(print_friendly_btn_xpath)
        print_friendly_btn.click()

    def extract_all_courses_in_page(self):
        all_information_nodes_xpath = "//div[contains(@class,'maincontent')]/*"
        all_information_nodes = self.driver.find_elements_by_xpath(all_information_nodes_xpath)
        print(f'all_information_nodes count : {len(all_information_nodes)}')

        all_courses_data = {}
        current_course = ''
        current_attribute = ''
        for node in all_information_nodes:
            if node.tag_name == 'h2':
                current_course = node.get_attribute('innerText')
                all_courses_data[current_course] = {}
                current_attribute = 'Course Name'
            elif node.tag_name == 'h3':
                current_attribute = node.get_attribute('innerText')
                all_courses_data[current_course][current_attribute] = ''
            else:
                if current_attribute == 'Course Name':
                    child_elements_titles = node.find_elements_by_xpath('.//strong')
                    child_elements_data = node.find_elements_by_xpath('./*')
                    for i in range(len(child_elements_titles)):
                        title = child_elements_titles[i].get_attribute('innerText')
                        text = child_elements_data[i].get_attribute('innerText').replace(title, '')
                        all_courses_data[current_course][title] = text

                else:
                    try:
                        all_courses_data[current_course][current_attribute] += node.get_attribute('innerText')
                    except KeyError:
                        pass
        return all_courses_data
