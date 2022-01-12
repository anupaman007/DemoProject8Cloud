import pytest
from selenium import webdriver
from PageObjects.CloudLoginPage import LoginPage
from Utilities import ScreenshotUtilities
import time
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from Utilities import XLUtilis


class Test_002_Login_DDT:
    baseURL = ReadConfig.getApplicationURL()
    path = r"C:\Users\user\PycharmProjects\pythonProject\pythonProject\8Cloud\TestData\
            Automation Test_WorksheetExcel3.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("*****************Test_002_Login_DDT********************")
        self.logger.info("*****************Verifying login test********************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.rows = XLUtilis.getRowCount(self.path, 'Sheet1')
        print("Number of rows in excel", self.rows)

        last_status = []  # Empty array

        for r in range(2, self.rows + 1):
            self.Username = XLUtilis.readData(self.path, 'Sheet1', r, 1)
            self.Password = XLUtilis.readData(self.path, 'Sheet1', r, 2)
            self.Expected = XLUtilis.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.Username)
            self.lp.setPassword(self.Password)
            self.lp.clickLogin()
            time.sleep(5)

            actual_title = self.driver.title
            exp_title = "8cloud | Login"

            if actual_title == exp_title:
                if self.Expected == "Pass":
                    self.logger.info("*******Passed********")
                    self.lp.clickLogout()
                    last_status.append("Pass")
                elif self.Expected == "Fail":
                    self.logger.info("*******Fail********")
                    self.lp.clickLogout()
                    last_status.append("Pass")
            elif actual_title != exp_title:
                if self.Expected == "Pass":
                    self.logger.info("*******Failed********")
                    last_status.append("Fail")
                elif self.Expected == "Fail":
                    self.logger.info("*******Passed********")
                    last_status.append("Pass")

        if "Fail" not in last_status:
            self.logger.info("**********Login DDT test passed************")
            self.driver.close()
            assert True
        else:
            self.logger.info("**********Login DDT test failed************")
            self.driver.close()
            assert False
        self.logger.info("****************End of login DDT test***************")
        self.logger.info("*****************Completed Test_002_DDT_Login***********************")
