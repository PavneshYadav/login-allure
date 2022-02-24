import time
from utilities.baseClass import BaseClass
from pageObjects.login import LogIn
import allure
from allure_commons.types import AttachmentType


class TestLoginPage(BaseClass):

    @allure.title("TestMinio - Configuration Page")
    @allure.description("This is test of minio default test Configuration")
    def test_login_page(self):    
        login = LogIn(self.driver)
        verify_url = self.driver.current_url
        assert "login" in verify_url
        verify_title = login.title_name_login_url()
        assert "Please login to Fortress IQ" in verify_title
        config_change = login.back_to_conf_setting()
        assert "Back to Configuration Settings" in config_change
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    @allure.title("TestMinio - Configuration Page")
    @allure.description("This is test of minio default test Configuration")
    def test_login_failed(self):
        login = LogIn(self.driver)
        login.user_name('admin')
        login.login_button()
        assert login.alert_pass()
        self.driver.refresh()
        login.pass_word('admin')
        login.login_button()
        alert_usr = login.alert_user()
        assert "Please enter your username." in alert_usr
        self.driver.refresh()
        login.login_button()
        alert_pass = login.alert_pass()
        assert "Please enter your password" in alert_pass and "Please enter your username." in alert_usr
        self.driver.refresh()
        login.user_name("admin")
        login.pass_word("adm")
        login.login_button()
        time.sleep(5)
        admin = login.alert_admin()
        assert "Please contact administrator for access." in admin
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    @allure.title("TestMinio - Configuration Page")
    @allure.description("This is test of minio default test Configuration")
    def test_login_passsed(self):    
        login = LogIn(self.driver)
        self.driver.refresh()
        login.user_name('admin')
        login.pass_word('admin')
        login.login_button()
        # welcome_user = self.driver.find_element_by_xpath("//div[@class='ant-col user-header']").text
        # assert "Welcome" in welcome_user
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    
