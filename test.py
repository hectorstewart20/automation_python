from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
driver.maximize_window()
driver.find_element_by_id('search_query_top').send_keys('holaa')
driver.find_element_by_name('submit_search').click()
time.sleep(1)
msg_error = driver.find_element_by_xpath('//*[@id="center_column"]/p')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/a').click()
time.sleep(2)
driver.find_element_by_partial_link_text('omen').click()
time.sleep(2)
tc.assertEqual('No results were found for your search "holaa"',msg_error.text)
driver.close()
driver.quit()

