from PageObjects.CloudLoginPage import LoginPage
from PageObjects.ProjectPage import ProjectPage
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen


class Test_004_NotificationIcon:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_notificationIcon(self, setup):
        self.logger.info("*********** Test_004_NotificationIcon ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful **************")

        self.driver.implicitly_wait(20)
        self.NI = ProjectPage(self.driver)
        self.logger.info("*************** Loads Project Page **************")

        self.driver.implicitly_wait(20)
        self.NI.clickNotificationIcon()
        self.logger.info("*************** Click On Bell Notification  **************")

        self.driver.implicitly_wait(20)
        self.NI.clickMangNotfSub()
        self.logger.info("*************** Click On Manage Notification Subscription **************")

        self.driver.implicitly_wait(20)
        self.NI.clickAddNotfSub()
        self.logger.info("*************** Click On Add Notification Subscription **************")
        self.logger.info("*************** Add New Item page display**************")

        self.driver.implicitly_wait(20)
        self.NI.clickEventType("Result Modified")
        self.logger.info("*************** Notification Test Completed ***********************")