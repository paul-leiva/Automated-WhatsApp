# A program to automate and schedule your WhatsApp messages within the next 24 hours
# Created by Paul Leiva | Florida International University, Miami, FL, United States
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from time import localtime, strftime
import time
import datetime

def schedule_message():
   queue_frame.destroy() # get rid of the old queued messages when a new one is scheduled
   q.grid(row=1, padx=5, sticky=EW)
   recipient_labelq = Label(q, text ='Recipient:')
   time_labelq = Label(q, text ='Will be sent at: ')
   msg_labelq = Label(q, text ='Message: ', justify="left")
   
   recipient_labelq.grid(row = 0, column = 0, padx=5)
   time_labelq.grid(row = 0, column=1)
   msg_labelq.grid(row=0, column=2)
   
   recipient = contact.get()
   messageq = message.get("1.0", END)
   if (str(time_entry.get()) < strftime("%H:%M", localtime())): # if the time entered for the message is earlier than the current time,
      date_q = datetime.date.today() + datetime.timedelta(days=1) # the message will be scheduled for that time tomorrow (the next occurrence of said time)
   else: # if the time enteres is later than the current time
      date_q = datetime.date.today() # the message will be scheduled for that time later today
   to_send.append([str(date_q), time_entry.get(), recipient, message.get("1.0", END)]) # add the message to the queue of messages
   to_send.sort() # sort the queue (by date, then by time)
   print(to_send) # prints your ordered messages on the console

   for x in range(len(to_send)): # Loop to redo the queue frame of messages
      Label(q, text=to_send[x][2]).grid(row = 4+x, column = 0) # recipient
      Label(q, text=to_send[x][1]).grid(row = 4+x, column = 1) # time to send
      Label(q, text=to_send[x][3], wraplength=500, justify="left").grid(row = 4+x, column = 2, columnspan=2) # message

def check_time(): #this method checks if a message is to be sent every 10 seconds
   if (to_send != []): # if the queue of messages is NOT empty
      if (strftime("%H:%M", localtime()) == to_send[0][1]): # once the next queued message's time is the current one
         print(to_send[0][1]) # print for reference
         send_Message() # send this message
   window.after(10000, check_time) # 10-second loop
   
def send_Message():
   # This path is the place where you have the Chrome driver stored. 
   # You may need to change this PATH variable if you download yours to a different location
   PATH = "C:\Program Files (x86)\chromedriver.exe"
   driver = webdriver.Chrome(PATH)
   driver.get('https://web.whatsapp.com/') #initiate the driver to pull up the web page
   
   # This exception handler is designed to give your machine 30 seconds to pull up the WhatsApp Login page and login before sending the message
   try:
      main = WebDriverWait(driver, 30).until(
         EC.presence_of_element_located((By.CLASS_NAME, "_210SC"))
      )
   except:
       driver.quit() # if the login page isn't passed in 30 seconds, the window will close
   
   # This variable is the placeholder on the page for finding the recipient of the message (name or number)
   user = driver.find_element_by_xpath('//span[@title = "{}" ]'.format(str(to_send[0][2])))
   user.click()
   
   time.sleep(1) # allow this process some time to do the clicking
   
   # This variable is the placeholder for the message box. Text messages only can be sent.
   message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
   time.sleep(2) # waiting time
   message_box.send_keys(to_send[0][3]) # insert the message string into the message_box
   try:
      button = driver.find_element_by_class_name('_1U1xa') # find the send button
      button.click() # click the send button
   except:
      print('ok') # this exception handles an unknown csselement finding error
   driver.quit() # close the window
   
   #print notification of message being sent
   print('Your message: ' + to_send[0][3] + ' was sent to ' + to_send[0][2])
   to_send.pop(0)
   
   #redo the queue of messages
   queue_frame.destroy()
   q.grid(row=1, padx=5, sticky=EW)
   recipient_labelq = Label(q, text ='Recipient:')
   time_labelq = Label(q, text ='Will be sent at: ')
   msg_labelq = Label(q, text ='Message: ', justify="left")
   
   recipient_labelq.grid(row = 0, column = 0, padx=5)
   time_labelq.grid(row = 0, column=1)
   msg_labelq.grid(row=0, column=2)
   
   recipient = contact.get()
   messageq = message.get("1.0", END)
   if (str(time_entry.get()) < strftime("%H:%M", localtime())):
      date_q = datetime.date.today() + datetime.timedelta(days=1)
   else:
      date_q = datetime.date.today()
   to_send.append([str(date_q), time_entry.get(), recipient, message.get("1.0", END)])
   
   for x in range(len(to_send)):
      Label(q, text=to_send[x][2]).grid(row = 4+x, column = 0) # recipient
      Label(q, text=to_send[x][1]).grid(row = 4+x, column = 1) # time to send
      Label(q, text=to_send[x][3], wraplength=500, justify="left").grid(row = 4+x, column = 2, columnspan=2) # message

def toggle_state(*_):
   if(contact.var.get() and time_entry.var.get()):
      schedule_button['state'] = 'normal'
   else:
      schedule_button['state'] = 'disabled'

#print the current time for reference when the program starts
current = strftime("%H:%M", localtime())
print(current)

to_send = [] # A list of messages stored as: [date, time, recipient/contact, message]

window = Tk() # make a GUI window
window.title("AutomatedWhatsApp.py")
window.geometry("600x600") 

q = LabelFrame(window, text = "Queued Messages", height=200, pady=5, padx=5)

schedule_frame = LabelFrame(window, text = "Schedule a Message", height=200, pady=5, padx = 5) # top frame
queue_frame = LabelFrame(window, text = "Queued Messages", height=200, pady=5, padx=5) # bottom frame

window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

#situate the frames
schedule_frame.grid(row=0, padx=5, sticky=EW)
queue_frame.grid(row=1, padx=5, sticky=EW)

# Make labels, buttons, and entry boxes
contact_label = Label(schedule_frame, text ='Contact name or #: ')
time_label = Label(schedule_frame, text ='Time to send (24HR:MM): ')
msg_label = Label(schedule_frame, text ='Message to send: ')
contact = Entry(schedule_frame, width=30)
time_entry = Entry(schedule_frame, width = 10)
message = Text(schedule_frame, width=50, height=10)
schedule_button = Button(schedule_frame, text ="Schedule Message", command = schedule_message)

# Positioning
contact_label.grid(row = 0, column = 0, padx=5)
contact.grid(row=0, column=1, columnspan=1, padx=5)
time_label.grid(row = 0, column=2)
time_entry.grid(row=0, column=3, sticky="w")
msg_label.grid(row=1, column=0)
message.grid(row=2, column=0, columnspan=3)
schedule_button.grid(row=3, column=3, sticky="SE")
schedule_button['state']='disabled'

# This process allows our 'Schedule Message' button to be unclickable until you fill the contact and time_entry fields
contact.var = StringVar()
contact['textvariable']=contact.var
contact.var.trace_add('write', toggle_state)

time_entry.var = StringVar()
time_entry['textvariable']=time_entry.var
time_entry.var.trace_add('write', toggle_state)

# Queue frame labels
recipient = Label(queue_frame, text ='Recipient:')
sending_time = Label(queue_frame, text ='Will be sent at: ')
msg = Label(queue_frame, text ='Message: ')

# Positioning
recipient.grid(row = 0, column = 0, padx=5)
sending_time.grid(row = 0, column=1)
msg.grid(row=0, column=2)

check_time() # process to check the time as part of mainloop
      
window.mainloop() # allows the GUI window to display
