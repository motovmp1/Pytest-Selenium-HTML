from selenium.webdriver.common.by import By


class HomePage1:

    def __init__(self, driver):
        self.driver = driver

    clear_name = (By.NAME, "name")
    insert_name = (By.NAME, "name")
    clear_email = (By.NAME, "email")
    insert_email = (By.NAME, "email")
    btn_login = (By.XPATH, "//body/app-root[1]/form-comp[1]/div[1]/form[1]/input[1]")


    def clearName(self):
        return self.driver.find_element(*HomePage1.clear_name)

    def insertName(self):
        return self.driver.find_element(*HomePage1.insert_name)

    def clearEmail(self):
        return self.driver.find_element(*HomePage1.clear_email)

    def insertEmail(self):
        return self.driver.find_element(*HomePage1.insert_email)

    def btnLogin(self):
        return self.driver.find_element(*HomePage1.btn_login)



