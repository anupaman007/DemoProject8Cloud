from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class ReportPage:
    lnkListReport_xpath = "/html/body/div[2]/aside[1]/section/ul/li[6]/ul/li[1]/a/span"

    txtSearchBox_xpath = "//*[@id='datatable_filter']/label/input"

    btnInfo_xpath = "//*[@id='29315']/td[8]/a[1]"

    btnDownloadButton_xpath = "//*[@id='29315']/td[8]/a[2]"

    txtDesBox_xpath = "//*[@id='details_Description']/i"
    txtKeyInForDesBox_id = "activeinput"

    btnTickMarkToSaveDesData_xpath = "//*[@id='details_Description']/i[1]"
    btnCrossMarkToUnsaveDesData_xpath = "//*[@id='details_Description']/i[2]"

    wholetable_xpath = "/html/body/div[2]/aside[2]/section[2]/div/div/div/div[2]/div/div[2]/div/table"
    tableRows_xpath = "/html/body/div[2]/aside[2]/section[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr"
    tableColumns_xpath = "/html/body/div[2]/aside[2]/section[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td"

    btnDelete_xpath = "/html/body/div[2]/aside[2]/section[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/" \
                      "tr[1]/td[8]/i"
    btnDelNo_id = "yesNoConfirmationDialogButtonNo"
    btnDelYes_id = "yesNoConfirmationDialogButtonYes"

    ddShow_xpath = "//*[@id='datatable_length']/label/select"

    def __init__(self, driver):
        self.driver = driver

    def clickOnListReport(self):
        self.driver.implicitly_wait(30)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.lnkListReport_xpath).click()

    def clickOnDownloadButton(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.btnDownloadButton_xpath).click()

    def clickOnSearchBox(self, value):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.txtSearchBox_xpath).send_keys(value)

    def clickOnInfoButton(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.btnInfo_xpath).click()

    def clickOnDesBox(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.txtDesBox_xpath).click()

    def setDataInDesBox(self, value):
        self.driver.find_element_by_id(self.txtKeyInForDesBox_id).clear()
        self.driver.find_element_by_id(self.txtKeyInForDesBox_id).send_keys(value)

    def clickOnTickMark(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.btnTickMarkToSaveDesData_xpath).click()

    def clickOnCrossMark(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.btnCrossMarkToUnsaveDesData_xpath).click()

    def setProjectName(self, pname):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.txtSearchBox_xpath).clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.txtSearchBox_xpath).send_keys(pname)

    def setScanID(self, scanid):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.txtSearchBox_xpath).clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.txtSearchBox_xpath).send_keys(scanid)

    def setReportID(self, reportid):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.txtSearchBox_xpath).clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.txtSearchBox_xpath).send_keys(reportid)

    def setCreatedAt(self, createdt):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.txtSearchBox_xpath).clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.txtSearchBox_xpath).send_keys(createdt)

    def setReportBy(self, reportby):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.txtSearchBox_xpath).clear()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.txtSearchBox_xpath).send_keys(reportby)

    def clickOnDeleteButton(self):
        self.driver.implicitly_wait(30)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.btnDelete_xpath).click()

    def clickDeleteNo(self):
        self.driver.implicitly_wait(30)
        time.sleep(5)
        self.driver.find_element_by_id(self.btnDelNo_id).click()

    def clickDeleteYes(self):
        self.driver.implicitly_wait(30)
        time.sleep(3)
        self.driver.find_element_by_id(self.btnDelYes_id).click()

    def clickShowDropDown(self):
        self.driver.implicitly_wait(30)
        time.sleep(3)
        element = self.driver.find_element_by_xpath(self.ddShow_xpath)
        dropdown = Select(element)
        dropdown.select_by_visible_text("25")

    # ---------------------------------- To verify the Report Validate/Verification -----------------------------------

    def getNoOfRows(self):
        self.driver.implicitly_wait(30)
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        self.driver.implicitly_wait(30)
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchReportByProjectName(self, pname):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            time.sleep(5)
            table = self.driver.find_element_by_xpath(self.wholetable_xpath)
            time.sleep(5)
            projectname = table.find_element_by_xpath("//*[@id='datatable']/tbody/tr["+str(r)+"]/td[2]").text
            time.sleep(5)
            if projectname == pname:
                time.sleep(5)
                flag = True
                break
        return flag

    def searchReportByScanID(self, scanid):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            time.sleep(5)
            table = self.driver.find_element_by_xpath(self.wholetable_xpath)
            time.sleep(5)
            scanidvalue = table.find_element_by_xpath("//*[@id='datatable']/tbody/tr["+str(r)+"]/td[3]").text
            time.sleep(5)
            if scanidvalue == scanid:
                time.sleep(5)
                flag = True
                break
        return flag

    def searchReportByReportID(self, reportid):    # reportid = 4689 which will take to search and reportidvalueincol = 46891 this value if present in the table and matches with "reportid" test case=PASS else test case=FAIL
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            time.sleep(5)
            table = self.driver.find_element_by_xpath(self.wholetable_xpath)
            time.sleep(5)
            reportidvalueincol = table.find_element_by_xpath("//*[@id='datatable']/tbody/tr["+str(r)+"]/td[4]").text
            time.sleep(5)
            if reportidvalueincol == reportid:
                time.sleep(5)
                flag = True
                break
        return flag

    def searchReportByCreatedAt(self, datetime):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            time.sleep(5)
            table = self.driver.find_element_by_xpath(self.wholetable_xpath)
            time.sleep(5)
            datetimevaluepresent = table.find_element_by_xpath("//*[@id='datatable']/tbody/tr["+str(r)+"]/td[5]").text
            time.sleep(5)
            if datetimevaluepresent == datetime:
                time.sleep(5)
                flag = True
                break
        return flag

    def searchReportByReportBy(self, reportcreatedby):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            time.sleep(5)
            table = self.driver.find_element_by_xpath(self.wholetable_xpath)
            time.sleep(5)
            reportcreatedbyincol = table.find_element_by_xpath("//*[@id='datatable']/tbody/tr["+str(r)+"]/td[6]").text
            time.sleep(5)
            if reportcreatedbyincol == reportcreatedby:
                time.sleep(5)
                flag = True
                break
        return flag

