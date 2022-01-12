import pytest

from PageObjects.CloudLoginPage import LoginPage
from PageObjects.ProjectPage import ProjectPage
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from PageObjects.ReportPage import ReportPage
import time


class Test_007_ReportDownload:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    # @pytest.mark.regression
    def test_ReportDownload(self, setup):
        self.logger.info("************ Starting Test_007_ReportDownload Test *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful **************")

        self.driver.implicitly_wait(20)
        self.RP = ReportPage(self.driver)
        self.RP.clickOnListReport()

        self.driver.implicitly_wait(20)
        self.RP.clickOnSearchBox("29112")
        self.logger.info("*************** Search Successful **************")

        self.driver.implicitly_wait(20)
        self.RP.clickOnDownloadButton()

        self.logger.info("*************** Download button clicked Successfully **************")
        self.logger.info("************ Completed Test_007_ReportDownload Test *************")

