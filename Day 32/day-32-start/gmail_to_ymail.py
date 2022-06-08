import smtplib

# from gmail to ymail

my_gmail = "myglomail1@gmail.com"
gmail_pass = "terah0704"

my_ymail = "joesephmensah@yahoo.com"
ymail_pass = "koypluyogfkemdou"


def send_from_gmail_ymail(msg):
    "Sends mail from specified gmail to yahoo mail"
    global ymail_pass, gmail_pass, my_gmail, my_ymail

    # create new connection and start sending email service
    with smtplib.SMTP(host="smtp.gmail.com") as connection:

        # start ttls to secure email
        connection.starttls()

        # login to email
        connection.login(user=my_gmail, password=gmail_pass)

        # send email
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=my_ymail,
            msg=msg,
        )

        # # close connection
        # connection.close()


