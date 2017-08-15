from selenium import webdriver
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
        self.fail('Finish the test!')

        # user can add a to-do item

        # user types in "go grocery shopping"

        # when user hits enter, page updates and lists "1. go grocery shopping" is shown in the list.

        # the text box to add an item is still present.  User enters "pressure wash driveway".

        # page updates again and both items are present.

        # site has generated a unique url and informed user.

        # user can visit that url to view todo list.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    
