from appium.webdriver.common.appiumby import AppiumBy


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, selector):
        return self.driver.find_element(by, selector)
        # raise NotImplementedError

    def click_element(self, by, selector):
        return self.find_element(by, selector).click()
        # raise NotImplementedError
