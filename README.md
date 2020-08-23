# Automated-WhatsApp
###### A program used to schedule and automate sending messages in WhatsApp
 
###### DISCLAIMER: 
This is a program built for demonstrational and project-purposes. **PLEASE DO NOT USE THIS TO CONTACT EMERGENCY SERVICES OR FOR OTHER VERY URGENT MATTERS.** Thank you.
 
In order to run this program successfully, you will need to download the [Chrome WebDriver (ChromeDriver). This is available here](https://chromedriver.chromium.org/downloads) under "Current Releases"; choose the right one to install for your platform. If you are on a Windows machine, unzip the file and move chromedriver.exe to your "Program Files (x86)" folder; if you do this, you shouldn't have to touch the code. Otherwise, you will have to modify the path in line 49 based on what you did.

## How to Enter data into the fields:
You should see a box that looks like this within 10-15 seconds of running the program. If you do, that means you set the path correctly for the driver.

There are three fields of concern when scheduling a message and they should be formatted as follows:

Contact Name or # | Time to Send | Messsage |
------------ | ------------- | -------------
You must enter either a phone number (w/ country code) OR \nthe exact name of the person in your contacts | Must be entered in 24-hour format | Can contain only text
Ex: Joe Smith, +1 (123) 456-7890 | Ex: 07:30, 18:45 | Hello there, friend.

![GUI](/GUIboxed.jpg?raw=true "You should see this GUI")

## Known Bugs and Issues:
