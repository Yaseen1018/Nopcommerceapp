import pytest
import random
import string
import time
from selenium import webdriver
from PageObjects.AddCustomer import AddCustomer
from PageObjects.LoginPage import LoginPage
from PageObjects.SearchCustomer import SearchCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import logGen
from selenium.webdriver.support.ui import WebDriverWait

class Test_03_searchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = logGen.loggen()

    @pytest.mark.sanity
    def test_searchCustomerByName(self,setup):
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

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomernenuItems()

        self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        time.sleep(20)
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
