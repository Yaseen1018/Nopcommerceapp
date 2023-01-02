import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import logGen
from Utilities import ExcelUtils
from selenium.webdriver.support.ui import WebDriverWait
import time


class Test_02_ddt__Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/Cred.xlsx"
    logger = logGen.loggen()


    def test_loginPage_ddt(self,setup):
        self.logger.info("*********Test 02_ddtLogin*******")
        self.logger.info("*******Verifying Login Page Title*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)

        self.rows = ExcelUtils.getRowCount(self.path,"Sheet1")
        print("Number of Rows in a Excel",self.rows)

        list_status=[] #Empty list variable
        for r in range(2,self.rows+1):
            self.user = ExcelUtils.readData(self.path,"Sheet1",r,1)
            self.password = ExcelUtils.readData(self.path,"Sheet1",r,2)
            self.exp = ExcelUtils.readData(self.path,"Sheet1",r,3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

        act_title =self.driver.title
        exp_title ="Dashboard / nopCommerce administration"
        if act_title == exp_title:
            if self.exp=="Pass":
                self.logger.info("***Passed***")
                self.lp.clickLogout();
                list_status.append("Pass")
            elif self.exp == "Fail":
                self.logger.info("***Failed***")
                self.lp.clickLogout();
                list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("***Failed***")
                    list_status.append("Fail")
                elif self.exp == 'Fail':
                    seelf.logger.info("***Failed***")
                    list_status.append("Pass")
            print(lst_status)

        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("*****End of Login DDT Test ****")









