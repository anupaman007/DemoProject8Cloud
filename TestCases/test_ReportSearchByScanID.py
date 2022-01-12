import pytest

from PageObjects.CloudLoginPage import LoginPage
from PageObjects.ProjectPage import ProjectPage
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from PageObjects.ReportPage import ReportPage
import time


class Test_018_ReportSearchByScanID:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    # @pytest.mark.regression
    def test_ReportSearchByScanID(self, setup):
        self.logger.info("************ Starting Test_018_ReportSearchByScanID Test *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful **************")

        self.driver.implicitly_wait(20)

        rpage = ReportPage(self.driver)
        time.sleep(5)
        rpage.clickOnListReport()

        self.driver.implicitly_wait(20)

        rpage.setScanID("46444")
        time.sleep(5)
        status = rpage.searchReportByScanID("46444")
        time.sleep(5)
        assert True == status

        self.logger.info("*************** Search Successful **************")
        self.logger.info("************ Completed Test_018_ReportSearchByScanID Test *************")

