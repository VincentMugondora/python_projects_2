# go over to uor gmail account and setup 2 factor authentication
# genarate app password
# create a function to send the email


from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = "vincent@uncommon.org"
email_password = password

email_receiver = "Vinmugondora@gmail.com"

subject = "Don't forget to subscribe"
body = """
Hi there, When you watch a video please hit subscribe and leave a like!
\n
From,
Vincent Mugondora
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)



context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
