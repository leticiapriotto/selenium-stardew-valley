from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class WebDriverConfig:
    def __init__(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())

    def openWebDriver(self):
        global driver
        driver.get("https://stardewvalleywiki.com")
        #driver.maximize_window()
        #sleep(2)

    def openPage(self, xPathLink):
        global driver
        driver.find_element(By.XPATH, xPathLink).click()
        #sleep(2) 
        
    def gettingFirstTableFishNames(self):
        global driver
        columns = len (driver.find_elements(By.XPATH, "//table[1]/thead/tr[1]/th"))
        rows = len (driver.find_elements(By.XPATH, '//div/table[1]/tbody[1]/tr'))
        imgs = len (driver.find_elements(By.XPATH, '//div/table[1]/tbody[1]/tr'))
        print(f"Columns = {repr(columns)}\nRows = {repr(rows)}")
        #sleep(8)

        before_XPath  = "//div/table[1]/tbody[1]/tr["
        aftertd_XPath = "]/td["
        aftertr_XPath = "]"


        fishIcon = []
        fishNames = []
        fishLocation = []
        fishTime = []
        fishSeason = []
        fishWeather = []
        for table_row in range(1, (rows)):
            print("reading rows...")
            for table_column in range(1, (columns + 1)):
                finalXPath = before_XPath + str(table_row) + aftertd_XPath + str(table_column) + aftertr_XPath
                cell_text = driver.find_element(By.XPATH, finalXPath).text

                if finalXPath.find("td[1]") != -1:
                    fishIconSrc = driver.find_element(By.XPATH, finalXPath + "/div/div/a/img").get_attribute("src")
                    fishIcon.append(str(fishIconSrc))
                  
                if finalXPath.find("td[2]") != -1:
                    fishNames.append(cell_text)
                
                if finalXPath.find("td[7]") != -1:
                    fishLocation.append(cell_text)

                if finalXPath.find("td[8]") != -1:
                    fishTime.append(cell_text)

                if finalXPath.find("td[9]") != -1:
                    fishSeason.append(cell_text)

                if finalXPath.find("td[10]") != -1:
                    fishWeather.append(cell_text)

        print("All done!")

    def closeWebDriver(self):
        global driver
        driver.close()

fishLink = "(//a[normalize-space()='Fish'])[1]"
    
web = WebDriverConfig()
web.openWebDriver()
web.openPage(fishLink)
web.gettingFirstTableFishNames()
web.closeWebDriver()

