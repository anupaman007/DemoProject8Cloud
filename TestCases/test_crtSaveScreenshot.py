from PageObjects.CloudLoginPage import LoginPage
from PageObjects.ProjectPage import ProjectPage
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from PageObjects.ScanPage import ScanPage
import time
import pytest


class Test_025_crtSaveScreenshot:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    # @pytest.mark.regression
    def test_crtSaveScreenshot(self, setup):
        self.logger.info("*********** Test_025_crtSaveScreenshot ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful **************")

        self.driver.implicitly_wait(20)
        self.SP = ScanPage(self.driver)
        self.logger.info("*************** Scan Page Called **************")

        self.driver.implicitly_wait(20)
        self.SP.clickOnScanPage()
        self.logger.info("*************** Scan Page Displayed **************")

        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.SP.clickOnSearchBox("46444")
        self.logger.info("*************** Searching for the data **************")
        self.logger.info("*************** Data Found **************")

        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.SP.crtSaveScreenshot()

        self.logger.info("*************** Ending Test_025_crtSaveScreenshot **************")
