# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def Start(name):
    DRIVER_PATH = '/path/to/chromedriver'
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://nike.com')
    accepCookies =driver.find_element(By.XPATH,"//.[@aria-label='Accept all']")

    time.sleep(5)

    print(driver.page_source)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Start('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
