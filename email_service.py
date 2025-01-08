import smtplib
from email.mime.text import MIMEText

def send_email(email: str, message: str):
    sender_email = "venkateshramkumar3@gmail.com"
    app_password = "kizz qqao hkap fofr"

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