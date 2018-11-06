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
print(password)
for email in emails:
    driver.get("https://login.gearbest.com/m-users-a-sign.htm?type=1")
    emailAddressInput = driver.find_element_by_id("email")
    passwordInput = driver.find_element_by_id("password")
    emailAddressInput.send_keys(email)
    passwordInput.send_keys(password)
    driver.find_element_by_id("js-btnSubmit").click()
    time.sleep(20)
    #response = driver.request('POST', 'http://promotion.geekbuying.com/LuckyDraw/AddSigned?day=2')
    #time.sleep(5)
    #file.write(email+": "+response.text+"\n")
    #print(email+": "+response.text)
    driver.delete_all_cookies()
driver.close()
file.close() 