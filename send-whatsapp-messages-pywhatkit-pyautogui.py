# library
import pywhatkit as pwk
import pyautogui as pai
import pandas as pd
import datetime
import time as tm

# read data ./csv
contactAll = pd.read_csv('contact.csv')
contactNumberAll = contactAll['Number Contact']
print(contactNumberAll)

# function clean a phone number contact
# remove space and strip "-"
def clean_phone_number_contact():
    cleanPhoneNumberContact = contactNumberAll.str.replace('[ -]', '', regex=True)
    return cleanPhoneNumberContact

contactNumberAllClean = clean_phone_number_contact()
print(contactNumberAllClean)

# conversion data to type list/array
contactNumberArray = contactNumberAllClean.tolist()
print(contactNumberArray)

# phone and message send to target
messageSend = 'HAlOOOOooooOOOOoooo'

# to load WhatsApp Web
loadTimeWA = 20 

# change these coordinates according to the wa message button
sendButtonX = 1321
sendButtonY = 678   

# code send message looping
for i, phoneNumber in enumerate(contactNumberArray):
    try:
        print("-------------------------")
        print(f"[{i+1}/{len(contactNumberArray)}] Send to {phoneNumber}...")
        
        pwk.sendwhatmsg_instantly(
            phoneNumber, 
            messageSend, 
            wait_time=loadTimeWA,
            tab_close=False
        )
        
        # wait for the message to appear in the textbox
        print("Waiting for message to load...")
        tm.sleep(5)
        
        # click the send button directly (use coordinates)
        print("Clicking send button...")
        pai.click(x = sendButtonX, y = sendButtonY)
        
        print(f"Message Sent to {phoneNumber}")
        print("-------------------------")
        
        # wait before closing the tab
        tm.sleep(3)
        pai.hotkey('ctrl', 'w')
        
        # delay before sending to the next number
        tm.sleep(5)
        
    except Exception as e:
        print(f"Error sending to {phoneNumber}: {str(e)}")
        print("-------------------------")
        try:
            pai.hotkey('ctrl', 'w')
        except:
            pass