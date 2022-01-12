import time
from idlelib.multicall import r
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from PageObjects.CloudLoginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class CRTPage:
    lnkScanPage_xpath = "//*[@id='pagecontent']/aside[1]/section/ul/li[4]/a/span"
    txtSearchBox_xpath = "//*[@id='datatable_filter']/label/input"
    lnkRowInActionColumn_xpath = "/html/body/div[2]/aside[2]/section[2]/div/div/div/div[3]/div/div[2]/div/table/" \
                                 "tbody/tr"
    lnkColumnInActionColumn_xpath = "/html/body/div[2]/aside[2]/section[2]/div/div/div/div[3]/div/div[2]/" \
                                    "div/table/tbody/tr/td"
    btnCRTInActionColumn_xpath = "/html/body/div[2]/aside[2]/section[2]/div/div/div/div[3]/div/div[2]/div/table/" \
                                 "tbody/tr/td[7]/a[1]/i"

    # ************************************* Switch to CRT Frame ******************************************
    iframeCRT_id = "crtiframe"
    lnkSavedResultPopUpWindow_xpath = "/html/body/soo-app/div/soo-eight-cloud-reporting-page/div/div[2]/" \
                                      "scan-panel-app/crt-data-selection-dialog/div/div/div/div[2]/ul/a[1]"
    imageAreaClick_xpath = "//*[@id='interactiv-container']"
    plusBtn_xpath = "//*[@id='wheelnav-piemenu-slice-0']"
    btnROI_xpath = "//*[@id='wheelnav-piemenu_sub-slice-2']"

    clickOnDent_xpath = "//*[@id='6']"
    roiCircle_xpath = "//*[@id='roi-info-annotation-0']"
    createReportBtn_xpath = "//*[@id='wheelnav-piemenu_context-slice-0']"
    confirmBtnForReportGeneration_xpath = "//*[@id='ReportSettingsDialog']/div/div/div[3]/button[2]"

    # ************************************ Connect All ******************************************************
    btnMax_xpath = "//*[@id='wheelnav-piemenu_sub-slice-1']"
    # btnEdge_xpath = "//*[@id='wheelnav-piemenu_sub-slice-0']"

    btnErase_xpath = "//*[@id='toolboxheader']/button[8]/i"
    btnConfirm_xpath = "//*[@id='CrtConfirmationDialog']/div/div/div[3]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnScanPage(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.lnkScanPage_xpath).click()

    def clickOnSearchBox(self, scanid):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.txtSearchBox_xpath).send_keys(scanid)

    # --------------------------- START = Used for test_OpenCRT.py script ---------------------------------------------
    def setActionColumn(self):
        self.driver.implicitly_wait(10)

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.btnCRTInActionColumn_xpath)))
        element.click()
        time.sleep(5)
        print("CRT Open")
        self.driver.implicitly_wait(20)
        iframe = self.driver.find_element_by_id(self.iframeCRT_id)
        self.driver.switch_to.frame(iframe)
        time.sleep(5)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.lnkSavedResultPopUpWindow_xpath).click()
        time.sleep(5)
        print("Saved Result is loaded on CRT")
        self.driver.implicitly_wait(30)
        self.driver.switch_to.default_content()
        time.sleep(5)
    # --------------------------- End = Used for test_OpenCRT.py script ---------------------------------------------

    # ------------------------ Distance ruler function -------------------------------------------------
    def RulerFunInCRT(self):
        self.driver.implicitly_wait(10)

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.btnCRTInActionColumn_xpath)))
        element.click()
        time.sleep(5)
        print("CRT Open")

        self.driver.implicitly_wait(10)
        time.sleep(5)

        iframe = self.driver.find_element_by_id(self.iframeCRT_id)
        time.sleep(5)
        self.driver.implicitly_wait(10)

        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(10)
        time.sleep(5)

        # Code for generating report for newly uploaded scan
        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath(self.imageAreaClick_xpath).click()
            print("Clicked on the scan image - Single Scan")
        # Code for more than one result saved in CRT
        except:
            self.driver.implicitly_wait(20)
            time.sleep(5)
            self.driver.find_element_by_xpath(self.lnkSavedResultPopUpWindow_xpath).click()
            print("Saved Result is loaded on CRT")
            self.driver.implicitly_wait(30)
            self.driver.switch_to.default_content()
            time.sleep(5)

            self.driver.switch_to.frame(iframe)
            self.driver.implicitly_wait(20)

            self.driver.find_element_by_xpath(self.imageAreaClick_xpath).click()
            print("Clicked on the scan image - Multiple Scans")
        # ----------------------------------------------------------------------------------------------------------
        element = self.driver.find_element_by_id("wheelnav-piemenu-slice-1")
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform()
        print("Clicked on Connect All option")
        time.sleep(5)
        self.driver.find_element_by_xpath(self.btnMax_xpath).click()
        print("Connected all dents max-to-max")

        self.driver.find_element_by_xpath(self.btnErase_xpath).click()
        print("Clicked on Erase All")
        time.sleep(5)
        self.driver.find_element_by_xpath(self.btnConfirm_xpath).click()
        print("Erase All >> Confirm")

        self.driver.close()


