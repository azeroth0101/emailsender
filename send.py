import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up your email and SMTP server information
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_address = 'your_email_address@gmail.com'
email_password = 'your_email_password'

# Set up the message you want to send
subject = 'Subject of your email'
body = 'Content of your email'
sender_name = 'Your Name'
recipient_file = 'email_list.csv'

# Read the list of recipients from a CSV file
with open(recipient_file, 'r') as f:
    reader = csv.reader(f)
    recipients = [row[0] for row in reader]

# Set up the message headers and body
message = MIMEMultipart()
message['From'] = sender_name + ' <' + email_address + '>'
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Set up the SMTP connection and send the email to each recipient
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(email_address, email_password)
    for recipient in recipients:
        message['To'] = recipient
        smtp.sendmail(email_address, recipient, message.as_string())
        print(f"Email sent to {recipient}")
