# A program to automate and schedule your WhatsApp messages
# Created by Paul Leiva | Florida International University, Miami, FL, United States
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
#from tkinter.ttk import *
from time import localtime, strftime
import datetime

def schedule_message():
   queue_frame.destroy()
   q = LabelFrame(window, text = "Queued Messages", height=200, pady=5, padx=5)
   q.grid(row=1, padx=5, sticky=EW)
   recipient = Label(q, text ='Recipient:')
   sending_time = Label(q, text ='Will be sent at: ')
   msg = Label(q, text ='Message: ')
   
   recipient.grid(row = 0, column = 0, padx=5)
   sending_time.grid(row = 0, column=1)
   msg.grid(row=0, column=2)
   Label(q, text=contact.get()).grid(row = 4, column = 0)
   Label(q, text=time.get()).grid(row = 4, column = 1)
   Label(q, text=message.get("1.0", END), wraplength=500, justify="left", bg="green").grid(row = 4, column = 2, columnspan=2)
   
def toggle_state(*_):
   if(contact.var.get() and time.var.get()):
      schedule_button['state'] = 'normal'
   else:
      schedule_button['state'] = 'disabled'

current = strftime("%H:%M", localtime())
print(current)

to_send = []#["2020/08/24", "08:08", "ari", "Hello"]] # set of queued messages

practice = False

window = Tk()
window.title("AutomatedWhatsApp.py")
window.geometry("600x600") 

schedule_frame = LabelFrame(window, text = "Schedule a Message", height=200, pady=5, padx = 5)
queue_frame = LabelFrame(window, text = "Queued Messages", height=200, pady=5, padx=5)

window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

schedule_frame.grid(row=0, padx=5, sticky=EW)
queue_frame.grid(row=1, padx=5, sticky=EW)

contact_label = Label(schedule_frame, text ='Contact name or #: ')
time_label = Label(schedule_frame, text ='Time to send (24HR:MM): ')
msg_label = Label(schedule_frame, text ='Message to send: ')
contact = Entry(schedule_frame, width=30)
time = Entry(schedule_frame, width = 10)
message = Text(schedule_frame, width=50, height=10)
schedule_button = Button(schedule_frame, text ="Schedule Message", command = schedule_message)

contact_label.grid(row = 0, column = 0, padx=5)
contact.grid(row=0, column=1, columnspan=1, padx=5)
time_label.grid(row = 0, column=2)
time.grid(row=0, column=3, sticky="w")
msg_label.grid(row=1, column=0)
message.grid(row=2, column=0, columnspan=3)
schedule_button.grid(row=3, column=3, sticky="SE")
schedule_button['state']='disabled'

contact.var = StringVar()
contact['textvariable']=contact.var
contact.var.trace_add('write', toggle_state)

time.var = StringVar()
time['textvariable']=time.var
time.var.trace_add('write', toggle_state)

recipient = Label(queue_frame, text ='Recipient:')
sending_time = Label(queue_frame, text ='Will be sent at: ')
msg = Label(queue_frame, text ='Message: ')

recipient.grid(row = 0, column = 0, padx=5)
sending_time.grid(row = 0, column=1)
msg.grid(row=0, column=2)

for x in to_send:
   Label(queue_frame, text = str(to_send))

window.mainloop()

while (to_send != []):
   now = strftime('%H:%M', localtime())
   #if (time < now):
   if (str(time) < strftime("%H:%M", localtime())):
      date = datetime.date.today() + datetime.timedelta(days=1)
   else:
      date = datetime.date.today()
   to_send.append([str(date), time, contact, message])
   to_send.sort()
   print(to_send)
   print(to_send[0][1])
   next = to_send[0][1]
   #if (strftime("%H:%M", localtime()) == to_send[0][1]):
      #print(to_send[0])
   to_send.pop(0)


"""
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