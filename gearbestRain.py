from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumrequests import Chrome
import time
import datetime
import requests

file = open("dane.txt","a") 
with open(("konta.txt")) as f:
    line = f.readlines()
emails = [x.strip() for x in line] 
password=emails[0]
emails=emails[1:]
driver=Chrome()
for email in emails:
    driver.get("https://login.gearbest.com/m-users-a-sign.htm?type=1")
    emailAddressInput = driver.find_element_by_id("email")
    passwordInput = driver.find_element_by_id("password")
    emailAddressInput.send_keys(email)
    passwordInput.send_keys(password)
    driver.find_element_by_id("js-btnSubmit").click()
    driver.get("https://www.gearbest.com/promotion-COUPON-RAIN-special-3881.html")
    response=driver.request('POST', 'https://www.gearbest.com/activity/lottery/red-rain-raffle?activityId=6457650456939036672',
    data = {'count': '30'})
    file.write(email+"  "+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"  "+response.text+"\n")
    print(email+": "+response.text)
    driver.delete_all_cookies()
driver.close()
file.close() 