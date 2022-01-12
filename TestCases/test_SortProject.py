from PageObjects.CloudLoginPage import LoginPage
from PageObjects.ProjectPage import ProjectPage
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen


class Test_003_ProjectPage:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_ProjectPage(self, setup):
        self.logger.info("************ Starting Test_003_ProjectPage Test *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful **************")

        self.logger.info("************* Clicked on the Project Name *****************")

        self.driver.implicitly_wait(20)
        self.OP = ProjectPage(self.driver)
        self.driver.implicitly_wait(20)
        self.OP.clickOnSorting("ID (↑)")

        self.logger.info("*************** Sorting completed *******************")







