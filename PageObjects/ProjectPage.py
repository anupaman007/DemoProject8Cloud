import time
from selenium.webdriver.support.ui import Select
from PageObjects.CloudLoginPage import LoginPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ProjectPage:
    drpProjectSort_id = "ordercriteria"

    lnkNotification_xpath = "//*[@id='topnavbar']/div/ul/li[2]/a"

    lnkMangNotfSub_xpath = "//*[@id='topnavbar']/div/ul/li[2]/ul/li[3]/a"

    lnkAddNotfSub_xpath = "//*[@id='pagecontent']/aside[2]/section[2]/div/div/div/div[1]/div/button"

    iframeCRT_id = "crtiframe"

    drpEventType_id = "noteventtype"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSorting(self, value):
        self.driver.implicitly_wait(20)
        drp = Select(self.driver.find_element_by_id(self.drpProjectSort_id))
        drp.select_by_visible_text(value)

    def clickNotificationIcon(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.lnkNotification_xpath).click()

    def clickMangNotfSub(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.lnkMangNotfSub_xpath).click()

    def clickAddNotfSub(self):
        self.driver.implicitly_wait(20)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.lnkAddNotfSub_xpath)))
        element.click()
        time.sleep(10)
        self.driver.find_element_by_xpath(self.lnkAddNotfSub_xpath).click()

    def clickEventType(self, value):
        self.driver.implicitly_wait(10)
        iframe = self.driver.find_element_by_id(self.iframeCRT_id)
        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.drpEventType_id).click()
        self.driver.switch_to.default_content()
        drp = Select(self.driver.find_element_by_id(self.drpEventType_id))
        drp.select_by_visible_text(value)








