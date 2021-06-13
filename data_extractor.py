class DataExtractor:
    def __init__(self, driver, subjects):
        self.driver = driver
        self.subjects = subjects

    def extract_all_subjects_data(self):
        result = {}
        for subject in self.subjects:
            self.driver.get(subject)
            self.click_print_friendly_btn()
            page_courses = self.extract_all_courses_in_page()
            result = {**result, **page_courses}
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
            elif node.tag_name == 'h3':
                current_attribute = node.get_attribute('innerText')
                all_courses_data[current_course][current_attribute] = []
            else:
                try:
                    all_courses_data[current_course][current_attribute].append(node.get_attribute('innerText'))
                except KeyError:
                    pass
        return all_courses_data
