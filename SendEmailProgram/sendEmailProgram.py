# We need to activate Less secure in Gmail settings

import smtplib

sender = "ganceaali@gmail.com"
receiver = "ganceaali@gmail.com"
password = "jOeeprost"
subject = "test"
body = "This is a test"

message = f"""From: {sender}
To: {receiver}
Subjext: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:

    server.login(sender,password)
    print("Logged in...")

    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")