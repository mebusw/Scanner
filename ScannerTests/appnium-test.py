"""Be sure to use the latest selenium version
as there might be some problems with JSON serialization

Before running the test make sure you started appium server
with TestApp app: grunt appium:TestApp
"""
import unittest
import os
from random import randint
from selenium import webdriver


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        # set up appium
        # app = os.path.join(os.path.dirname(__file__),
        #                    '../../apps/TestApp/build/Release-iphonesimulator',
        #                    'TestApp.app')
        # app = os.path.abspath(app)
        app = '/Users/jacky/Library/Developer/Xcode/DerivedData/Scanner-dqjuhfkafslszccqsdanmwzceztq/Build/Products/Debug-iphonesimulator/Scanner.app'
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'browserName': '',
                'device': 'iPhone Simulator',
                'platform': 'Mac',
                'version': '7.1',
                'app': app
            })
        self._values = []

    def _populate(self):
        # populate text fields with two random number
        elems = self.driver.find_elements_by_tag_name('textField')
        for elem in elems:
            rndNum = randint(0, 10)
            elem.send_keys(rndNum)
            self._values.append(rndNum)

    def test_ui_computation(self):
        # populate text fields with values
        self._populate()

        inputs = self.driver.find_elements_by_name("123")
        self.assertEqual(inputs[0].text, '123')


        # trigger computation by using the button
        buttons = self.driver.find_elements_by_name("Scan")
        buttons[0].click()


        # # is sum equal ?
        # texts = self.driver.find_elements_by_tag_name("staticText")
        # self.assertEqual(int(texts[0].text), self._values[0] + self._values[1])

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()