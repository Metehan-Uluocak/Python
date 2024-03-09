import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(sender_email, sender_password, to_email, subject, message_body):
    try:
        
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject

        
        message.attach(MIMEText(message_body, 'plain'))

       
        with smtplib.SMTP("smtp.gmail.com", 587) as email_server:
            # Start TLS encryption
            email_server.starttls()

            # Login to the email account
            email_server.login(sender_email, sender_password)

            # Send the email
            email_server.sendmail(sender_email, to_email, message.as_string())

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Please check your email and password.")
    except smtplib.SMTPException as e:
        print(f"Error: Unable to send email. {e}")
    except Exception as e:
        print(f"Error: {e}")


