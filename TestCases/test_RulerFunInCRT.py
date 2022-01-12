from PageObjects.CloudLoginPage import LoginPage
from PageObjects.ProjectPage import ProjectPage
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from PageObjects.CRTPage import CRTPage
import time
import pytest


class Test_028_RulerFunInCRT:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_RulerFunInCRT(self, setup):
        self.logger.info("*********** Test_028_RulerFunInCRT ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful **************")

        self.driver.implicitly_wait(20)
        self.SP = CRTPage(self.driver)
        self.logger.info("*************** Scan Page Called **************")

        self.driver.implicitly_wait(30)
        time.sleep(5)
        self.SP.clickOnScanPage()
        self.logger.info("*************** Scan Page Displayed **************")

        self.driver.implicitly_wait(30)
        time.sleep(10)
        self.SP.clickOnSearchBox("41070")
        # self.SP.clickOnSearchBox("47248")

        self.logger.info("*************** Searching for the data **************")
        self.logger.info("*************** Application loading **************")

        self.driver.implicitly_wait(30)
        time.sleep(10)
        self.SP.RulerFunInCRT()

        self.logger.info("*************** Ending Test_028_RulerFunInCRT **************")