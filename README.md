# A lightweight Python script to automate sending WhatsApp messages using (multiple) CSV data, PyWhatKit, and PyAutoGUI

## Installation & Setup

1. Install required packages:
```bash
pip install pywhatkit pyautogui pandas
```

2. Before running the main script, you need to find the coordinates of WhatsApp's send button:
- Create a file `find_coordinates.py`:
```python
import pyautogui as pai
import time as tm
print("Move your mouse to WhatsApp SEND BUTTON in 5 seconds...")
print("5...")
tm.sleep(1)
print("4...")
tm.sleep(1)
print("3...")
tm.sleep(1)
print("2...")
tm.sleep(1)
print("1...")
tm.sleep(1)
position = pai.position()
print(f"\nSend button coordinates: x={position.x}, y={position.y}")
print(f"Use these coordinates in the main script!")
```
- Run the script:
```bash
python find_coordinates.py
```
- Quickly move your mouse to the WhatsApp send button (paper plane icon)
- Copy the coordinates shown (example: `x=1321, y=678`)

3. Update Main Script
Update these variables in the main script with your coordinates:
```python
sendButtonX = 1321  # replace with your X coordinate
sendButtonY = 678   # replace with your Y coordinate
```

4. Prepare CSV File
Example contact.csv with column 'Number Contact' 'Group':
```python
contactAll = pd.read_csv('contact.csv')
contactNumberAll = contactAll['Number Contact']
print(contactNumberAll)
```
```csv
Number Contact,Group
 +62 813-6033-9061,Secret
 +62 812-6589-8260,Secret
 +62 812-4812-6005,Secret
```

5. Adjust the deletion of contact numbers in this case with spaces and hyphens "-" (+62 812-4812-6005 -> +6281248126005)
```python
def clean_phone_number_contact():
    cleanPhoneNumberContact = contactNumberAll.str.replace('[ -]', '', regex=True)
    return cleanPhoneNumberContact
```

6. Adjust/Change message
```python
messageSend = 'Your message here'
```

7. Run Script
```bash
python send-whatsapp-messages-pywhatkit-pyautogui.py
```

## Prerequisites

Before running this script, make sure you have:
- Python 3.12 or higher
- Active WhatsApp account
- WhatsApp Web logged in on your browser (default browser, closed condition)
- No draft messages in WhatsApp Web for any contacts in the data
- Do not touch or disturb device activity while the program is running (just leave it alone)
- Ensure the device is supported and the network connection is very stable

## Project Structure
```
send-whatsapp-messages-pywhatkit-pyautogui/
│
├── send-whatsapp-messages-pywhatkit-pyautogui.py   # Main script
├── find_coordinates.py                             # (Create) Helper script to find coordinates
├── contact.csv                                     # Your contact list
└── README.md                                       # Documentation
```

## License
This project is licensed under the MIT License.
Copyright © 2025 Bangfiq