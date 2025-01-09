import smtplib
from email.mime.text import MIMEText
from os import environ as env


def send_email(email: str, message: str):
    sender_email = env.get('SENDER_EMAIL')
    app_password = env.get('APP_PASSWORD')

    msg = MIMEText(message)
    msg["Subject"] = "Notification"
    msg["From"] = sender_email
    msg["To"] = email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")