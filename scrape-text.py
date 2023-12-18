from selenium import webdriver
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")

    return driver

def get_num(text):
    return float(text.split(": ")[1])

def main():
    driver = get_driver()
    time.sleep(2)
    #copy full xpath
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return get_num(element.text)

print(main())