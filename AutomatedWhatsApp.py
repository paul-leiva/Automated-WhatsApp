# A WhatsApp Messenger application

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
   PATH = "C:\Program Files (x86)\chromedriver.exe"
   driver = webdriver.Chrome(PATH)
   driver.get('https://web.whatsapp.com/')
   
   name = input('Enter name of contact or group: ')
   message = input('Enter your message: ')
   
   input('Enter DONE once you have scanned your QR Code: ')
   
   user = driver.find_element_by_xpath('//span[@title = "{}" ]'.format(name))
   user.click()
   
   time.sleep(5)
   
   message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
   time.sleep(5)
   message_box.send_keys(message)
   
   button = driver.find_element_by_class_name('_1U1xa')
   button.click()
main()