from selenium.webdriver.common.by import By
import time


class HandyWrappers:

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element not found")
        return element

    def takeScreenshot(self, driver):
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = ".\\Screenshots\\"
        destinationFile = screenshotDirectory + fileName
        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False
    
    def total_element_present(self, byType, locator):
        try:
            elementList = self.driver.find_elements(byType, locator)
            for element in elementList:
                if len(element) == len(elementList):
                    print("Total Count Found")
                    return len(element)
                else:
                    print("Element not found")
                    return False
        except:
            print("Element not found")
            return False

