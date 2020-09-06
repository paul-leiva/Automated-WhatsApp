# Automated-WhatsApp
###### A program used to schedule and automate sending messages in WhatsApp
 
###### DISCLAIMER: 
This is a program built for demonstrational and project-purposes. **PLEASE DO NOT USE THIS TO CONTACT EMERGENCY SERVICES OR FOR OTHER VERY URGENT MATTERS.** Thank you.
 
In order to run this program successfully, you will need to download the [Chrome WebDriver (ChromeDriver). This is available here](https://chromedriver.chromium.org/downloads) under "Current Releases"; choose the right one to install for your platform. If you are on a Windows machine, unzip the file and move chromedriver.exe to your "Program Files (x86)" folder; if you do this, you shouldn't have to touch the code. Otherwise, you will have to modify the `PATH` in line 49 based on what you did. (`PATH = "C:\Program Files (x86)\chromedriver.exe"`) If you are on a macOS, then you should take the `chromedriver.exe` file and put it in your `/usr/local/bin` directory, and selenium will default to using said directory.

## Running the program:
All you need to do is run Automated-WhatsApp.py. You can run the file in an IDE of your choosing or from your terminal by executing `python Automated-WhatsApp.py`.

## How to Enter data into the fields:
You should see a box that looks like the one below within 10-15 seconds of running the program. If you do, that means you set the `PATH` correctly for the driver.

There are three fields of concern when scheduling a message and they should be formatted as follows:

Contact Name or # | Time to Send | Messsage |
------------ | ------------- | -------------
You must enter either a phone number (w/ country code) OR <br> the exact name of the person in your contacts <br> Your entry here should match the conversation in your WhatsApp, character-for-character. | Must be entered in **24-hour format**<br>(Military Time)| Can contain **ONLY TEXT**<br>NO images, files, or attachments
Ex: Joe Smith, +1 (123) 456-7890<br> For a list of country codes, [click here.](https://countrycode.org/) | Ex: 07:30, 18:45 | Hello there, friend.

Once you have entered data in every field, you should then be able to hit the *Schedule Message* button and your message will enter into the queue.
This program is designed to schedule messages within a 24-hour window. So if the current time is 20:00 (8:00 PM) and you schedule a message for 06:30 (06:30 AM), then your message will be sent the following morning at 06:30. But if you schedule a message for 22:30 (10:30 PM) at the same time, then the message will be sent later that night. **All times are local times.**

![GUI](/GUIboxed.jpg?raw=true "You should see this GUI")

## Routine for sending a message:
1. A message will be sent when there are messages in the queue and the earliest message's time to send is equal to the current time.
2. A Google Chrome window should appear shortly after the clock changes.
3. You will need to have your phone handy to login to web.whatsapp.com when the browser opens the window(You have **30 seconds to scan the QR code** before the window will close).
4. After your message is sent, the console will confirm the recipient and message that was sent.

## Known Bugs and Issues:
1. You cannot send a message to someone unless you have already sent them a message. If you are going to send a message to someone who is a new contact or you have otherwise not sent a message to already, you must start a conversation on another device before using this tool.
2. If your contacts are in a group chat or other conversation with multiple participants, then your message may be sent to the group chat instead of to the individual contact. So test it out before you send something sensitive.
3. If you are struggling to get the GUI to display, then you are probably not setting the `PATH` correctly. Try to re-set the `PATH` in line 49, which by default is set to `PATH = "C:\Program Files (x86)\chromedriver.exe"`.
