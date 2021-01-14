import unittest
from Config.Driver import Driver
from Web_Pages.Main_Page import Main_Page



class AOS_TESTS(unittest.TestCase):

    def setUp(self):
        self.browser = Driver().browser

    def test_quantity_popup_checkout(self):
        page = Main_Page(self.browser)
        page.load()

    def tearDown(self):
        print('s')


if __name__ == '__main__':
    unittest.main()

