from selenium.webdriver.common.by import By


class HomePage2:

    def __init__(self, driver):
        self.driver = driver

    btn_shop = (By.XPATH, "//a[contains(text(),'Shop')]")

    def btnShop(self):
        return self. driver.find_element(*HomePage2.btn_shop)




