import smtplib
import puremagic
from email.message import EmailMessage

username="adygoyal07@gmail.com"
password="rayxvhkcbcuceuby"
receiver="adygoyal07@gmail.com"
def send_email(image_path):
    print("Send Email started")
    email_message=EmailMessage()
    email_message["Subject"]="New customer showed up!!"
    email_message.set_content("Hey, We just saw a new customer")

    with open(image_path,"rb") as file:
        content=file.read()
    email_message.add_attachment(content,maintype="image",subtype="png")

    gmail=smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username,password)
    gmail.sendmail(username,receiver,email_message.as_string())
    gmail.quit()
    print("Send email ended")
