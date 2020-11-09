import pytest
from selenium import webdriver

from PagesObjects.HomePage1 import HomePage1
from PagesObjects.HomePage2 import HomePage2
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass
import time


# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")


class TestONe(BaseClass):
    timer_clear = 0.2
    action_page = 3

    def test_e2e(self, get_data):
        username_1 = "Vinicius Miranda de Pinho"
        emailed_1 = "vinicius.pinho@vpinho.com"
        homepage1 = HomePage1(self.driver)
        # log file
        log = self.test_logginfile()
        self.timerPages()
        homepage1.clearName().clear()
        time.sleep(self.timer_clear)
        homepage1.insertName().send_keys(get_data["name_user"])
        log.info(get_data["name_user"])
        self.timerPages()
        homepage1.clearEmail().clear()
        time.sleep(self.timer_clear)
        homepage1.insertEmail().send_keys(get_data["email"])
        log.info(get_data["email"])
        self.timerPages()
        homepage1.btnLogin().click()
        time.sleep(self.action_page)
        self.refreshPage()
        log.info("Refresh 3 seconds new page: ")

    def test_e2e_part(self):
        homepage1 = HomePage1(self.driver)
        homepage2 = HomePage2(self.driver)

        self.timerPages()
        homepage1.clearName().clear()
        time.sleep(self.timer_clear)
        self.driver.find_element_by_name("name").send_keys("Shophia Pinho")
        self.timerPages()
        self.driver.find_element_by_name("email").clear()
        time.sleep(self.timer_clear)
        self.driver.find_element_by_name("email").send_keys("sophia.pinho@vpinho.com")
        self.timerPages()
        self.driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/input[1]").click()
        time.sleep(self.action_page)
        homepage2.btnShop().click()
        time.sleep(self.action_page)

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def get_data(self, request):
        return request.param
