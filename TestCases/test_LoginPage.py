import pytest
from selenium import webdriver
from PageObjects.CloudLoginPage import LoginPage
from Utilities import ScreenshotUtilities
import time
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.logger.info("*********************Test_001_Login************************")
        self.logger.info("******************Verifying Home Page title**********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "8cloud | Login":
            ScreenshotUtilities.screenshot(setup)
            self.driver.close()
            assert True
            self.logger.info("*****************Home Page title test is passed********************")
        else:
            self.logger.error("*****************Home Page title test is failed********************")
            assert False

    def test_login(self, setup):
        self.logger.info("***************** Verifying login test ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        # self.driver.close()
        if act_title != "8cloud":
            time.sleep(5)
            ScreenshotUtilities.screenshot(setup)
            # wait = WebDriverWait(self.lp.driver, 10)  # maximum time to wait until the element is ready
            # element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='topnavbar']/div/ul/li[3]/a/span")))
            # element.click()
            # time.sleep(3)
            # self.lp.clickLogout()

            self.logger.info("*****************Login test is passed********************")
            assert True
        else:
            self.logger.error("*****************Login test is fail********************")
            assert False

