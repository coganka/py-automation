from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.udemy.com/join/login-popup/")

    return driver

def main():
    driver = get_driver()
    driver.find_element(by="xpath", value="/html/body/div[1]/div[2]/div/div/form/div[1]/div/div/div/input").send_keys("cankaragun@gmail.com")
    time.sleep(1)
    driver.find_element(by="xpath", value="/html/body/div[1]/div[2]/div/div/form/div[2]/div/div/input").send_keys("Axdfga34." + Keys.RETURN)
    time.sleep(1)
    #driver.find_element(by="xpath", value="/html/body/nav/div/a").click()

    #time.sleep(2)
    #element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    
print(main())