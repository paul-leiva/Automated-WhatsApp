# Automated-WhatsApp
###### A program used to schedule and automate sending messages in WhatsApp
 
###### DISCLAIMER: 
This is a program built for demonstrational and project-purposes. **PLEASE DO NOT USE THIS TO CONTACT EMERGENCY SERVICES OR FOR OTHER VERY URGENT MATTERS.** Thank you.
 
In order to run this program successfully, you will need to download the [Chrome WebDriver (ChromeDriver). This is available here](https://chromedriver.chromium.org/downloads) under "Current Releases"; choose the right one to install for your platform. If you are on a Windows machine, unzip the file and move chromedriver.exe to your "Program Files (x86)" folder; if you do this, you shouldn't have to touch the code. Otherwise, you will have to modify the `PATH` in line 49 based on what you did.

## How to Enter data into the fields:
You should see a box that looks like the one below within 10-15 seconds of running the program. If you do, that means you set the `PATH` correctly for the driver.

There are three fields of concern when scheduling a message and they should be formatted as follows:

Contact Name or # | Time to Send | Messsage |
------------ | ------------- | -------------
You must enter either a phone number (w/ country code) OR <br> the exact name of the person in your contacts <br> Your entry here should match the conversation in your WhatsApp, character-for-character. | Must be entered in **24-hour format**<br>(Military Time)| Can contain **ONLY TEXT**<br>NO images, files, or attachments
Ex: Joe Smith, +1 (123) 456-7890<br> For a list of country codes, [click here.](https://countrycode.org/) | Ex: 07:30, 18:45 | Hello there, friend.

Once you have entered data in every field, you should then be able to hit the *Schedule Message* button and your message will enter into the queue.

![GUI](/GUIboxed.jpg?raw=true "You should see this GUI")

## Known Bugs and Issues:
1. You cannot send a message to someone unless you have already sent them a message. If you are going to send a message to someone who is a new contact or you have otherwise not sent a message to already, you must start a conversation on another device before using this tool.
2. If your contacts are in a group chat or other conversation with multiple participants, then your message may be sent to the group chat instead of to the individual contact. So test it out before you send something sensitive.
3. If you are struggling to get the GUI to display, then you are probably not setting the `PATH` correctly. Try to re-set the `PATH` in line 49, which by default is set to `PATH = "C:\Program Files (x86)\chromedriver.exe"`.
