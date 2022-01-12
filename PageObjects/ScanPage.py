import time
from idlelib.multicall import r

from selenium.webdriver.support.ui import Select
from PageObjects.CloudLoginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ScanPage:
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

    # ****************************************** Functions In CRT Variables ******************************
    # ********** Close CRT Button **********************
    lnkCloseCRT_xpath = "//*[@id='crtiframedialog']/div/div/div[1]/button/span"

    # ********** Save Result button in CRT *************
    btnSaveResult_xpath = "//*[@id='toolboxheader']/button[2]"
    btnSaveResultOkButton_xpath = "//*[@id='NormalMessageDialog']/div/div/div[3]/button"

    # ********** Version Control button ****************
    btnVersionControlButton_xpath = "//*[@id='toolboxheader']/button[9]/i"
    btnVersionCrtButtonClose_xpath = "//*[@id='CrtInfoDialog']/div/div/div[3]/button"

    # ********** Save Screenshot from CRT **************
    btnSaveScreenshot_xpath = "/html/body/soo-app/div/soo-eight-cloud-reporting-page/div/div[2]/" \
                              "scan-panel-app/crt-data-selection-dialog/div/div/div/div[2]/ul/a[1]/span/img"

    # ********** Click on Image ************************
    imageAreaClick_xpath = "//*[@id='interactiv-container']"
    eyeButtonOnPie_xpath = "//*[@id='wheelnav-piemenu-title-2']"
    eyeButtonOnPie2_xpath = "//*[@id='wheelnav-piemenu_sub-slice-1']"

    plusBtn_xpath = "//*[@id='wheelnav-piemenu-slice-0']"

    btnROI_xpath = "//*[@id='wheelnav-piemenu_sub-slice-2']"

    clickOnDent_xpath = "//*[@id='3']"
    roiCircle_xpath = "//*[@id='roi-info-annotation-0']"
    createReportBtn_xpath = "//*[@id='wheelnav-piemenu_context-slice-0']"
    confirmBtnForReportGeneration_xpath = "//*[@id='ReportSettingsDialog']/div/div/div[3]/button[2]"
    # *********************** Share Scan ******************************************************************
    btnSelectRow_xpath = "/html/body/div[2]/aside[2]/section[2]/div/div/div/div[3]/div/div[2]/div/table/tbody/" \
                         "tr"
    btnShareIcon_xpath = "/html/body/div[2]/aside[2]/section[2]/div/div/div/div[1]/div/button[3]/i"

    btnShareButton_xpath = "/html/body/div[2]/aside[2]/div[4]/div/div/div[3]/div[1]/button[2]"
    btnOpenWithMailClient_xpath = "/html/body/div[2]/aside[2]/div[4]/div/div/div[2]/div[2]/ul/div/a"
    btnCloseShareYourDataWindow_xpath = "/html/body/div[2]/aside[2]/div[4]/div/div/div[3]/div[2]/button"

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

    def clickToCloseCRT(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.lnkCloseCRT_xpath).click()

    # --------------------------- END = Used for test_OpenCRT.py script ---------------------------------------------

    # --------------------------  START = Used for test_crtVersion.py script ----------------------------------------
    def crtVersion(self):
        self.driver.implicitly_wait(10)

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.btnCRTInActionColumn_xpath)))
        element.click()
        time.sleep(5)
        print("CRT Open")
        self.driver.implicitly_wait(30)
        iframe = self.driver.find_element_by_xpath(self.iframeCRT_id)
        self.driver.switch_to.frame(iframe)
        time.sleep(3)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(self.lnkSavedResultPopUpWindow_xpath).click()
        time.sleep(5)
        print("Saved Result is loaded on CRT")
        self.driver.implicitly_wait(30)
        self.driver.switch_to.default_content()
        time.sleep(5)

        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.btnVersionControlButton_xpath).click()
        time.sleep(5)
        print("CRT Version window Opened")
        self.driver.find_element_by_xpath(self.btnVersionCrtButtonClose_xpath).click()
        time.sleep(5)
        print("CRT Version window closed")
        self.driver.implicitly_wait(30)
        self.driver.switch_to.default_content()

        # --------------------------  END = test_crtVersion.py script -----------------------------------

        # --------------------------  START = test_crtSaveScreenshot.py script --------------------------
    def crtSaveScreenshot(self):
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

        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.btnSaveScreenshot_xpath).click()
        time.sleep(5)
        print("Click on Save Screenshot button")
        self.driver.implicitly_wait(30)
        self.driver.switch_to.default_content()

        # --------------------------  END = test_crtSaveScreenshot.py script --------------------------

        # --------------------------  START = test_crtRoi.py script --------------------------
    def crtRoi(self):
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
        element = self.driver.find_element_by_id("wheelnav-piemenu-slice-0")
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform()
        print("Clicked on plus more options")
        time.sleep(5)

        self.driver.find_element_by_xpath(self.btnROI_xpath).click()
        print("Clicked on ROI button")

        self.driver.implicitly_wait(30)
        time.sleep(5)

        self.driver.find_element_by_xpath(self.clickOnDent_xpath).click()
        print("Clicked on the dent")
        time.sleep(5)

        self.driver.find_element_by_xpath(self.roiCircle_xpath).click()
        print("Clicked on the Region of interest")
        time.sleep(5)

        self.driver.find_element_by_xpath(self.createReportBtn_xpath).click()
        print("Clicked on create report button")
        time.sleep(5)

        ele = self.driver.find_element_by_xpath("//*[@id='reportTemplateId']")
        dropdown = Select(ele)
        self.driver.implicitly_wait(10)
        dropdown.select_by_visible_text("31706 - 8cloud Example Report Template (8cloud global)")
        print("Selected the setting template")
        time.sleep(5)

        self.driver.find_element_by_xpath(self.confirmBtnForReportGeneration_xpath).click()
        print("Clicked Confirm")
        print("Report Generated successfully")
        time.sleep(5)

        self.driver.switch_to.default_content()
        # --------------------------  END = test_crtRoi.py script --------------------------

    # --------------------------  START = Used for test_ShareScanByDownloadLink.py script ------------------------------
    def ShareScanByDownloadLink(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.btnSelectRow_xpath).click()
        self.driver.find_element_by_xpath(self.btnShareIcon_xpath).click()
        self.driver.find_element_by_xpath(self.btnShareButton_xpath).click()
        self.driver.find_element_by_xpath(self.btnOpenWithMailClient_xpath).click()
        self.driver.find_element_by_xpath(self.btnCloseShareYourDataWindow_xpath).click()
    # --------------------------  END = Used for test_ShareScanByDownloadLink.py script ------------------------------




