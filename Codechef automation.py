#coding: utf-8
#pip install selenium bs4
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

import time,os,sys

#headless firefox browser
os.environ['MOZ_HEADLESS'] = '1'
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout)

browser=webdriver.Firefox()

browser.get("https://www.codechef.com/")

#login using facebook
browser.find_element_by_id("button_facebook").click()

user_input=browser.find_element_by_id("email")
username=input("Enter fb username/email/mobile no.: ")
user_input.send_keys(username)

password=getpass("Enter facebook password:" )
pass_input=browser.find_element_by_id("pass")
pass_input.send_keys(password)
pass_input.send_keys(Keys.ENTER)
#browser.find_element_by_id("loginbutton").click()

#If internet connection is slow, uncomment next line
#time.sleep(5)

problem_tag=input("Enter problem tag: ")
browser.get("https://www.codechef.com/submit/"+problem_tag)
file=input("Enter complete file path: ")

with open(file,"r") as f:
    code=f.read()

print("1. C++\n2. Python2\n3. Python3")
language=input("Enter language option from menu: ")
if language=="1":
    language="41"
elif language=="2":
    language="4"
else:
    language="116"

lang = Select(browser.find_element_by_id('edit-language'))
lang.select_by_value(language)

#If internet connection is slow, uncomment next line
#time.sleep(5)
browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

#If internet connection is slow, uncomment next line
#time.sleep(10)

prog_input=browser.find_element_by_id("edit-program")
prog_input.send_keys(code)

#If internet connection is slow, uncomment next line
#time.sleep(10)

browser.find_element_by_id("edit-submit").click()
time.sleep(10)

#printing submission result
soup=BeautifulSoup(browser.page_source,"html5lib")
result=soup.findAll("strong")
print(list(result[0])[0])

#logging out after submission
logout=browser.find_elements_by_tag_name("a")

for i in range(len(logout)):
    if logout[i].get_attribute("class")=="button grey logout-link":
        x=logout[i].get_attribute("href")
        break

browser.get(x)
time.sleep(2)

browser.close()

