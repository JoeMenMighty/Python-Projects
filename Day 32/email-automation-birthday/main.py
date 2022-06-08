from birthday_checker import check_birthday_list, pick_template
from send_email_from_gmail_ymail import send_from_gmail_ymail

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
email_list = check_birthday_list()
template = pick_template()

# check and send mail
if len(email_list) != 0:
    print("There are birthdays , sending emails.......")
    for val in email_list:
        template_edited = template.replace("[NAME]", val['name'])
        msg = f"Subject: It's your birthday\n\n {template_edited}"
        email = val['email']
        send_from_gmail_ymail(msg, email)
    print("all emails sent !!!!")
else:
    print("No birthdays today")

# 4. Send the letter generated in step 3 to that person's email address.
