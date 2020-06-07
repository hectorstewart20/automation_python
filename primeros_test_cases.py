import unittest
from selenium import webdriver
import time

class PrimerosTestCases(unittest.TestCase):


    def test_search_word_dont_exist(self):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('http://automationpractice.com/index.php')
        driver.maximize_window()
        driver.find_element_by_id('search_query_top').send_keys('hector')
        driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        self.assertEqual('No results were found for your search "hector"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text)
      
    def test_search_word_dont_exist2(self):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('http://automationpractice.com/index.php')
        driver.find_element_by_id('search_query_top').send_keys('hector')
        driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        self.assertEqual('No results were found for your search "hector"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text)
        driver.close()
        driver.quit()

    def test_click_contactUs(self):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('http://automationpractice.com/index.php')
        driver.find_element_by_partial_link_text('Contact').click()
        time.sleep(2)
        boton_file = driver.find_element_by_xpath('//*[@id="uniform-fileUpload"]/span[2]')
        self.assertTrue(boton_file.is_displayed()," Se mostro el boton")
        driver.close()
        driver.quit()


if __name__ == "__main__":
    unittest.main()