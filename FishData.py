from sqlite3 import Row
from WebDriverConfig import WebDriverConfig
from selenium.webdriver.common.by import By

class FishData:
    def __init__(self):
        global fishNames, fishIcon, fishLocation, fishTime, fishSeason, fishWeather
        global webDriverApp, driver
        webDriverApp = WebDriverConfig()
        driver = webDriverApp.openBrowser("https://stardewvalleywiki.com/Fish")
        
        fishIcon = []
        fishNames = []
        fishLocation = []
        fishTime = []
        fishSeason = []
        fishWeather = []

    def getFishData(self):
        before_XPath  = "//div/table[1]/tbody[1]/tr["
        aftertd_XPath = "]/td["
        aftertr_XPath = "]"

        collumnXPath = "//table[1]/thead/tr[1]/th"
        rowXPath = '//div/table[1]/tbody[1]/tr'
      
        collumnRow =  webDriverApp.getTableRowsCollumn(collumnXPath, rowXPath)
        n_collumn = int(collumnRow[0])
        n_row = int(collumnRow[1])

        for table_row in range(1, (n_row)):
            print("Getting Data...")
            for table_column in range(1, (n_collumn)):
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
                    
        print("\nAll done!\n")
        print(fishNames)

        webDriverApp.closeBrowser()

