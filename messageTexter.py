"""
Authors: Robert Beery III

Description: A simple email to sms texter using gmail and smtp.

Last Modified: 7/27/21
"""

import smtplib, json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from color import bcolors
import sys
import datetime


def messageTexter(message):
    jsonFin = open('config.json', 'r')
    jsonData = json.load(jsonFin)
    jsonFin.close()
    time = datetime.datetime.now()

    phoneNumber = jsonData.get("phone_number_email")

    print('\n' + str(time)[:16] + '\n' + message)

    if len(phoneNumber) > 0:
        try:
            email = "cryptocoastr@gmail.com"
            password = 'I hate Barbarians'

            sms_gateway = jsonData.get("phone_number_email")

            smtp = "smtp.gmail.com"
            port = 587

            server = smtplib.SMTP(smtp, port)
            server.starttls()
            server.login(email, password)

            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = sms_gateway
            msg['Subject'] = "TRRadeAlgo:\n"
            body = message + "\n"
            msg.attach(MIMEText(body, 'plain'))

            sms = msg.as_string()

            server.sendmail(email, sms_gateway, sms)

            server.quit()

        except:
            print(f"{bcolors.WARNING}A phone number was found in the config file but a message could not be sent"
                     f" - closing the program."
                     f"\nTo fix this, please double check your phone number and carrier address in the config file"
                     f"and restart the program."
                  f"\nThis window will close in 30 seconds.{bcolors.ENDC}")
            time.sleep(30)
            sys.exit()