import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

SERVER = "smtp.gmail.com"
PORT = 587
FROM = "saiteja5421@gmail.com"
TO = "saiteja5421@gmail.com"
PASS = "fophhpkptgqicvnp"

msg = MIMEMultipart()
cc= "168r1a0494@gmail.com"
subject = f"sending mail using python"
msg["Subject"] = subject
msg["From"] = FROM
msg["To"] = TO
msg["Cc"] = cc
recpt = cc.split(",")+[TO]
print(recpt)
content = "sending mail using python to check its correct or not" 
msg.attach(MIMEText(content))
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, recpt, msg.as_string())
print("Email Sent....")

server.quit()