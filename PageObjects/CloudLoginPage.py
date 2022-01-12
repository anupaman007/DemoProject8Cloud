from selenium import webdriver


class LoginPage:
    textbox_username_id = "username"
    textbox_Password_id = "password"
    link_login_link_text = "//*[@id='btnLogin']"
    partial_link_logout = "Sign out"
    partial_link_forgot_password = "I forgot my password"
    textbox_Email_id = "useridentity"
    btn_reset_password_id = "btnResetPw"
    partial_link_backtologin_xpath = "Back to login"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_Password_id).clear()
        self.driver.find_element_by_id(self.textbox_Password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.link_login_link_text).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.partial_link_logout).click()

    def clickOnForgotPassword(self):
        self.driver.find_element_by_link_text(self.partial_link_forgot_password).click()

    def enterEmailAddress(self, email):
        self.driver.find_element_by_id(self.textbox_Email_id).send_keys(email)

    def clickOnRestPassword(self):
        self.driver.find_element_by_id(self.btn_reset_password_id).click()

    def clickOnBackToLogin(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_link_text(self.partial_link_backtologin_xpath)
