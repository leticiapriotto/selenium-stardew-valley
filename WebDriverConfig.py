from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class WebDriverConfig:

    def __init__(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())

    def openBrowser(self, webLink):
        driver.get(webLink)
        return driver
        #driver.maximize_window()

    def getTableRowsCollumn(self, collumnXPath, rowXPath):
        columns = len(driver.find_elements(By.XPATH, collumnXPath))
        rows = len(driver.find_elements(By.XPATH, rowXPath))
        print(f"Columns = {repr(columns)}\nRows = {repr(rows)}")

        return columns, rows

    def closeBrowser(self):
        driver.close()

