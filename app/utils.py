from passlib.context import CryptContext
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

def hash(plain_password) :
    return pwd_context.hash(plain_password)

def verify_password(plain_password, hashed_password) :
    return pwd_context.verify(plain_password, hashed_password)



def send_text(number : str, code : int):
    message = f"Your verification code is {code}"
    url = f'''http://66.45.237.70/api.php?username=01782267068&password=6BNPADM4&number={number}&message={message}'''
    payload  = {}
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers = headers, data = payload)
    print(response.text.encode('utf8'))


def send_email(email : str, code : int):
    sender_name = "ReDevOps"
    sender_email = "noreply@redevops.store"
    sender_password = "#&e6&pg9^42$YQ"
    receiver_email = email
    subject = "ReDevOps Verification Email"
    smtp_server = "smtp0001.neo.space"
    smtp_port = 587  # If using SSL/TLS, Should change the port to 465
    message = f"Your verification code is {code}"
    # Creating a multipart message and set headers
    msg = MIMEMultipart()
    msg["From"] = f"{sender_name} <{sender_email}>"
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Adding body to email
    msg.attach(MIMEText(message, "plain"))

    # Creating SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.ehlo()
        server.login(sender_email, sender_password)
        server.send_message(msg)


def mobile_number_verification(mobile_number) :
    if len(mobile_number) != 11 :
        return False
    if mobile_number[:2] != "01" :
        return False
    return True