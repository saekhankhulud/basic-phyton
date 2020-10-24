import smtplib
import os
import imghdr
from email.message import EmailMessage
email_id = os.environ.get('EMAIL_ADDRESS')
email_pass = os.environ.get('EMAIL_PASS')

to = ['khuludsaekhan@gmail.com, khulud.saekhan@ui.ac.id']

msg = EmailMessage()
msg['Subject'] = 'Coba meneh'
msg['From'] = email_id
msg['To'] = to
msg.set_content("Please ke-attach dong ah")


with open('meme.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id, email_pass)
    smtp.send_message(msg)