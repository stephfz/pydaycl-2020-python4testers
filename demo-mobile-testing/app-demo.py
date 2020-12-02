import os
import unittest
from appium import webdriver
import time

class SpotifyAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'StephGalaxy'
        desired_caps['appPackage'] = "com.spotify.music"
        desired_caps['appActivity'] = 'com.spotify.music.MainActivity'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.quit()

    def test_search_artist(self):
        element = self.driver.find_element_by_xpath(
                        '//android.widget.ImageView[@content-desc="Search"]')
        element.click()
        self.driver.find_element_by_id("com.spotify.music:id/find_search_field_text").click()
        artist = 'Pearl Jam'
        self.driver.find_element_by_id("com.spotify.music:id/query").send_keys(artist)
        time.sleep(2)
        locator =  "//android.widget.TextView[@text = 'Pearl Jam']"
        element = self.driver.find_element_by_xpath(
                        "//android.widget.TextView[@text = '{0}']".format("Pearl Jam"))
        assert element != None
