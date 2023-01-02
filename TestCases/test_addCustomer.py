import pytest
import random
import string
from selenium import webdriver
from PageObjects.AddCustomer import AddCustomer
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import logGen
from selenium.webdriver.support.ui import WebDriverWait

class Test_03_addCustromer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = logGen.loggen()

    def test_addCustomer(self,setup):
        self.logger.info("*********Test Add Customer*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)


        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****Login Successfull****")

        self.logger.info("****Add Customer****")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomernenuItems()
        #self.addcust.ClickOnToggleIcon()

        self.logger.info("*****Providing customer details*****")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)

        self.addcust.setPassword("test123")
        self.addcust.setFirstname("Demouser")
        self.addcust.setLastname("user")
        self.addcust.setGender("Male")
        self.addcust.setCompanyname("microsoft")
        self.addcust.setCustomerRole("Guests")
        self.addcust.setCompanyname("Text")
        self.addcust.btn_save_xpath

        self.logger.info("*****saving customer details******")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))



