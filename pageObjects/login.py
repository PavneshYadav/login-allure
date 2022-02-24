from time import time
import time

class LogIn:
    def __init__(self, driver):
        self.driver = driver

    alert_username = "//div[contains(text(),'Please enter your username.')]"
    alert_password = "//div[contains(text(),'Please enter your password')]"

    def user_name(self, text):
        self.driver.find_element_by_id('username').send_keys(text)

    def pass_word(self, text):
        self.driver.find_element_by_id('password').send_keys(text)

    def login_button(self):
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def alert_user(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath("//div[contains(text(),'Please enter your username.')]").text

    def alert_pass(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath("//div[contains(text(),'Please enter your password')]").text


    def alert_admin(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath("//div[@class='ant-notification-notice-message']").text

    def title_name_login_url(self):
        return self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[2]/div/h1/strong").text
    
    def back_to_conf_setting(self):
        # self.driver.find_element_by_xpath("//span[contains(text(),'Back to Configuration Settings')]").click()
        return self.driver.find_element_by_tag_name('a').text

    


