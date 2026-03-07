import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_photo_email(receiver_email, photo_path):

    msg = EmailMessage()
    msg["Subject"] = "Photo from DrishyaMitra"
    msg["From"] = EMAIL_USER
    msg["To"] = receiver_email
    msg.set_content("Here is your requested photo.")

    with open(photo_path, "rb") as f:
        file_data = f.read()
        file_name = photo_path.split("/")[-1]

    msg.add_attachment(file_data, maintype="image", subtype="octet-stream", filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)

    return "Email sent successfully"