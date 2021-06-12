import os
from twilio.rest import Client
import re


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure


os.environ['ACCOUT_SID'] = 'ACa958e3e7adfa6633848742ca7f22458c'
os.environ ['ACCOUNT_TOKEN'] = '7b1f96d766d566e4ad23fa6daa147581'
os.environ['SERVICE_ID'] = 'VA792ec94b826ee64d788d964cc8050941'

account_sid = os.environ['ACCOUT_SID']
auth_token = os.environ['ACCOUNT_TOKEN']
client = Client(account_sid, auth_token)
SERVICE_ID = os.environ['SERVICE_ID']


def send_message(body,to):
    message = client.messages.create(
                              body=body,
                              from_='+19522609588',
                              to=to
                          )


    print(body)
    print(to)



INTERNATIONAL = r"\+2519\d{8}$"  # E.16 format phone number
#Inter = r"\09\d{8}$" 
def formated_number(number):
        """convert number to E.16 format
        It need to be changed b/c twilio require
        E.16 format number."""
        if re.match(INTERNATIONAL, number):
            return number
        else:
            return f'+251{number.lstrip("0")}'
       





# ACCOUNT_SID = config("ACCOUNT_SID_TRIAL", cast=str) 
# AUTH_TOKEN = config("AUTH_TOKEN_TRIAL", cast=str)

# MSG_SERVICE = config("MSG_SERVICE", cast=str)
# INTERNATIONAL = r"\+2519\d{8}$"  # E.16 format phone number

   
def send_verification(number):
        """ Send 5 digit verification code to user when required."""
        verification =client.verify.services(
        SERVICE_ID
        ).verifications.create(to=formated_number(number), channel="sms")
        return verification.status

def verify_code(number, code):
        """ verify users verification code based on their number """
        verification_check = client.verify.services(
        SERVICE_ID
        ).verification_checks.create(to=formated_number(number), code=code)
        return verification_check.status

    