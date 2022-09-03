import time
import hashlib
from urllib.request import urlopen, Request
import os
import smtplib
from email.message import EmailMessage
from smtplib import SMTP
from dotenv import load_dotenv
load_dotenv()

# /*-----------Variables----------*/
sleeptime= 1800 # 30min
running = True
options = [
{"url1": "staticHash"}
]


# /*-----------Functions----------*/
def send_email(subject):
    smtp_port = SMTP("smtp.gmail.com", 587)
    smtp_port.ehlo()
    smtp_port.starttls()
    smtp_port.login(os.getenv("SELFEMAIL") , os.getenv("PW"))# Sending the email
    final_message = f"Subject: {subject}"
    smtp_port.sendmail(os.getenv("SELFEMAIL"), os.getenv("RECIVERMAIL"), final_message)
    print("Email erfolgreich versendet.")
    smtp_port.quit()


if __name__ == "__main__":
    for option in options:
        key,value = list((option.items()))[0]
        url = Request(key, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        # Sending mail if hash differs
        if currentHash != value:
            send_email("Mentoriatsanmeldung - Fernuni Hagen - Algomathe moeglich?" )
            print(f"hashO: {value}")
            print(f"hashN: {currentHash}")
            running = False
            break
        else: 
            print(f"{key} - keine Änderung")
    if running:
        print(f"keine Änderungen gefunden - {sleeptime} Sekunden warten...")
        print ("-------------------------------------\n")







