from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
 
driver = webdriver.Chrome("F:\\z\\chromedriver_win32\\chromedriver.exe")

driver.get('https://www.naukri.com/nlogin/login')
time.sleep(5)
print("Opened naukri...")

text = driver.find_element_by_id('usernameField')
text.send_keys('saikumarda4@gmail.com')
print("email entered...")
password = driver.find_element_by_id('passwordField')
password.send_keys('sai521sai')
print("Password entered...")
#submit = driver.find_element_by_xpath("//input[@id='sbtLog']")
password.submit()
print("facebook opened")
#status= driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
#status.send_keys("Bot is typing here");
#print("Status trying")
time.sleep(5)
driver.get('https://www.naukri.com/mnjuser/profile?id=&altresid')
#upload = driver.find_element_by_xpath("//a[@id='uploadLink']")
#upload.click()
time.sleep(5)
#driver.execute_script("window.scrollTo(0,3060)")
#time.sleep(5)
#driver.execute_script("window.scrollTo(0,-1)")
#link=driver.find_element_by_class_name("secondary-content")

#link=driver.find_element_by_xpath("//select[@name='name']")
link = driver.find_element_by_xpath("//a[contains(.,'Update')]")
link.click()
time.sleep(5)
uploadFile = driver.find_element_by_xpath("//input[@id='attachCV']")
uploadFile.send_keys('F:\\z\\resume-s.pdf')
time.sleep(5)
#save = driver.find_element_by_xpath("//button[contains(.,'Save')]")
#save.click()
print("post done")
quit
'''

driver.get('https://my.monsterindia.com/login.html')

monsterEmail = driver.find_element_by_xpath("//input[@id='username_login']")
monsterEmail.send_keys('saikumarda4@gmail.com')
monsterEmail.send_keys(Keys.TAB) # tab over to not-visible element
password = driver.find_element_by_xpath("//input[@name='passwd']")
password.send_keys('sai355sai')
submit= driver.find_element_by_xpath("//input[@id='button']")
password.submit()
driver.get('http://my.monsterindia.com/view_resume.html')
monsterUpload = driver.find_element_by_xpath("//a[contains(.,'Edit Resume')]")
monsterUpload.click()
monsterUploadFile = driver.find_element_by_xpath("//input[@id='wordresume']")
monsterUploadFile.send_keys('F:\\z\\resume-saib.pdf')
time.sleep(5)
monsterSave = driver.find_element_by_xpath("//input[@value='Submit']")
time.sleep(5)
monsterSave.click()
time.sleep(5
'''




