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

    def getAllFishData(self):
        self.getFirstTableFishData()
        self.getSecondTableFishData()

    def getFirstTableFishData(self):
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
                cellText = driver.find_element(By.XPATH, finalXPath).text

                self.getFishIcon(finalXPath)
                self.getFishName(finalXPath, cellText)
                self.getFishLocation(finalXPath, cellText)
                self.getFishTime(finalXPath, cellText)
                self.getFishSeason(finalXPath, cellText)
                self.getFishWeather(finalXPath, cellText)
    
    def getSecondTableFishData(self):
        before_XPath  = "/html/body/div[3]/div[3]/div[5]/div/table[2]/tbody/tr["
        aftertd_XPath = "]/td["
        aftertr_XPath = "]"

        collumnXPath = "/html/body/div[3]/div[3]/div[5]/div/table[2]/thead[2]/tr[1]/th"
        rowXPath = '/html/body/div[3]/div[3]/div[5]/div/table[2]/tbody[1]/tr'
      
        collumnRow =  webDriverApp.getTableRowsCollumn(collumnXPath, rowXPath)
        n_collumn = int(collumnRow[0])
        n_row = int(collumnRow[1])

        for table_row in range(1, (n_row)):
            print("Getting Data...")
            for table_column in range(1, (n_collumn)):
                finalXPath = before_XPath + str(table_row) + aftertd_XPath + str(table_column) + aftertr_XPath
                cellText = driver.find_element(By.XPATH, finalXPath).text

                self.getFishIcon(finalXPath)
                self.getFishName(finalXPath, cellText)
                self.getFishLocation(finalXPath, cellText)
                self.getFishTime(finalXPath, cellText)
                self.getFishSeason(finalXPath, cellText)
                self.getFishWeather(finalXPath, cellText)
        print(fishNames)

    def getFishIcon(self, finalXPath):
        if finalXPath.find("td[1]") != -1:
            fishIconSrc = driver.find_element(By.XPATH, finalXPath + "/div/div/a/img").get_attribute("src")
            fishIcon.append(str(fishIconSrc))
        
    def getFishName(self, finalXPath, cellText):
        if finalXPath.find("td[2]") != -1:
            fishNames.append(cellText)

    def getFishLocation(self, finalXPath, cellText):    
            if finalXPath.find("td[7]") != -1:
                fishLocation.append(cellText)

    def getFishTime(self, finalXPath, cellText):    
            if finalXPath.find("td[8]") != -1:
                fishTime.append(cellText)

    def getFishSeason(self, finalXPath, cellText):    
            if finalXPath.find("td[9]") != -1:
                fishSeason.append(cellText)
                
    def getFishWeather(self, finalXPath, cellText):    
                if finalXPath.find("td[10]") != -1:
                    fishWeather.append(cellText)
                    
