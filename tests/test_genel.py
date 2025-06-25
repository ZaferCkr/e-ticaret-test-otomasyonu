from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # görünmez çalıştırmak için
    service = Service(executable_path=r"C:\Users\zafer\OneDrive\Masaüstü\chromedriver-win64\chromedriver.exe")  # chromedriver yolunu buraya yaz
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_homepage_title(driver):
    driver.get("https://automationexercise.com")
    assert "Automation Exercise" in driver.title


def test_homepage_logo_visible(driver):
    driver.get("https://automationexercise.com")
    logo = driver.find_element(By.XPATH, "//img[@alt='Website for automation practice']")
    assert logo.is_displayed()


def test_navigation_to_login(driver):
    driver.get("https://automationexercise.com")
    login_link = driver.find_element(By.XPATH, "//a[@href='/login']")
    login_link.click()

    WebDriverWait(driver, 5).until(
        EC.url_contains("/login")
    )

    assert "Login" in driver.page_source or "Signup" in driver.page_source


def test_signup_form_elements(driver):
    driver.get("https://automationexercise.com/login")

    # Form alanlarını kontrol et
    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")

    assert name_input.is_displayed()
    assert email_input.is_displayed()


def test_footer_visibility(driver):
    driver.get("https://automationexercise.com")
    footer = driver.find_element(By.TAG_NAME, "footer")
    assert footer.is_displayed()
