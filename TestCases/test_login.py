import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import logGen


class Test_01_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = logGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*********Test 01_Login*******")
        self.logger.info("*******Verifying Home Page Title*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title= self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********Home Page title test is passed********")
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("*********Home Page title test is failed********")
            assert False

    @pytest.mark.sanity
    def test_loginPage(self,setup):
        self.logger.info("*********Test 02_Login*******")
        self.logger.info("*******Verifying Login Page Title*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title1 =self.driver.title
        if act_title1 == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*********Login Page title test is passed********")
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_loginPage.png")
            self.driver.close()
            self.logger.info("*********Login Page title test is failed********")
            assert False

