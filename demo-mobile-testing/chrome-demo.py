import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ChromeDemoTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'ephGalaxy'
        desired_caps['browserName'] = 'Chrome'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_cod_envio_inexistente(self):
        time.sleep(2)
        self.driver.get('https://track24.net/service/chilexp/tracking/')
        try:
            element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, "inputTrackCode")))
        except TimeoutException:
            print ("Element not Found")
        element.send_keys("FRMO $6")
        self.driver.find_element_by_id("trackingButton").click()
        time.sleep(2)
        element = self.driver.find_element_by_class_name("text-danger")
        assert element != None



#appium --allow-insecure chromedriver_autodownload
