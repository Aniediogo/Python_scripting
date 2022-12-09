from email.message import EmailMessage
from mysec import password
import ssl
import smtplib

email_sender = 'angelamitchelle7@gmail.com'
email_password = password

email_receiver = 'citax42166@esmoud.com'

subject = 'View my first python project'
body = """
Hi Gela,
I trust you are doing okay? kindly let me know what you think of this project
I created it to enable me have more knowledge of python and it think its supercool.
I will talk to you again. 
Bye!!!
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())