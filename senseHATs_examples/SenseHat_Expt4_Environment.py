#==== MIME is multipurpose internet mailing extension =========
import smtplib
from email.message import EmailMessage
import ssl
# =============================================================

from sense_hat import SenseHat
import time
from time import asctime

email_sender = "cs3907.edgelab@gmail.com"
email_password = "uhoj xyxj apmc knms"
email_receiver = "kartik.bulusu@gmail.com"

#sense = SenseHat()
#temp = round(sense.get_temperature()*1.8+32)
#humidity = round(sense.get_humidity())
#pressure = round(sense.get_pressure())
#message = ' T=%dF, H=%d, P =%d ' %(temp,humidity,pressure)
#sense.show_message(message, scroll_speed=(0.08), text_colour = [200, 240, 200], back_colour = [0,0,0])
#
#log = open('weather.txt', "a")
now = str(asctime())
#log.write(now + " " + message + '\n')
#log.close()

msg = EmailMessage()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = "Temp Rasp"

#body = """
#Testing the email
#"""

header = ' FirstName LastName sent the following data on ' + now + '\n'
#data = ' T=%dF, H=%d, P =%d \n' %(temp,humidity,pressure)
#body = header + data
body = header

msg.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, msg.as_string())
    
    