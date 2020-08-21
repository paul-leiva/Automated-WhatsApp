# A program to automate and schedule your WhatsApp messages
# Created by Paul Leiva | Florida International University, Miami, FL, United States
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
from tkinter.ttk import *
from time import localtime, strftime
import datetime

#stuff = [[6, "London", "England"], [1, "New York", "United States"], [3, "Ottawa", "Canada"]]

#stuff.sort() # default sort by first element
#stuff.sort(key=lambda x: x[2]) # sort by element at index[1] in each tuple
#print(stuff)

current = strftime("%H:%M", localtime())
print(current)

to_send = []

practice = True

while (practice == True):
   contact = input('Enter name of contact or group: ')
   message = input('Enter your message: ')
   time = input('Enter time to send (24H:MM): ')
   now = strftime("%H:%M", localtime())
   #if (time < now):
   if (time < strftime("%H:%M", localtime())):
      date = datetime.date.today() + datetime.timedelta(days=1)
   else:
      date = datetime.date.today()
   to_send.append([str(date), time, contact, message])
   to_send.sort()
   print(to_send)
   print(to_send[0][1])
   next = to_send[0][1]
   if (strftime("%H:%M", localtime()) == to_send[0][1]):
      print(to_send[0])
      to_send.pop(0)
      print(to_send)



today = datetime.date.today()
print(today)
print(today + datetime.timedelta(days=1)) #tomorrow

# use 24-hour time
AMmessages = [['Ari Heyd','Hello at last','08/21/20 05:55'], ['Ari Heyd','Hello','08/21/20 17:45'], ['Ari Heyd','Hello again','08/22/20 17:35']]
AMmessages.sort(key=lambda x: x[2])
print(AMmessages)
#print(messages[1][2]-current)
"""
def schedule_message():
   # Label(window, text="Time to Schedule the Message").grid(row = 4, column = 0)


def sendMessage():
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
#main()
"""