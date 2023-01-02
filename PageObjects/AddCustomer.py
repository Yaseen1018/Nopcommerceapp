from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AddCustomer:
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath ="//a[@href='/Admin/Customer/List']"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    toggle_plus_xpath = "//i[@class='fa toggle-icon fa-plus']"
    textbox_email_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    textbox_firstname_xpath = "//input[@id='Password']"
    textbox_lastname_xpath = "//input[@id='LastName']"
    rd_Malegender_xpath = "//input[@id='Gender_Male']"
    rd_Femalegender_xpath = "//input[@id='Gender_Female']"
    textbox_dob_xpath = "//input[@id='DateOfBirth']"
    textbox_CompanyName_xpath = "//input[@id='Company']"
    rd_IstaxExempt_xpath = "//input[@id='IsTaxExempt']"
    textbox_CustomerRole_xpath ="//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-hover']//div[@role='listbox']"
    list_itemRegister_xpath = "//li[contains(text(), 'Registered')]"
    list_Administrator_xpath = "//li[contains(text(), 'Administrators')]"
    list_itemGuest_xpath = "//li[contains(text(), 'Guests')]"
    list_itemForum_xpath = "//li[contains(text(), 'Forum Moderators')]"
    list_itemVendor_xpath = "//li[contains(text(), 'Vendors')]"
    drp_managerOfVendoe_xpath = "//select[@id='VendorId']"
    rd_Active_xpath = "//input[@id='Active']"
    textbox_AdminComment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomernenuItems(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def ClickOnAddNewButton(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def ClickOnToggleIcon(self):
        self.driver.find_element(By.XPATH, self.toggle_plus_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def setFirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.textbox_firstname_xpath).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.XPATH, self.textbox_lastname_xpath).send_keys(lastname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rd_Malegender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rd_Femalegender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_Malegender_xpath).click()

    def setCompanyname(self, companyname):
        self.driver.find_element(By.XPATH, self.textbox_CompanyName_xpath).send_keys(companyname)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drp_managerOfVendoe_xpath))
        drp.select_by_visible_text(value)

    def clickOnSavebutton(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def setCustomerRole(self, role):
        self.driver.find_element(By.XPATH, self.textbox_CustomerRole_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitems=self.driver.find_element(By.XPATH, self.list_itemRegister_xpath)
        elif role == 'Administrators':
            self.listitems=self.driver.find_element(By.XPATH, self.list_administrator_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitems=self.driver.find_element(By.XPATH, self.list_itemGuest_xpath)
        elif role == 'Registered':
            self.listitems=self.driver.find_element(By.XPATH, self.list_itemRegister_xpath)
        elif role =='Vendors':
            self.listitems=self.driver.find_element(By.XPATH, self.list_itemVendor_xpath)
        else:
            self.listitems=self.driver.find_element(By.XPATH, self.list_itemGuest_xpath)
            time.sleep(3)

        #self.listeditem.click()
        self.driver.execute_script("arguments[0].click();", self.listitems)













