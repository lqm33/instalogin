from selenium import webdriver
import time
import os
print("coder:LQM33")
print("ig:lqm33.sec")
print("\n")
username=input("username giriniz")
password=input("password'u giriniz")
cdriver=os.getcwd()+"/chromedriver.exe"
driver=webdriver.Chrome(executable_path=cdriver)
driver.get("https://instagram.com")
time.sleep(3)
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password+"\n")