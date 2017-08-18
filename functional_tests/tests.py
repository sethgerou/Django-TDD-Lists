from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

class NewVisiortTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):

        MAX_WAIT = 10
        start_time = time.time()

        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn('row_text', [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # look at served page
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: go grocery shopping')

        # the text box to add an item is still present.  User enters "pressure wash driveway".
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('pressure wash driveway')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # page updates again and both items are present.
        self.wait_for_row_in_list_table('1: go grocery shopping')
        self.wait_for_row_in_list_table('2: pressure wash driveway')

        # site has generated a unique url and informed user.
        self.fail('Finish the test!')
        # user can visit that url to view todo list.
