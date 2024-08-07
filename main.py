from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()

options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
items=driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
items_ids=[ item.get_attribute("id") for item in items]
time_out= time.time() + 5
five_minutes = time.time() + 5*60
while True:
    cookie.click()
    if time.time()> time_out:
        prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices=[]
        for price in prices:
            price_text = price.text
            if price_text !="":
                cost = int(price_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        cookie_dictionary={}
        for n in range(len(item_prices)):
            cookie_dictionary[item_prices[n]]=items_ids[n]
        money=driver.find_element(By.ID,"money").text
        if "," in money:
            money=money.replace(",","")
        money_count=int(money)
        affordable_upgrades={}
        for cost, id in cookie_dictionary.items():
            if money_count>cost:
                affordable_upgrades[cost]=id
        highest_price=max(affordable_upgrades)
        print(highest_price)
        price_id=affordable_upgrades[highest_price]
        driver.find_element(By.ID,price_id).click()
        time_out=time.time()+5
        if time.time()>five_minutes:
            cookies_perSecond = driver.find_element(By.ID,"cps").text
            print(cookies_perSecond)
            break
            

















