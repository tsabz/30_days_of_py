import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'tezt3311@gmail.com'
password = 'Algodj3311$'

def send_mail(text='Email Body', subject='Hello world', 
from_email='TEZT <tezt3311@gmail.com>', to_emails=None):
    assert isinstance(to_emails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ",".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    html_part = MIMEText("<h1>This is working</h1>", 'html')
    # login to my smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email, to_emails, msg)
    server.quit()