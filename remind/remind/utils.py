from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client
import os
from dotenv import load_dotenv
from .messages import REMINDER_MESSAGES
import random

load_dotenv()


def remindByMail(To_mails: list) -> None:
    message = Mail(
        from_email="amishdfghj27@gmail.com",
        to_emails=To_mails,
        subject="Test Email",
        html_content="<strong>This is a test email from Django + SendGrid!</strong>"
    )

    try:
        sg = SendGridAPIClient("SENDGRID_API_KEY")
        response = sg.send(message)
        print("Email sent succcessfully")
        print("Status Code", response.status_code)
        
    except Exception as e:
        print("Error:", e)


def remindByMessage() -> None:
    body = random.choice(REMINDER_MESSAGES)

    client = Client(
        os.getenv("TWILLIO_ACCOUNT_ID"),
        os.getenv("TWILLIO_AUTH_TOKEN")
    )
    phone_numbers = os.getenv("PHONE_NUMBERS", "").split(", ")

    for number in phone_numbers:
        try:
            msg = client.messages.create(
                body=body,
                messaging_service_sid=os.getenv("TWILLIO_SERVICE_SID"),
                to=f"+91{number}"
            )

            print(f"Message sent to {number}")
            print("Status:", msg.status)

        except Exception as e:
            print(f"Error sending to {number}: {e}")