import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def send_order_email(to_email: str, order_summary: str):
    smtp_host = os.getenv("SMTP_HOST", "localhost")
    smtp_port = int(os.getenv("SMTP_PORT", 1025))

    from_email = "noreply@furniturestore.local"
    subject = "Your Furniture Order"

    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject

    body = f"Thank you for your order!\n\n{order_summary}"
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.send_message(message)
            print(f"Order email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
