from datetime import datetime
import pytest
from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    cwd = os.getcwd()
    path = os.path.join(cwd)
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': path}
    chrome_options.add_experimental_option('prefs', prefs)
    #chrome_options.add_argument("headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('disable-infobars')
    driver = webdriver.Chrome(ChromeDriverManager().install() ,options=chrome_options)
    driver.get('https://bucket-access-true-k-lite-serverless-vx6j3hrgca-ue.a.run.app/')
    driver.find_element_by_xpath("//button[@id='SubmitBtn']").click()
    #driver.maximize_window()
    request.cls.driver = driver
    yield
    #driver.close()

# def pytest_configure(config):
#     config._metadata = None

#     if not os.path.exists('reports'):
#         os.makedirs('reports')

#     config.option.htmlpath = 'reports/' + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
