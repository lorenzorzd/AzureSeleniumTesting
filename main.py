import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\ancastro\Development/chromedriver.exe")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.rpachallenge.com/")
        self.assertIn("Rpa Challenge", driver.title)
        elem = driver.find_element(By.PARTIAL_LINK_TEXT, "Search")
        elem.click()
        
        elem =  driver.find_element(By.TAG_NAME,'input')
        elem.send_keys("AntMan")
        elem.send_keys(Keys.RETURN)

        #self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
