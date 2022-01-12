import time
from selenium.webdriver.support.ui import Select
from PageObjects.CloudLoginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class SearchUser:
    dropdownAccount_xpath = "//*[@id='topnavbar']/div/ul/li[3]/a/span"
    buttonAdvanceView_xpath = "//*[@id='topnavbar']/div/ul/li[3]/ul/li[2]/div[2]/div/div/label[2]"

    linkUser_xpath = "//*[@id='pagecontent']/aside[1]/section/ul/li[8]/ul/li/a/span"
    textSearchBox_xpath = "//*[@id='datatable_filter']/label/input"

    wholetable_sub_sub_xpath = "/html/body/div[2]/aside[2]/section[2]/div[1]/div/div/" \
                               "div[2]/div/div[2]/div/div/div[2]/table"
    tableRows_xpath = "/html/body/div[2]/aside[2]/section[2]/div[1]/div/div/div[2]/div/div[2]/div/" \
                      "div/div[2]/table/tbody/tr"
    tableColumns_xpath = "/html/body/div[2]/aside[2]/section[2]/div[1]/div/div/div[2]/" \
                         "div/div[2]/div/div/div[2]/table/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def clickOnAccountdropdown(self):
        # self.driver.implicitly_wait(20)
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.dropdownAccount_xpath)))
        element.click()
        time.sleep(5)

    def clickOnAdvanceViewButtonON(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.buttonAdvanceView_xpath)))
        element.click()
        time.sleep(5)

    def clickOnUser(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.linkUser_xpath)))
        element.click()
        time.sleep(3)

    def setEmail(self, email):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.textSearchBox_xpath).clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.textSearchBox_xpath).send_keys(email)

    def setFirstname(self, fname):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.textSearchBox_xpath).clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.textSearchBox_xpath).send_keys(fname)

    def setLastname(self, lname):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.textSearchBox_xpath).clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.textSearchBox_xpath).send_keys(lname)

    def setJob(self, job):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.textSearchBox_xpath).clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.textSearchBox_xpath).send_keys(job)

    def setScannerUserLevel(self, scanner):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.textSearchBox_xpath).clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.textSearchBox_xpath).send_keys(scanner)

    # ---------------------------------- To verify the Search User Validate/Verification -----------------------------------
    def getNoOfRows(self):
        self.driver.implicitly_wait(30)
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        self.driver.implicitly_wait(30)
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchUserByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            time.sleep(5)
            table = self.driver.find_element_by_xpath(self.wholetable_sub_sub_xpath)
            time.sleep(5)
            emailid = table.find_element_by_xpath("//*[@id='datatable']/tbody/tr["+str(r)+"]/td[3]").text
            time.sleep(5)
            if emailid == email:
                time.sleep(5)
                flag = True
                break
        return flag

    def searchUserByFName(self, fname):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.wholetable_sub_sub_xpath)
            fnamecol = table.find_element_by_xpath("//*[@id='datatable']/tbody/tr["+str(r)+"]/td[4]").text
            if fnamecol == fname:
                flag = True
                break
        return flag

    def searchUserByLName(self, lname):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.wholetable_sub_sub_xpath)
            lnamecol = table.find_element_by_xpath("//*[@id='datatable']/tbody/tr["+str(r)+"]/td[5]").text
            if lnamecol == lname:
                flag = True
                break
        return flag

    def searchUserByJob(self, job):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.wholetable_sub_sub_xpath)
            jobcol = table.find_element_by_xpath("//*[@id='datatable']/tbody/tr["+str(r)+"]/td[6]").text
            if jobcol == job:
                flag = True
                break
        return flag

    def searchUserByScannerUserLevel(self, scanner):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.wholetable_sub_sub_xpath)
            scannercol = table.find_element_by_xpath("//*[@id='datatable']/tbody/tr["+str(r)+"]/td[7]").text
            if scannercol == scanner:
                flag = True
                break
        return flag
