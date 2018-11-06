from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumrequests import Chrome
import time


file = open("dane.txt","w") 
with open(("konta.txt")) as f:
    line = f.readlines()
emails = [x.strip() for x in line] 
password=emails[0]
emails=emails[1:]
driver=Chrome()
for email in emails:
    driver.get("https://www.geekbuying.com/main/signin")
    emailAddress = driver.find_element_by_id("EmailAddress")
    password = driver.find_element_by_id("Password")
    emailAddress.send_keys(email)
    password.send_keys()
    driver.find_element_by_id("btn_signin").click()
    time.sleep(2)
    response = driver.request('POST', 'http://promotion.geekbuying.com/LuckyDraw/AddSigned?day=2')
    time.sleep(5)
    file.write(email+": "+response.text+"\n")
    print(email+": "+response.text)
    driver.delete_all_cookies()
driver.close()
file.close() 