import smtplib
import datetime as dt
import random

my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as q_file:
        all_q = q_file.readlines()  # readlines make the text file convert to list
        quote = random.choice(all_q)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr="FROM EMAIL",
            to_addrs="TO EMAIL",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
        connection.quit()
