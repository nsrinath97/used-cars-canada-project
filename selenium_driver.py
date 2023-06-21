from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    """Initialize chromedriver"""
    chrome_options = Options()
    chrome_options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images":2}) # Doesn't load images
    chrome_options.add_argument('--headless')  # Doesn't open up a web browser gui
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return chrome_driver