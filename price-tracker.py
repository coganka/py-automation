from selenium import webdriver
import yagmail
import time
import os

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #options.add_experimental_option("detach", True)
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amazon.com/PlayStation-5-DualSense-Wireless-Controller/dp/B08MLRTYF5")

    return driver

def main():
    driver = get_driver()
    #copy full xpath
    element = driver.find_element(by="xpath", value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[2]/span[2]')
    return element.text

def clean_price(raw):
    return float(raw.replace('$', ''))

sender = 'cankaragun@gmail.com'
receiver = 'cankaragun@gmail.com'

raw_price = main()
price = (clean_price(raw_price))
prices = [price]

while True:
    time.sleep(3600)
    raw_price = main()
    price = clean_price(raw_price)
    prices.append(price)
    print(prices)

    if prices[-1] != prices[-2]:
        subject = f"price changed"
        contents = f"price changed to ${price}"

        yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
        yag.send(to=receiver, subject=subject, contents=contents)

        print("email sent")

    del prices[-2]