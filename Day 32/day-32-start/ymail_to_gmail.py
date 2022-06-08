import smtplib

# from gmail to ymail

my_gmail = "myglomail1@gmail.com"
gmail_pass = "terah0704"

my_ymail = "joesephmensah@yahoo.com"
ymail_pass = "koypluyogfkemdou"


# create new connection and start sending email service
with smtplib.SMTP(host="smtp.mail.yahoo.com") as connection:

    # start ttls to secure email
    connection.starttls()

    # login to email
    connection.login(user=my_ymail, password=ymail_pass)

    # send email
    connection.sendmail(
        from_addr=my_ymail,
        to_addrs=my_gmail,
        msg=" Subject: {Testing SMTP}\n\n{Hello, This is a test mail from Yahoo Mail}"
    )

# close connection
# use close when you don't use with
# connection.close()


