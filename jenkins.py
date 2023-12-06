import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    options = Options()
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    yield driver

def test_github_login(browser):
    browser.get("https://www.google.com/")

    search_field = browser.find_element("xpath", '//*[@id="APjFqb"]')

    search_field.send_keys("Virat kohli")
    search_field.send_keys(Keys.ENTER)

    time.sleep(2)

    assert browser.find_element("xpath", '//*[@id="rcnt"]/div[2]/div/div/div[3]/div[1]/div/div/div/div[1]/div/div')

if __name__ == "__main__":
    pytest.main([__file__, "--html=report.html"])