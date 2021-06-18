import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from login import *
from lotto import *

sender_email_id = 'stuurmanmzwandile@gmail.com'
receiver_email_id = ['kiyaamudienkhan@gmail.com', 'aslamdien90@gmail.com','siyanjomeni@gmail.com','mpendulokhozamk2@gmail.com','sithandathuzipho@gmail.com']
password = input("Enter your password: ")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = ', ' .join(receiver_email_id)
msg['Subject'] = subject
body = "What do you say now!!!\n"

msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication

s.login(sender_email_id, password)
# message to be sent

# sending the mail
s.sendmail(sender_email_id, receiver_email_id, text)
# terminating the session
s.quit()
