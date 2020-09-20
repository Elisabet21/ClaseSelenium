from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

tc=unittest.TestCase('__init__')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_id('search_query_top').send_keys('hola')
driver.find_element_by_name('submit_search').click()
time.sleep(2)
tc.assertEqual('No results were found for your search "hola"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text)
driver.close()
driver.quit()

