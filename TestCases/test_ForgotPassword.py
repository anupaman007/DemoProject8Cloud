from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.CloudLoginPage import LoginPage


class Test_008_Forgot_Password:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_forgot_password(self, setup):
        self.logger.info("*********** Test_008_Forgot_Password ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("*********** maximize_window ************")
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.logger.info("*********** Login Page ************")
        self.lp.clickOnForgotPassword()
        self.logger.info("*********** Clicked on the I Forgot My Password ************")

        self.logger.info("*********************** Password Rest Page is open *****************")
        self.lp.enterEmailAddress("anupama@8-tree.com")
        self.logger.info("*********************** Email address entered *****************")
        self.lp.clickOnRestPassword()
        self.lp.clickOnBackToLogin()
        self.logger.info("*********************** Email sent to you for Password rest *****************")
