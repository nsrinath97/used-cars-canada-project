from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def get_driver():
    """Initialize driver"""
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options)
    return driver
