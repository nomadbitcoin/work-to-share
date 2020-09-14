import login
from twilio.rest import Client

def sendSms(text, return_error=False):
    try:
        twilio_ssid = login.getToken("twilio_ssid")
        twilio_token = login.getToken("twilio_token")
        
        client = Client(twilio_ssid, twilio_token)
        client.messages.create(from_='+17547145366',to='+5547988917321', body=text)
        return True
    except Exception as error:
        if return_error==True:
            return error
        else:
            return False