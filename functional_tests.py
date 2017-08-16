from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisiortTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # look at served page
        self.browser.get('http://localhost:8000')

        # look for To-Do in page title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # user can add a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        # user types in "go grocery shopping"
        inputbox.send_keys('go grocery shopping')
        # when user hits enter, page updates and lists "1. go grocery shopping" is shown in the list.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # the text box to add an item is still present.  User enters "pressure wash driveway".
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('pressure wash driveway')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # page updates again and both items are present.
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: go grocery shopping', [row.text for row in rows])
        self.assertIn('2: pressure wash driveway', [row.text for row in rows])

        # site has generated a unique url and informed user.
        self.fail('Finish the test!')
        # user can visit that url to view todo list.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
